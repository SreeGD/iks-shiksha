# Day 5 — A 5×5 Magic Square

**Module:** Magic Squares (*Bhadragaṇita*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will independently construct a 5×5 magic square using the *turagagati* method and verify its magic constant of 65.

## Materials

- Printed blank 5×5 grids (3 per student)
- The 5-step rule handout from Day 4
- Stopwatch (for timed second-construction)

## Vocabulary review

- *turagagati* — stair-step method (introduced Day 4).
- *magic constant* for 5×5 → **65** (from Day 2).

## Lesson flow

### Warm-up (5 min)

- Class recall: 5-step rule, recited together.
- Magic-constant check: *"For a 5×5 with numbers 1–25, the magic constant is ____?"* (65.)
- Pre-class question: did everyone produce the *same* 5×5 last night? Most will say yes.

### Core (20 min)

1. **Build a 5×5 together on the board.** Narrate every step. Take 8–10 minutes — go cell-by-cell.

   Start with 1 in row-1, column-3 (the top middle). Place 2 up-right (off the top → wraps to bottom row, column 4). Place 3 up-right from 2 (off the right → wraps to row 4, column 5)... continue.

   Expected result (the classical Nārāyaṇa 5×5):

   ```
   17 | 24 |  1 |  8 | 15
   ----------------------
   23 |  5 |  7 | 14 | 16
   ----------------------
    4 |  6 | 13 | 20 | 22
   ----------------------
   10 | 12 | 19 | 21 |  3
   ----------------------
   11 | 18 | 25 |  2 |  9
   ```

2. **Verify together.** Pick:
   - One row → 17 + 24 + 1 + 8 + 15 = 65 ✓
   - One column → 17 + 23 + 4 + 10 + 11 = 65 ✓
   - The main diagonal → 17 + 5 + 13 + 21 + 9 = 65 ✓
   - The anti-diagonal → 15 + 14 + 13 + 12 + 11 = 65 ✓

3. **Notice the structure.** Take 3 minutes to observe:
   - 13 (the middle number) is in the centre — consistent with the *n*²/2 + 1 = 13 rule for odd-order.
   - Numbers 1–9 occupy a "broken diagonal" pattern; 16–25 occupy the complementary pattern.
   - The same algorithm that gave us the 3×3 gave us this. The rule does not change with size.

### Activity (15 min) — Formative quiz Part B + speed construction

- **First 10 min:** Hand out `quizzes/formative.md` Part B. Students complete individually.
- **Last 5 min:** Each student starts a fresh 5×5 grid. On "Go," they construct a magic square from scratch as fast as they can. Self-time. Verify one row before stopping the watch.

### Wrap-up (5 min)

- Show of hands: who finished in under 4 minutes? Under 6? Under 8?
- *"Yesterday's home practice was the same 5×5. Tomorrow we look at a different beast — the 4×4."*
- Preview Day 6: Khajuraho and the 4×4.

## Student-facing content

> **The 5×5 magic square — classical Nārāyaṇa form**
>
> Magic constant: 65 (from *S = n(n² + 1)/2* with *n* = 5).
>
> ```
> 17 | 24 |  1 |  8 | 15
> ----------------------
> 23 |  5 |  7 | 14 | 16
> ----------------------
>  4 |  6 | 13 | 20 | 22
> ----------------------
> 10 | 12 | 19 | 21 |  3
> ----------------------
> 11 | 18 | 25 |  2 |  9
> ```
>
> Built using the *turagagati* method, exactly as for the 3×3 — the rule does not change with size, as long as *n* is odd.

## Homework

- Construct a 7×7 magic square using the stair-step method. The magic constant should be 175. Yes, it takes time — work patiently. Bring it tomorrow for spot-checks.

## Differentiation

- **One tier up:** Construct a 9×9 magic square. Constant = 369. Time it.
- **One tier down:** Construct another 5×5, slowly, with the rule sheet visible. Speed is not the goal yet.

## Teacher notes

- For the live demonstration, use a slow pace and check student-following frequently — "where would 2 go?" "is that cell filled?"
- Students may resist because "I already built one at home." Push them to *re-build* it on the board — narrating the rule reinforces it.
- A few students will produce mirror-image squares because they reversed the up-right direction. Show that mirror images are also valid magic squares (by symmetry from Day 3) — but consistency matters when you're describing the algorithm.

## Citation(s) used in this lesson

- Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE — the 5×5 example is one of the worked examples in the original text.
