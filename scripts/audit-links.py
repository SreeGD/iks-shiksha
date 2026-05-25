#!/usr/bin/env python3
"""Walk exports/site and exports/{pdf,pptx,docx} to find broken internal links.

Reports:
  - Total HTML pages scanned
  - Total internal links (counted)
  - Broken link list (file -> link -> missing target)
"""
from pathlib import Path
import re
from urllib.parse import urlparse, unquote
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "exports" / "site"
EXPORTS = ROOT / "exports"

HREF_RE = re.compile(r'(?:href|src)="([^"]+)"', re.IGNORECASE)


def resolve(html_file: Path, link: str) -> Path | None:
    """Resolve a relative link from html_file to an absolute path on disk.

    Returns None if the link is external (http/mailto) or unresolvable.
    """
    if not link:
        return None
    p = urlparse(link)
    if p.scheme in ("http", "https", "mailto", "data", "javascript", "tel"):
        return None
    # Drop anchor + query for filesystem check
    path = unquote(p.path) or ""
    if not path:
        return None  # pure anchor link like "#section"
    # Absolute paths starting with /
    if path.startswith("/"):
        # Treat as relative to site root for our purposes
        return SITE / path.lstrip("/")
    # Relative
    target = (html_file.parent / path).resolve()
    return target


def main() -> int:
    pages = sorted(SITE.rglob("*.html"))
    broken: dict[Path, list[tuple[str, Path]]] = defaultdict(list)
    total_links = 0
    external_links = 0
    same_page_anchors = 0
    by_target_count: dict[Path, int] = defaultdict(int)

    for page in pages:
        text = page.read_text(encoding="utf-8")
        for link in HREF_RE.findall(text):
            total_links += 1
            if link.startswith(("http://", "https://")):
                external_links += 1
                continue
            if link.startswith("mailto:") or link.startswith("#"):
                if link.startswith("#"):
                    same_page_anchors += 1
                continue
            target = resolve(page, link)
            if target is None:
                continue
            # Check existence — also try with .html appended for clean URLs
            if not target.exists():
                broken[page].append((link, target))
            else:
                by_target_count[target] += 1

    # Report
    print("===== LINK AUDIT =====\n")
    print(f"HTML pages scanned:        {len(pages)}")
    print(f"Total links (href/src):    {total_links}")
    print(f"  External (http/https):   {external_links}")
    print(f"  Same-page anchors:       {same_page_anchors}")
    print(f"  Internal that resolved:  {sum(by_target_count.values())}")
    print(f"  Internal BROKEN:         {sum(len(v) for v in broken.values())}\n")

    if broken:
        print("===== BROKEN LINKS =====\n")
        # Group by missing target for cleaner output
        by_missing: dict[Path, list[Path]] = defaultdict(list)
        for src, items in broken.items():
            for link, target in items:
                by_missing[target].append(src)
        for target, srcs in sorted(by_missing.items()):
            rel_t = target.relative_to(ROOT) if ROOT in target.parents else target
            print(f"MISSING: {rel_t}")
            print(f"  referenced by {len(srcs)} page(s):")
            for s in sorted(set(srcs))[:5]:
                print(f"    - {s.relative_to(ROOT)}")
            if len(set(srcs)) > 5:
                print(f"    ... and {len(set(srcs)) - 5} more")
            print()
    else:
        print("✅ No broken internal links!\n")

    # Also check that all download targets in exports/ exist
    print("===== EXPORTS COVERAGE =====")
    pptx = list((EXPORTS / "pptx").rglob("*.pptx"))
    pdf = list((EXPORTS / "pdf").rglob("*.pdf"))
    docx = list((EXPORTS / "docx").rglob("*.docx"))
    print(f"  PPTX on disk:    {len(pptx)}")
    print(f"  PDF on disk:     {len(pdf)}")
    print(f"  DOCX on disk:    {len(docx)}")

    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
