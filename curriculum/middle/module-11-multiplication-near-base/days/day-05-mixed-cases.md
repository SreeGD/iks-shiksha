# Day 5 — Mixed Cases: One Above, One Below

**Module:** Nikhilam Multiplication · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will solve any 2-digit × 2-digit multiplication where one factor is *above* 100 and one is *below*, handling the negative right-part correctly.

## Materials

- Whiteboard.
- Drill sheet (8 mixed-sign problems).
- `activities/activity-01-mixed-signs.md` worksheet.

## Lesson flow

### Warm-up (5 min)

- Complement-to-100 round.
- Excess-from-100 round.
- Now mix: teacher says "97," class says "−3." Teacher says "103," class says "+3." This trains the sign attention.

### Core (15 min) — One above, one below

1. **Set up `102 × 98`.** Write on board:

   ```
       102 │ +2       ← excess
     ×  98 │ −2       ← deficit
     ─────┼──────
       ?   │  ?
   ```

2. **The left part — either cross still works:**
   - `102 + (−2) = 102 − 2 = 100`.
   - `98 + 2 = 100`. (Same answer ✓.)

3. **The right part — sign matters:**
   - `(+2) × (−2) = −4`.
   - The right part is **negative**!

4. **What does it mean to have a "negative" right part?**
   - Concatenating "100" and "−4" gives... `100 | −4` = `100 × 100 + (−4)` = 10000 − 4 = **9996**.
   - Check: 102 × 98 = 9996. ✓

5. **The "borrow" maneuver — cleaner mental version.** Same problem:
   - The negative right part of `−4` says: "subtract 4 from the natural concatenation 100|00 = 10000."
   - So 102 × 98 = 10000 − 4 = **9996**. Clean.

6. **Or — the "borrow from left" form:** if students prefer always-positive right parts:
   - Left = 100. Right = −4. Borrow 1 from left (which is worth 100 in the right):
   - New left = 100 − 1 = 99. New right = 100 − 4 = 96 (now positive).
   - Answer: **9996**.

7. **Worked examples in chorus:**
   - `104 × 96`: excess +4, deficit −4. Left = 100 (either cross). Right = +4 × −4 = −16. Answer: 100 × 100 − 16 = **9984**. ✓
   - `97 × 103`: deficit −3, excess +3. Left = 100. Right = −3 × +3 = −9. Answer: **9991**. ✓
   - `108 × 95`: excess +8, deficit −5. Left = 108 − 5 = 103 (or 95 + 8 = 103 ✓). Right = +8 × −5 = −40. Answer: 103 × 100 − 40 = 10300 − 40 = **10260**. ✓

8. **The pattern (write on board):**

   | Case | Cross | Right part sign |
   |---|---|---|
   | Both below | Subtract | + (deficit × deficit) |
   | Both above | Add | + (excess × excess) |
   | Mixed | Either form — still cancels | **−** (excess × deficit) |

### Activity (20 min) — `activities/activity-01-mixed-signs.md`

Brief:
- 8 problems on the activity sheet, all mixed-sign.
- 8 min individual silent.
- 7 min paired check.
- 5 min: students re-do any they got wrong, OR move to challenge problems if all correct.

### Wrap-up (5 min)

- Quick chorus check: `102 × 98`? (9996.) `104 × 96`? (9984.) `108 × 95`? (10260.)
- Preview Day 6: *"Tomorrow — base 1000. The pad becomes 3 digits."*

## Student-facing content

> **Mixed case: one above, one below**
>
> 1. Find the **excess** of the bigger number and the **deficit** of the smaller (or just signed: + for above 100, − for below).
> 2. LEFT: cross-subtract using signs. `102 + (−2) = 100`. Either cross still works.
> 3. RIGHT: multiply the two signed numbers. The RIGHT part is **negative**.
> 4. Subtract the absolute value of the right from `LEFT × 100`.
>
> **Examples:**
> - 102 × 98 → 100 | −4 → 10000 − 4 = **9996**
> - 104 × 96 → 100 | −16 → 10000 − 16 = **9984**
> - 108 × 95 → 103 | −40 → 10300 − 40 = **10260**
>
> Tip: for `(a+x)(a−y)` with a = base, the left is `a + x − y` and the right is `−xy`. Whenever excess equals deficit, the left is exactly the base and the answer is `base² − xy`.

## Homework

- 10 mixed problems (mix of both-below, both-above, and mixed-sign). Decide the case first.
- Find ONE example in your textbook where mixed-sign Nikhilam would be faster than long multiplication. Bring it.

## Differentiation

- **Tier up:** Try `121 × 79` (further from 100). Excess +21, deficit −21. Cross: 121 − 21 = 100. Right: +21 × −21 = −441. Answer: 10000 − 441 = **9559**. (Equivalently: (100+21)(100−21) = 100² − 21² = 10000 − 441.) Notice you've just used the *difference of squares* identity. Connect to algebra.
- **Tier down:** Stay with `102 × 99`, `103 × 98` (small differences). Build up the sign care before tackling larger gaps.

## Teacher notes

- The mixed case is where most students give up and revert to long multiplication. **Don't let them.** The sign care is genuinely tricky for one day; by Day 6 it'll be a non-issue.
- The "tier up" connection to difference-of-squares (a²−b² identity) is a real bridge to algebra. If a student spots it, celebrate.
- Some students will resist the negative right part. Show them the "borrow from left" form (above) as an alternative — both forms give the same answer.

## Citation(s) used in this lesson

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA) — Nikhilam multiplication, mixed-sign examples.
