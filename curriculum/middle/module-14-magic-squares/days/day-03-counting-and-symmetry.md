# Day 3 — How Many 3×3 Magic Squares Are There?

**Module:** Magic Squares (*Bhadragaṇita*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will (a) discover that the 3×3 magic square with 1–9 is **unique up to symmetry**, (b) list the 8 symmetries (4 rotations + 4 reflections), and (c) explain why 5 must occupy the centre.

## Materials

- Printed 3×3 grids (5 per pair) with the digits 1–9 listed
- Coloured pencils (3 colours per student)
- The Day-1 square visible on the board

## Vocabulary introduced today

- *symmetry* — a way of moving or flipping a figure so that it looks the same in a different orientation.
- *rotation* — turning around a centre by 90°, 180°, or 270°.
- *reflection* — flipping across a line (horizontal, vertical, or one of the diagonals).

## Lesson flow

### Warm-up (5 min)

- Daily fluency: "row sums to 15 — give me the missing number." Quick 5 rounds.
- Recall: *"Yesterday we proved the magic constant for a 3×3 is 15. Today's question: how many different 3×3 magic squares with 1–9 are there?"*
- Take 3 student guesses. Write the guesses on the board.

### Core (20 min)

1. **Why 5 must be in the centre.** Argue together:

   - The centre cell sits on 4 lines: the middle row, the middle column, and both diagonals.
   - The four corner cells each sit on 3 lines (a row, a column, and one diagonal).
   - The four edge-middle cells each sit on 2 lines (a row and a column).
   - Sum of all lines = 4 × 15 = 60 (4 lines through the centre? — actually 8 lines total in a 3×3: 3 rows + 3 columns + 2 diagonals. Their sum is 8 × 15 = 120.)
   - In that sum of 120, each cell is counted as many times as the number of lines it sits on: centre counted 4 times, corners 3 times each, edges 2 times each.
   - Total: 4*c* + 3*(corner sum)* + 2*(edge sum)* = 120, where *c* is the centre value.
   - Corner sum + edge sum + *c* = 45 (the total of 1..9). So 3*(corner+edge)* + 4*c* + ... — work it out together. The cleanest answer: *c* = 5.

   *(Don't make them complete the full algebra — show the structure, conclude 5 = centre.)*

2. **Why 2, 4, 6, 8 must be at corners.** The four corner cells must contain the four *even* numbers from 1–9 (which are 2, 4, 6, 8). Reason: corners sit on diagonals — and the diagonals also sum to 15. With 5 in the centre, each diagonal pair must sum to 10. Pairs from 1–9 (excluding 5) summing to 10 are (1,9), (2,8), (3,7), (4,6). The two diagonals use four of these — pick any two pairs. The remaining four numbers (the odd or even ones, depending on the pair choice) end up at the edges. Most cleanly: even numbers at corners.

3. **The 8 symmetries.** Demonstrate on the board. Take the Day-1 square and:
   - Rotate 90°, 180°, 270° — three new arrangements.
   - Reflect horizontally, vertically, and across each diagonal — four more.
   - Total: 8 different-looking arrangements, all the *same* magic square up to symmetry.

   > **Theorem (state, don't prove):** There is exactly **ONE** 3×3 magic square with 1–9, *up to symmetry*. Counting all 8 rotated/reflected versions, you get 8 grids that all share the same essential structure.

### Activity (15 min) — Find all 8

- Each pair starts with the Day-1 square. They must produce all 8 rotated/reflected versions on their own paper.
- Verify each by checking one row sums to 15.
- Pair share: any two pairs swap, and compare — did they get the same 8?

### Wrap-up (5 min)

- *"There is essentially ONE 3×3 magic square with 1–9. Eight different orientations of the same square. Tomorrow we ask: is there a *method* to construct magic squares of any size — not just 3×3?"*
- Preview Day 4: Nārāyaṇa's stair-step method.

## Student-facing content

> **There is only ONE 3×3 magic square with 1–9** — up to symmetry.
>
> The 4 rotations and 4 reflections together produce 8 grid arrangements. They all share the same structure:
> - **5** is in the centre.
> - The four even numbers (2, 4, 6, 8) are at the four corners.
> - The four odd numbers other than 5 (1, 3, 7, 9) are at the four edge-middles.
>
> ```
> 2 | 7 | 6      6 | 7 | 2
> ---------      ---------
> 9 | 5 | 1      1 | 5 | 9    ← reflection (horizontal flip)
> ---------      ---------
> 4 | 3 | 8      8 | 3 | 4
> ```
>
> Eight arrangements; one square.

## Homework

- Take the 3×3 magic square and ask: if I change every entry by adding 10 (so the square becomes 12, 17, 16, 19, 15, 11, 14, 13, 18), is it still a magic square? What's the new magic constant? Verify one row.

## Differentiation

- **One tier up:** Try the same question for 4×4 magic squares — how many are there? Look it up (or estimate). The answer is 880 distinct 4×4 squares up to symmetry; that's a surprise.
- **One tier down:** Just memorise: 5 in the centre, even at corners. Use coloured pencils to highlight the pattern in the Day-1 square.

## Teacher notes

- The full proof that 5 must be central is a beautiful counting argument but takes 10 minutes if done thoroughly. Choose: either do it well, or do it briefly with hand-waves. Don't do it half-fast — that confuses more than it clarifies.
- The "eight symmetries form a group" idea is the *dihedral group D₄*. Don't introduce that name at Middle band — note it for yourself; it returns at Senior band.
- A few students will produce a "9th" square that turns out to be one of the 8 in disguise. Walk them through which symmetry transforms theirs into the original.

## Citation(s) used in this lesson

- Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE — discusses equivalence classes of magic squares (paraphrased).
