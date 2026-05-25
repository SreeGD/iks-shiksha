# Day 4 — The Stair-Step Method (*turagagati*)

**Module:** Magic Squares (*Bhadragaṇita*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will reproduce Nārāyaṇa Paṇḍita's stair-step (*turagagati*) algorithm to construct a 3×3 magic square from scratch, and will be able to state all five steps of the rule.

## Materials

- Whiteboard
- Printed blank 3×3 grids (3 per student)
- A printed copy of the five-step rule (handout) — see Student-facing content below

## Vocabulary introduced today

- *turagagati* (IAST: turaga-gati; lit. "horse-step" or "knight-move") — Nārāyaṇa Paṇḍita's name for the diagonally-upward-right placement rule for constructing odd-order magic squares.

## Lesson flow

### Warm-up (5 min)

- Daily fluency: row-sum-to-15 quick fire. 5 rounds.
- *"You've all built the 3×3 by guessing. Today we replace guessing with a method — Nārāyaṇa Paṇḍita's *turagagati* rule from 1356 CE."*

### Core (20 min)

1. **State the rule.** Five steps. Write them on the board. Have students copy.

   > **The stair-step (*turagagati*) method** — for any odd-order *n × n* square:
   >
   > 1. Place **1** in the **top-middle** cell.
   > 2. From the cell containing *k*, move **one up and one to the right** (diagonally up-right) to place *k* + 1.
   > 3. If you go off the **top edge**, wrap to the **bottom row** (same column you'd have landed in).
   > 4. If you go off the **right edge**, wrap to the **left column** (same row).
   > 5. If the destination cell is **already filled**, place *k* + 1 in the cell **directly below** the cell containing *k* instead.
   >
   > Continue until all *n*² cells are filled.

2. **Demonstrate live on the 3×3.** Walk through cell-by-cell, narrating each step:

   ```
   Step:    1            2            3            4            5
   Cell:  (1, c2)      (off-top,    (off-right,  filled —     (off-top,
                       wrap to      wrap to      go directly  wrap to
                       bottom)      left col)    below)       bottom)
   ```

   The result:

   ```
   . | 1 | .          . | 1 | .          . | 1 | .         . | 1 | .         2 | 1 | .
   ----------         ----------          ----------         ----------         ----------
   . | . | .    →     . | . | .    →     3 | . | .    →    3 | . | .    →     3 | . | .
   ----------         ----------          ----------         ----------         ----------
   . | . | .          . | . | 2          . | . | 2         4 | . | 2         4 | . | 2
   ```

   Continue: 6 (up-right from 5, wraps), 7 (up-right from 6, blocked → below), 8, 9. Final:

   ```
   2 | 7 | 6
   ---------
   9 | 5 | 1
   ---------
   4 | 3 | 8
   ```

   *"Notice — this is exactly the square we discovered on Day 1. The method gave it to us directly, no guessing."*

3. **Why does this work?** Brief preview: the method spreads numbers evenly across rows, columns, and diagonals in a structured way. The full *proof* is Senior-band material. For now, the algorithm produces a magic square; verify by summing.

### Activity (15 min) — Drill

- Use `activities/activity-01-stair-step-drill.md`.
- Each student constructs three 3×3 squares from scratch — first slowly, then faster.
- Pair check: did your neighbour get the same square? Verify magic constant = 15.

### Wrap-up (5 min)

- Quick recap of the 5-step rule.
- Preview Day 5: *"Tomorrow we apply the same algorithm to a 5×5. The rule does not change."*

## Student-facing content

> **The stair-step (*turagagati*) method** — for any odd-order *n × n* magic square:
>
> 1. Place **1** in the **top-middle** cell.
> 2. From the cell with *k*, move **one up and one to the right** to place *k* + 1.
> 3. If you go **off the top**, wrap to the **bottom row**.
> 4. If you go **off the right**, wrap to the **left column**.
> 5. If the destination is **already filled**, place *k* + 1 **directly below** the cell containing *k* instead.
>
> ```
> 2 | 7 | 6
> ---------
> 9 | 5 | 1
> ---------
> 4 | 3 | 8
> ```
>
> Nārāyaṇa Paṇḍita described this method in *Bhadragaṇita* (1356 CE). Modern textbooks sometimes call it the *Siamese method* or *de la Loubère method* — named for a European traveller who reported it from Siam in 1687. Nārāyaṇa described it 300+ years earlier.

## Homework

- Construct three 5×5 magic squares using the stair-step method. The magic constant should be 65 for all three. Yes — they will all be the same square. We'll discuss why tomorrow.

## Differentiation

- **One tier up:** Try the method starting at the *bottom-middle* with the number 1 going *down-right* instead of up-right. Does it still produce a magic square? (Yes — a rotated version. Symmetry strikes again.)
- **One tier down:** Re-do the 3×3 construction with the rule sheet open in front of you. Speed comes later.

## Teacher notes

- The most common student error is step 5 — when blocked, students go in random directions instead of "directly below." Drill this. Repeat: "blocked → directly below."
- A second common error: students try to apply this method to a 4×4 square. Remind them this is **odd-order only**. The 4×4 needs a different method (Day 6).
- When students wrap (step 3 or 4), they often "lose" themselves on the grid. A useful trick: imagine the grid tiled — the cell at (off-top, column *c*) is the same as (bottom row, column *c*).
- Walk around during the activity and correct misplacements early; mistakes compound.

## Citation(s) used in this lesson

- Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE — primary source for the *turagagati* method we are using.
- Plofker (2009), *Mathematics in India* — secondary scholarly context.
