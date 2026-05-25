# Teacher Notes — Module 14 Magic Squares (Middle)

## Posture

This module is about **pattern + procedure**. The pattern is the magic constant (a row, column, or diagonal always sums to the same number); the procedure is Nārāyaṇa's stair-step algorithm for constructing any odd-order square. Both are accessible to Middle-band students. The cultural anchor is the 1356 CE *Gaṇita-kaumudī*; the math is the math.

Honesty about history: magic squares were known in many cultures (China, India, Islamic world, Europe). Nārāyaṇa Paṇḍita's *Bhadragaṇita* is the most systematic pre-modern treatment we have in writing, but he was not the sole or first discoverer. Frame him as a brilliant systematiser, not as a lone genius.

## Common misconceptions

1. **"The magic constant is 15 for every magic square."** Only for the 3×3 with numbers 1–9. For an *n × n* magic square with 1..n², the constant is *S = n(n² + 1)/2*. So 5×5 → 65, 4×4 → 34, 7×7 → 175.
2. **"There are many different 3×3 magic squares with 1–9."** There is *one* such square up to symmetry — 8 if you count rotations and reflections. This is a beautiful surprise for students on Day 3.
3. **"The stair-step method only works on odd squares."** Correct — and that's a feature, not a bug. The 4×4 needs a different method (which we show but do not teach in detail at Middle band).
4. **"The Khajuraho square is just decorative."** It is unusually strong: it is panel-magic (every 2×2 block also sums to 34), not just row/column/diagonal magic. This is a real mathematical property; the panel sums are an extra structural constraint beyond the basic definition.
5. **"Magic squares are mystical/protective and must be treated reverently."** Some traditional uses are protective/contemplative; in this curriculum we engage them as combinatorial structures. We acknowledge the cultural context without using ritual framing.

## Differentiation hints

- **Tier up:** Construct a 7×7 magic square (same method, just more cells). Verify the constant equals 175. Bonus: try a "rotated start" — does the algorithm still produce a magic square if you begin in a different cell?
- **Tier down:** Stay with the 3×3. Practise the formula on smaller mental targets. Use coloured tiles for the stair-step rather than writing.

## Differential pacing

- A class strong in arithmetic and pattern-recognition can compress Days 1–3 into 2 days and use the extra time for the 7×7 challenge.
- A class new to grids should NOT skip Day 3 (counting and symmetry). Symmetry intuition feeds the rest of the module.

## Sensitivity notes

- Some students may have heard magic squares described as *yantra*s in religious or astrological contexts at home. Acknowledge: "yes, they have been used that way historically; in this class we study them as mathematics." Don't dismiss the home context; do keep the classroom frame mathematical.
- Avoid the framing "ancient Indians knew this first." Multiple cultures encountered magic squares; Nārāyaṇa's contribution is the *systematic* treatment, not the discovery.

## Project oversight

- Three project formats (poster, demo video, written exposition) — see `assessments/project-brief.md`. Each requires the student to actually *construct* a magic square at least 5×5.
- Common project pitfall: students copy a 5×5 from the internet without using the *turagagati* method. Insist on showing the construction order step-by-step.
- Verification step: every project must include the row/column/diagonal sum-check table. No exceptions — this is what makes it a *mathematical* project rather than a craft project.

## Citation discipline

This module cites a Sanskrit primary source (Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14, 1356 CE) and a modern scholarly secondary source (Plofker 2009). Students should cite the primary source in their project work. Middle-band students give a paraphrase plus citation, not a Sanskrit quote.

## Visualising the stair-step rule

The *turagagati* algorithm for an odd-order *n × n* square:

1. Place 1 in the **top-middle** cell.
2. From the cell containing *k*, move **one up and one to the right** (diagonally up-right) to place *k* + 1.
3. If you go off the top, wrap to the bottom row.
4. If you go off the right, wrap to the left column.
5. If the destination cell is **already filled**, place *k* + 1 in the cell **directly below** the cell containing *k* instead.
6. Repeat until all *n²* cells are filled.

The most common error students make is at step 5: when blocked, they go to the wrong "fallback" cell. Drill this until they can recite "blocked → directly below."

## If you only have 6 days

- Day 1 (combined: what is it + magic constant)
- Day 2 (counting and symmetry — quick)
- Day 3 (stair-step on 3×3)
- Day 4 (stair-step on 5×5)
- Day 5 (Khajuraho + Nārāyaṇa context)
- Day 6 (summative + brief share — no full project)
