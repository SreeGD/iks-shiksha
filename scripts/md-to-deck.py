#!/usr/bin/env python3
"""Build a Marp-style deck from a curriculum day/section markdown file.

Consolidates the per-day deck preprocessing that used to be a
`md-tables-to-lists.py | awk` pipeline, and adds overflow-aware splitting so
dense sections no longer get dropped by generate-pptx.js's IKS_LENIENT guard.

Pipeline:
  1. Tables → bullet lists (html2pptx silently drops <table> elements).
  2. Split into slides at every H2/H3 (demote H3 → H2 for visual consistency).
  3. Within a section, pack content blocks under a per-slide budget; overflow
     spills onto "(cont.)" slides. Long list blocks split by item.
  4. Emit with a leading `---` so the first (title/prelude) block is slide 1.

Note: we deliberately do NOT escape leading "- X" to "– X" (the legacy awk
did). That escape turned real bullet items into paragraphs starting with an
en-dash, which the html2pptx validator then rejected ("starts with bullet
sym") — causing skips. Left as "- X", such lines parse as proper <li> and are
never flagged; bullets inside code blocks are escaped by generate-pptx.js
itself.

Usage:
  python3 md-to-deck.py path/to/day.md            # writes deck to stdout
  BUDGET=14 python3 md-to-deck.py path/to/day.md   # tune slide density

Only feeds the slide deck — source markdown / PDF / DOCX outputs are untouched.
"""

import math
import os
import re
import sys

# Approx body lines that fit on one 720×405pt slide below the heading.
# Conservative on purpose: html2pptx rejects a slide whose content overflows
# the frame, so under-filling is much cheaper than over-filling.
BUDGET = int(os.environ.get('IKS_DECK_BUDGET', '11'))
CHARS_PER_LINE = 76  # wrap width for 12pt body in the ~656pt content frame


# ---------------------------------------------------------------------------
# 1. Tables → bullet lists
# ---------------------------------------------------------------------------

def _is_separator(cells):
    joined = ''.join(cells).replace(' ', '')
    return joined != '' and set(joined) <= {'-', ':'}


def tables_to_lists(text: str) -> str:
    lines = text.split('\n')
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('|') and i + 1 < n:
            nxt = lines[i + 1].strip()
            nxt_cells = [c.strip() for c in nxt.strip('|').split('|')] if nxt.startswith('|') else []
            if nxt.startswith('|') and _is_separator(nxt_cells):
                rows = []
                while i < n and lines[i].strip().startswith('|'):
                    rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
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
                    key_fmt = key if '*' in key else f"**{key}**"
                    rest = ' · '.join(c for c in r[1:] if c)
                    out.append(f"- {key_fmt}{(' — ' + rest) if rest else ''}")
                out.append('')
                continue
        out.append(line)
        i += 1
    return '\n'.join(out)


# ---------------------------------------------------------------------------
# 2-3. Section split + overflow packing
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r'^(#{2,3})\s+(.*)$')
NESTED_ITEM_RE = re.compile(r'^(\s+)([-*+]\s+|\d+\.\s+)(.*)$')


def flatten_lists(text: str) -> str:
    """Promote indented (nested) list items to top level.

    generate-pptx.js's slide parser is not indentation-aware: an indented
    "   - item" is not recognised as a list marker, so it gets folded into a
    paragraph starting with "- " — which the html2pptx validator rejects
    ("starts with bullet sym"). Flattening to a single level keeps the content
    as real <li> bullets. Nested ordered items are demoted to bullets. Code
    fences are left untouched.
    """
    out = []
    in_code = False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        m = NESTED_ITEM_RE.match(line)
        if m:
            marker = m.group(2)
            if re.match(r'\d+\.', marker):
                marker = '- '  # demote nested ordered → bullet
            out.append(marker + m.group(3))
        else:
            out.append(line)
    return '\n'.join(out)


def normalize_blockquotes(text: str) -> str:
    """Strip list markers from blockquote lines and separate former items with
    empty quote lines.

    generate-pptx.js renders a blockquote by joining its lines with spaces into
    a single <p>. If a quote contains "> - item", that <p> begins with "- " and
    the html2pptx validator rejects it ("starts with bullet sym"). Stripping the
    marker (and inserting a blank "> " between items so they split into separate
    quote paragraphs) keeps the content and avoids the leading bullet symbol.
    """
    lines = text.split('\n')
    out = []
    i, n = 0, len(lines)
    while i < n:
        if lines[i].lstrip().startswith('>'):
            rebuilt = []
            while i < n and lines[i].lstrip().startswith('>'):
                content = re.sub(r'^\s*>\s?', '', lines[i])
                m = re.match(r'^\s*([-*+]|\d+\.)\s+(.*)$', content)
                if m:
                    if rebuilt and rebuilt[-1].strip() != '>':
                        rebuilt.append('>')
                    rebuilt.append('> ' + m.group(2))
                else:
                    rebuilt.append('> ' + content if content else '>')
                i += 1
            out.extend(rebuilt)
        else:
            out.append(lines[i])
            i += 1
    return '\n'.join(out)


def line_cost(line: str) -> int:
    L = len(line.rstrip())
    return max(1, math.ceil(L / CHARS_PER_LINE)) if L else 1


def parse_blocks(body_lines):
    """Group a section body into blocks (blank-line separated; code fences kept
    whole). Returns list of block-line-lists."""
    blocks = []
    i, n = 0, len(body_lines)
    while i < n:
        if body_lines[i].strip() == '':
            i += 1
            continue
        if body_lines[i].lstrip().startswith('```'):
            chunk = [body_lines[i]]
            i += 1
            while i < n and not body_lines[i].lstrip().startswith('```'):
                chunk.append(body_lines[i]); i += 1
            if i < n:
                chunk.append(body_lines[i]); i += 1
            blocks.append(chunk)
            continue
        chunk = []
        while i < n and body_lines[i].strip() != '' and not body_lines[i].lstrip().startswith('```'):
            chunk.append(body_lines[i]); i += 1
        blocks.append(chunk)
    return blocks


def is_list_block(chunk):
    items = [l for l in chunk if l.strip()]
    return bool(items) and all(re.match(r'^\s*([-*+]|\d+\.)\s', l) for l in items)


def block_cost(chunk):
    # Each physical line wraps to >=1 rendered line; list items and short lines
    # also carry vertical margin, so add a per-line allowance plus block spacing.
    cost = 0
    for l in chunk:
        cost += line_cost(l)
        if re.match(r'^\s*([-*+]|\d+\.)\s', l):
            cost += 0.4  # list-item margin
    return cost + 1


def split_list_block(chunk, budget):
    """Split a too-long list block into sub-lists each within budget."""
    out, cur, cur_cost = [], [], 0
    for item in chunk:
        c = line_cost(item)
        if cur and cur_cost + c > budget:
            out.append(cur); cur, cur_cost = [], 0
        cur.append(item); cur_cost += c
    if cur:
        out.append(cur)
    return out


def build_deck(text: str) -> str:
    text = tables_to_lists(text)
    text = flatten_lists(text)
    text = normalize_blockquotes(text)
    lines = text.split('\n')

    # Partition into prelude + sections.
    prelude, sections, cur = [], [], None
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            heading = '## ' + m.group(2).strip()  # demote ### → ##
            cur = {'heading': heading, 'body': []}
            sections.append(cur)
        elif cur is None:
            prelude.append(line)
        else:
            cur['body'].append(line)

    slides = []  # each slide is a list of markdown lines
    if any(l.strip() for l in prelude):
        slides.append(list(prelude))

    for sec in sections:
        heading = sec['heading']
        blocks = parse_blocks(sec['body'])
        if not blocks:
            slides.append([heading])  # divider heading (no body)
            continue

        cur_lines = [heading]
        cur_cost = 0
        placed_any = False
        for blk in blocks:
            # Pre-split overlong list blocks into item-groups.
            if is_list_block(blk) and block_cost(blk) > BUDGET:
                subs = split_list_block(blk, BUDGET)
            else:
                subs = [blk]
            for sub in subs:
                bc = block_cost(sub)
                if placed_any and cur_cost + bc > BUDGET:
                    slides.append(cur_lines)
                    cur_lines = [heading + ' (cont.)']
                    cur_cost = 0
                cur_lines.append('')
                cur_lines.extend(sub)
                cur_cost += bc
                placed_any = True
        slides.append(cur_lines)

    # Emit: leading `---`, then each slide separated by `---`.
    parts = []
    for s in slides:
        parts.append('---')
        parts.append('')
        parts.append('\n'.join(s).rstrip())
        parts.append('')
    return '\n'.join(parts).rstrip() + '\n'


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    sys.stdout.write(build_deck(text))


if __name__ == '__main__':
    main()
