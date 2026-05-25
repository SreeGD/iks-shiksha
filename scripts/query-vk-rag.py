#!/usr/bin/env python3
"""Query the vidya-karana-kg RAG and write a cache JSON for a single lesson.

Usage:
    python scripts/query-vk-rag.py \
        --query "How does the Bhagavatam describe the five gross elements?" \
        --out curriculum/middle/module-02-panchabhuta/.rag-cache/day-01.json \
        [--top-k 10]

Requires CHROMADB_PATH (defaults to ../vidya-karana/chromadb relative to vidya-karana-kg).
Run from any cwd; the script handles paths.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

VK_KG = Path("/Users/sree/Projects/vidya-karana-kg")
CHROMADB_DEFAULT = "/Users/sree/Projects/vidya-karana/chromadb"

sys.path.insert(0, str(VK_KG))
os.environ.setdefault("CHROMADB_PATH", CHROMADB_DEFAULT)

from kg.retrieval import get_kg_context  # noqa: E402
from kg.store.chroma import open_chroma, get_corpus_collection  # noqa: E402
from kg.store.snapshot import load_latest  # noqa: E402


def hydrate(chunk_ids, col):
    hit = col.get(ids=list(chunk_ids), include=["documents", "metadatas"])
    by_id = {cid: (doc, meta) for cid, doc, meta in
             zip(hit["ids"], hit["documents"], hit["metadatas"])}
    return by_id


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--query", required=True)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--top-k", type=int, default=10)
    p.add_argument("--max-hops", type=int, default=2)
    args = p.parse_args()

    g = load_latest(VK_KG / "data" / "snapshots")
    col = get_corpus_collection(open_chroma())
    res = get_kg_context(query=args.query, g=g, collection=col)

    ids = [c.chunk_id for c in res.chunks[: args.top_k]]
    bodies = hydrate(ids, col)

    chunks_out = []
    for c in res.chunks[: args.top_k]:
        doc, meta = bodies.get(c.chunk_id, (None, None))
        chunks_out.append({
            "chunk_id": c.chunk_id,
            "score": c.score,
            "seed_score": c.seed_score,
            "overlap_score": c.overlap_score,
            "entity_ids": list(c.entity_ids),
            "source": (meta or {}).get("chunk_id") or (meta or {}).get("source_text") or "",
            "verse_ref": (meta or {}).get("verse_ref", ""),
            "author": (meta or {}).get("author", ""),
            "subdomain": (meta or {}).get("subdomain", ""),
            "text": doc or "",
        })

    payload = {
        "query": args.query,
        "mode": "kg_augmented",
        "top_k": args.top_k,
        "max_hops": args.max_hops,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "chunks": chunks_out,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"wrote {len(chunks_out)} chunks → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
