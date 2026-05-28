#!/usr/bin/env python3
"""Filter: convert GitHub-flavoured markdown tables into bullet lists.

html2pptx (used by generate-pptx.js) silently drops <table> elements, leaving
blank gaps on slides. For slide decks we convert each table into a definition-
style bullet list so the content survives:

    | Sanskrit | State  | Property |
    |----------|--------|----------|
    | Pṛthvī   | Solid  | Hardness |

becomes

    *Each row: Sanskrit · State · Property.*

    - **Pṛthvī** — Solid · Hardness

Usage:
    python3 md-tables-to-lists.py path/to/file.md   # reads file, writes stdout
    cat file.md | python3 md-tables-to-lists.py      # reads stdin, writes stdout

Only affects slide-deck preprocessing — the source markdown and the
prose/PDF/DOCX outputs are untouched.
"""

import sys


def _is_separator(cells):
    """A markdown table separator row: only -, :, space between pipes."""
    joined = ''.join(cells).replace(' ', '')
    return joined != '' and set(joined) <= {'-', ':'}


def tables_to_lists(text: str) -> str:
    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        # A table starts with a pipe row immediately followed by a separator row.
        if stripped.startswith('|') and i + 1 < n:
            nxt = lines[i + 1].strip()
            nxt_cells = [c.strip() for c in nxt.strip('|').split('|')] if nxt.startswith('|') else []
            if nxt.startswith('|') and _is_separator(nxt_cells):
                rows = []
                while i < n and lines[i].strip().startswith('|'):
                    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                    rows.append(cells)
                    i += 1
                header = rows[0]
                body = [r for r in rows[1:] if not _is_separator(r)]
                if len(header) > 1:
                    out.append(f"*Each row: {' · '.join(c for c in header if c)}.*")
                    out.append('')
                for r in body:
                    if not any(c for c in r):
                        continue
                    key = r[0]
                    # Avoid nested emphasis: if the key already contains markdown
                    # emphasis (e.g. *ākāśa*), keep it as-is rather than wrapping
                    # in ** (which would produce broken ***...***).
                    key_fmt = key if '*' in key else f"**{key}**"
                    rest = ' · '.join(c for c in r[1:] if c)
                    out.append(f"- {key_fmt}{(' — ' + rest) if rest else ''}")
                out.append('')
                continue
        out.append(line)
        i += 1
    return '\n'.join(out)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    sys.stdout.write(tables_to_lists(text))


if __name__ == '__main__':
    main()
