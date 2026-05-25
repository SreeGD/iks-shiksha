# RAG / Source Configuration

Two upstream systems supply the source material for this curriculum. Both run locally on the author's machine; neither is a hard dependency at *teach* time — generated lessons stand on their own.

## 1. vidya-karana-kg

**Location:** `/Users/sree/Projects/vidya-karana-kg/`
**Corpus:** 89,667 chunks; 145,486-node knowledge graph
- Śrīmad Bhāgavatam (28k)
- Bhagavad-gītā As It Is (8.5k)
- Caitanya Caritāmṛta (12k)
- Śrīla Prabhupāda books + letters (22k)
- Radha Ayurveda subset

**Use for:** scriptural citations and philosophical framing on the cosmology / wellness / ecology / ethics modules.

### MCP server (streamable-http)

```bash
cd /Users/sree/Projects/vidya-karana-kg
KG_MCP_TRANSPORT=streamable-http .venv/bin/kg-mcp     # binds 127.0.0.1:8766
```

### Direct Python API (preferred for authoring scripts)

```python
from kg.retrieval import get_kg_context
from kg.store.chroma import open_chroma, get_corpus_collection

col = get_corpus_collection(open_chroma())
result = get_kg_context(
    query="How does the Bhāgavatam describe the five gross elements?",
    collection=col,
    top_k=10,
    max_hops=2,
)
# result.chunks -> list of ChunkResult(text, score, source, ...)
```

### Cache shape

Per-day cache file `module-XX/.rag-cache/day-NN.json`:
```json
{
  "query": "<the question we asked>",
  "mode": "kg_augmented",
  "top_k": 10,
  "fetched_at": "<ISO timestamp>",
  "chunks": [{"chunk_id": "...", "text": "...", "score": 0.89, "source": "SB 11.14.21"}],
  "entities": [...],
  "notes": [...]
}
```

## 2. SutraGanita

**Location:** `/Users/sree/Projects/SutraGanita/`
**Corpus:** 70 PDFs in `content/`; embedded in Supabase pgvector
- *Vedic Mathematics* (Bharati Krishna Tirthaji, 1965)
- *Fundamental and Vedic Mathematics*
- Trachtenberg system
- Magic-square treatises
- Per-sūtra handbooks (Prārambha / Madhyama / Pravīṇa)

**Use for:** Vedic-math modules (Bindu Paddhati / dot addition, multiplication by 11, complement subtraction, multiplication close to 10/100, magic squares).

### Worksheet generation API

SutraGanita does **not** expose a retrieval-only endpoint. It exposes a streaming worksheet-generation endpoint backed by an internal retrieverNode.

```bash
cd /Users/sree/Projects/SutraGanita
npm run dev                                          # http://localhost:3000
# Authenticate once via the web UI (Supabase email/password)
# Then capture the session cookie from devtools
```

```bash
curl -N -X POST http://localhost:3000/api/generate \
  -H "Content-Type: application/json" \
  -H "Cookie: <session-cookie>" \
  -d '{
    "mode": "structured",
    "ageGroup": "11-13",
    "difficulty": "intermediate",
    "topic": "Bindu Paddhati for long addition",
    "sutraId": "shuddha",
    "outputKit": "both",
    "language": "en"
  }'
```

Stream ends with a `{"type":"done", content, studentContent, sources, cached, cachedAt}` event. Save the parsed payload to `module-XX/.sutraganita-cache/day-NN.json`.

### Cache shape

```json
{
  "request": {"mode": "structured", "ageGroup": "11-13", "topic": "...", "sutraId": "..."},
  "fetched_at": "<ISO timestamp>",
  "teacher_kit_md": "<markdown>",
  "student_kit_md": "<markdown>",
  "sources": ["Vedic Mathematics.pdf", "..."]
}
```

### Fallback if SutraGanita isn't running

1. **Direct Supabase access** — connect to the same database as SutraGanita and call `match_chunks(query_embedding, threshold, count)` over the `knowledge_chunks` table.
2. **Direct PDF read** — `/Users/sree/Projects/SutraGanita/content/` contains the raw source PDFs. Read directly and quote with the filename as `source`.

## Citation discipline

Whichever path was used, the citation in the lesson **must match** an entry in the corresponding cache file's `sources` (or the verbatim PDF filename, for the fallback path). The verification step at the end of Phase B greps lessons for citations and fails if any orphan citations exist.
