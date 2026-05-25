# Day 4 — Subtracting from a Power of Ten

**Module:** Nikhilam Subtraction · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will compute subtractions of the form `10ⁿ − A` (e.g. 1000 − 567, 10 000 − 4783) directly by reading off the complement of A, with no written borrow.

## Materials

- Whiteboard
- `activities/activity-01-complement-drill.md` worksheet (printed)
- Stopwatches (one per pair)

## Vocabulary

(All terms reused from Days 1–3.)

## Lesson flow

### Warm-up (5 min)

- Sūtra chant.
- Quick fire: complements to 100, then complements to 1000. Teacher calls; students chorus.

### Core (10 min) — The shift from "complement" to "subtraction"

1. **The pivot.** Write on the board:

   ```
        1000  −  567  =  ?
   ```

   *"We've spent two days finding the complement. The complement of 567 to 1000 is 433. Notice that's also the answer."*

2. **Why?** *"If A + B = 1000, then 1000 − A = B and 1000 − B = A. Complement IS the difference, when you're subtracting from the base."*

3. **Worked examples, with class predicting:**

   | Problem | Working | Answer |
   |---------|---------|--------|
   | 1000 − 567 | 9-5, 9-6, 10-7 = 4, 3, 3 | **433** |
   | 1000 − 248 | 9-2, 9-4, 10-8 = 7, 5, 2 | **752** |
   | 10 000 − 4567 | 9-4, 9-5, 9-6, 10-7 = 5, 4, 3, 3 | **5433** |
   | 10 000 − 89 | 9-0, 9-0, 9-8, 10-9 = 9, 9, 1, 1 | **9911** (pad 89 → 0089) |
   | 100 000 − 23 456 | 9-2, 9-3, 9-4, 9-5, 10-6 = 7, 6, 5, 4, 4 | **76 544** |

4. **The padding rule.** *"If A has fewer digits than the base 10ⁿ, pad A with leading zeros. 89 in `10000 − 89` becomes `0089`. The Nikhilam rule needs as many digits as the base has zeros."*

### Activity (20 min) — Complement Drill (timed pairs)

See `activities/activity-01-complement-drill.md`.

- 8 problems on a sheet. Mixed bases: 4 are `1000 − X`, 3 are `10 000 − X`, 1 is `100 000 − X`.
- Pair self-correction. Time the pair.

### Wrap-up (10 min)

- Compare with standard borrowing: pick one problem (say `10 000 − 4567`) and ask half the class to solve by borrowing, half by Nikhilam. Same time limit. See who finishes first.
- Discussion: *"When does Nikhilam beat standard borrowing? When does standard borrowing match it?"* (Answer: Nikhilam dominates when subtracting from a round base; matches roughly when subtracting from a non-round number — that's the Day 8 topic.)
- Preview Day 5: *"Tomorrow — mid-module retest of the Day 1 baseline. Same problem. Different speed."*

## Student-facing content

> **Subtracting from a Power of Ten**
>
> To compute `10ⁿ − A`:
>
> 1. Make sure A has exactly n digits (pad with leading zeros if needed).
> 2. Apply the Nikhilam rule digit-by-digit: each digit "from 9," last digit "from 10."
> 3. Read off the answer.
>
> No borrowing required. Verify by adding: original + answer = base.
>
> > Tirthaji's sūtra (1965): *Nikhilaṁ Navataścaramaṁ Daśataḥ.* Six words; an entire subtraction shortcut.

## Homework

- 12 problems on the back of today's worksheet. Time yourself. Try to finish all 12 in under 4 minutes.
- One reflection sentence: *"How did the Nikhilam method feel today compared to Day 1?"*

## Differentiation

- **Tier up:** Mixed-base problems where the base is given symbolically. E.g. let B = 10⁶ = 1 000 000; compute B − 234 567.
- **Tier down:** Stick to `1000 − A` for the homework. Step up to 10 000 only when the 1000 case is automatic.

## Teacher notes

- This is the day students go "ohh — that's why we learned the complement." Make the connection explicit. The complement IS the answer when subtracting from the base.
- A student will inevitably ask: *"What if the problem is `9999 − 567`? Does it still work?"* Answer: yes, but without the "last from 10" — the answer is `9999 − 567`, computed digit-wise as 9-5, 9-6, 9-7 = 432. Try it: 567 + 432 = 999. ✓. So `9999 − 567 = 9432`. This is the special case where ALL digits are "from 9" (because there's no "+1" needed when the base is `10ⁿ − 1`). Good for Tier-up.
- Avoid letting students treat the method as a black box. Insist they verify at least one of their answers by adding.

## Citation(s) used in this lesson

- Tirthaji, *Vedic Mathematics* (1965), sūtra Nikhilam (#2).
- *FUNDAMENTAL AND VEDIC MATHEMATICS .pdf*, Nikhilam chapter — provided the 5-digit example pattern.
