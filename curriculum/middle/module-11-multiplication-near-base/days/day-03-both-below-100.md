# Day 3 — Both Numbers Below 100

**Module:** Nikhilam Multiplication · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will solve any 2-digit × 2-digit multiplication where both factors are between 90 and 99 using the Nikhilam method, in under 10 seconds.

## Materials

- Whiteboard with the vertical-line template.
- Class wall-poster: "Deficits from 100" — small reference card (e.g. 97 → 3, 88 → 12).
- Pre-printed drill sheet (10 problems).
- Stopwatch per pair.

## Lesson flow

### Warm-up (5 min)

- **Complement-to-100 lightning round.** Teacher calls 2-digit numbers in the 80s and 90s; class chants the deficit. (97 → 3. 88 → 12. 96 → 4. 92 → 8. 99 → 1. 85 → 15. ...)
- Repeat. By the end most students should be doing this in under a second.

### Core (15 min) — The 2-digit × 2-digit case, both below 100

1. **The template** (vertical line, base = 100):

   ```
        97 │ −3       ← deficit from 100
      × 96 │ −4
     ─────┼──────
        ? │  ?
   ```

2. **Walk through `97 × 96`** (from Day 1, now formalised):
   - LEFT: 97 − 4 = **93**.
   - RIGHT: 3 × 4 = **12**.
   - **Pad to 2 digits** (base 100 has 2 zeros): RIGHT = `12` (already 2 digits, no pad needed).
   - Answer: **9312**.

3. **Walk through `98 × 99`:**
   - Deficits: 2, 1.
   - LEFT: 98 − 1 = **97**.
   - RIGHT: 2 × 1 = `2` → pad to 2 digits → `02`.
   - Answer: **9702**.

4. **The padding rule (write on board, boxed):**

   > **Pad the right part to as many digits as there are zeros in the base.**
   > Base 10 → 1 digit on the right.
   > Base 100 → 2 digits on the right.
   > Base 1000 → 3 digits on the right.

5. **The overflow / carry case: `88 × 89`.**
   - Deficits: 12, 11.
   - LEFT: 88 − 11 = **77**. (Or 89 − 12 = 77. ✓)
   - RIGHT: 12 × 11 = **132**.
   - But the right part should be only 2 digits (base 100). 132 has 3 digits — the leading `1` overflows.
   - **Carry the overflow into the left:** left = 77 + 1 = **78**; right = `32`.
   - Answer: **7832**. ✓ (Calculator check: 88 × 89 = 7832.)

6. **The "use either cross" check.** For `97 × 96`:
   - Either `97 − 4 = 93` or `96 − 3 = 93`.
   - If you get *different* numbers, you've made an error. This is your built-in error-detector.

### Activity (20 min) — Drill

Pair drill, then individual silent drill.

Drill sheet (10 problems, mixed difficulty):

```
1.  97 × 96       2.  98 × 99       3.  95 × 94       4.  93 × 91
5.  99 × 98       6.  92 × 95       7.  88 × 89       8.  87 × 92
9.  96 × 96       10. 91 × 87
```

- **5 min individual:** solve all 10 silently. No talking.
- **5 min paired check:** swap sheets. Partner reads problem 1; the other resolves it on a fresh strip; compare. Continue.
- **10 min mixed work:** problems with both-below-100, individual silent.

Answer key (teacher):
| Q | Deficits | Left | Right | Answer |
|---|----------|------|-------|--------|
| 1 | 3, 4 | 93 | 12 | 9312 |
| 2 | 2, 1 | 97 | 02 | 9702 |
| 3 | 5, 6 | 89 | 30 | 8930 |
| 4 | 7, 9 | 84 | 63 | 8463 |
| 5 | 1, 2 | 97 | 02 | 9702 |
| 6 | 8, 5 | 87 | 40 | 8740 |
| 7 | 12, 11 | 77+1=78 | 32 | 7832 |
| 8 | 13, 8 | 87−13=79 or 92−8=84... | (see note) | 8004 |
| 9 | 4, 4 | 92 | 16 | 9216 |
| 10 | 9, 13 | 91−13=78 or 87−9=78 | 117 → carry 1 → 79, right 17 | 7917 |

*(Note Q8: 87 − 8 = 79, OR 92 − 13 = 79. Right = 13 × 8 = 104. Carry 1 → 80; right = 04. Answer: 8004.)*

### Wrap-up (5 min)

- **Formative quiz on a slip of paper (5 questions, 3 min)** — see `quizzes/formative.md` Part A.
- Collect for grading. Hand back tomorrow.

## Student-facing content

> **Both numbers below 100**
>
> | Step | What you do |
> |---|---|
> | 1 | Find each number's **deficit from 100**. |
> | 2 | **Cross-subtract** for the LEFT part. |
> | 3 | **Multiply** the two deficits for the RIGHT part. |
> | 4 | **Pad the RIGHT part to 2 digits.** |
> | 5 | If the RIGHT part overflows (≥ 100), **carry** the overflow into the LEFT. |
>
> **Examples:**
> - 97 × 96 → 93 | 12 → **9312**
> - 98 × 99 → 97 | 02 → **9702**
> - 88 × 89 → 77+1 | 32 → **7832** (right part overflowed)
>
> Sanskrit name: *Nikhilam Navataścaramaṁ Daśataḥ* — "all from 9 and the last from 10."

## Homework

- 10 problems on the back of today's worksheet, all 2-digit × 2-digit with both factors in 85–99.
- Time yourself. Beat the class average from today.

## Differentiation

- **Tier up:** Try `83 × 89` and `78 × 85` (further from 100). The method still works, but the deficits are larger and the right-part overflow is more common. See how far below 100 you can go before the method stops feeling fast.
- **Tier down:** Stick to factors in 90–99 for the rest of the week. We'll revisit 80s on Day 5.

## Teacher notes

- The overflow / carry is the single most common error point. Spend time on `88 × 89` and `78 × 85`. If students don't fluent on the carry by end of class, schedule 5 min of catch-up at the start of Day 4.
- The "use either cross" check is a real check — encourage students to do both crosses initially. By Day 6 they'll naturally drop the second one.
- Some students will be fast on a calculator and slow on Nikhilam. Acknowledge: *"With a calculator, calculator wins. The Nikhilam method matters when you DON'T have a calculator — exams, mental estimation, daily life."*

## Citation(s) used in this lesson

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA) — Nikhilam multiplication, base-100 examples.
