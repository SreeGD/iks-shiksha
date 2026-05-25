#!/usr/bin/env python3
"""When the agent-written Middle band already has 10 day files, remove the
generator-added duplicates that use a different naming slug.

The generator wrote day files using slugs from MODULES['days'] in
generate-pack.py. The agents wrote day files with their own choice of slugs.
Both can coexist — but Middle now has 14–20 day files where there should be 10.

Strategy: for each (band, module), keep the FIRST 10 day files when sorted by
filename, deleting any extras. Since both naming schemes start with `day-NN-`,
sorted order goes day-01-*, day-02-*, etc., and within a day-N both schemes
sort alphabetically. We prefer the file that was created first (agent's, since
the generator added new files only when missing) — which means we prefer
files NOT matching the generator's expected slugs.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / 'curriculum'

# Import the generator's MODULES to know which slugs IT used
sys.path.insert(0, str(ROOT / 'scripts'))
from importlib import import_module
spec = import_module('generate-pack')
MODULES = spec.MODULES


def dedupe_pack(band: str, mod_slug: str, mod_data: dict):
    days_dir = CURRICULUM / band / mod_slug / 'days'
    if not days_dir.exists():
        return 0

    files = sorted(days_dir.glob('day-*.md'))
    if len(files) <= 10:
        return 0

    # The generator's slugs for this module
    generator_slugs = {f"day-{i+1:02d}-{d[0]}.md" for i, d in enumerate(mod_data['days'])}

    # Group files by day number (e.g., day-01-* all go together)
    by_day = {}
    for f in files:
        m = re.match(r'day-(\d+)-', f.name)
        if m:
            n = int(m.group(1))
            by_day.setdefault(n, []).append(f)

    removed = 0
    for n, day_files in by_day.items():
        if len(day_files) <= 1:
            continue
        # Prefer the file NOT written by the generator (agent's content is richer)
        generator_files = [f for f in day_files if f.name in generator_slugs]
        non_gen_files = [f for f in day_files if f.name not in generator_slugs]
        if non_gen_files:
            # Keep first non-gen file, remove all gen files + extra non-gen files
            to_remove = generator_files + non_gen_files[1:]
        else:
            # All are generator's; keep first, remove the rest
            to_remove = day_files[1:]
        for f in to_remove:
            f.unlink()
            removed += 1
    return removed


total = 0
for band in ['primary', 'middle', 'senior']:
    for slug, data in MODULES.items():
        r = dedupe_pack(band, slug, data)
        if r:
            print(f"  {band}/{slug}: removed {r}")
            total += r
print(f"Total removed: {total}.")
