# Day 8 — General Subtraction with Complements

**Module:** Nikhilam Subtraction · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will subtract a number from any larger number (not necessarily a power of ten) using a *combined* method: take the complement of the subtrahend to a nearby base, add it to the minuend, and adjust by the difference.

## Materials

- Whiteboard
- `activities/activity-02-shopkeeper.md` worksheet
- Pretend currency (paper notes of 100, 500, 1000 rupee denominations)
- Stopwatches

## Lesson flow

### Warm-up (5 min)

- Sūtra chant.
- Quick fire: 4 complements (mix of bases).

### Core (15 min) — Beyond clean bases

1. **The setup.** *"So far we've done `1000 − 567`. Easy: complement of 567 is the answer, 433. Now: `8243 − 567`. The minuend isn't a clean power of ten. What do we do?"*

2. **Idea: borrow a base.** Rewrite:

   ```
   8243 − 567
   = 8243 − 1000 + (1000 − 567)
   = 7243 + 433
   = 7676.
   ```

   *"We pick a base that's larger than the subtrahend (1000 > 567 here). We subtract that base from the minuend (8243 − 1000 = 7243; easy). Then we add the complement (433). Done."*

   Verify: 8243 − 567 = 7676 by standard borrowing. ✓

3. **Why does this work?** Algebra:
   ```
   M − S = M − (B − (B − S)) = M − B + complement(S to B)
   ```
   *"`B − S` is the complement of S to base B. Add the complement and subtract B from M."*

4. **Worked examples (class participates):**

   | Problem | Base B | Complement | M − B | Add | Answer |
   |---------|--------|-----------|-------|-----|--------|
   | 8243 − 567 | 1000 | 433 | 7243 | 7243 + 433 | **7676** |
   | 5172 − 89 | 100 | 11 | 5072 | 5072 + 11 | **5083** |
   | 6300 − 248 | 1000 | 752 | 5300 | 5300 + 752 | **6052** |
   | 12 000 − 4 567 | 10 000 | 5 433 | 2 000 | 2 000 + 5 433 | **7 433** |

5. **When is this faster than standard borrowing?** *"When the subtrahend is close to a base — say 567 to 1000 — Nikhilam-with-adjustment is genuinely faster. When the subtrahend is in the middle (like 4567 from 8243, where 4567 is not close to any clean base), standard borrowing is competitive. The mature mental-arithmetic move is to know both and pick."*

### Activity (20 min) — Shopkeeper role-play

See `activities/activity-02-shopkeeper.md`.

- In pairs, one is the shopkeeper, one is the customer.
- Customer hands over a "round" note (100, 500, 1000, or 2000 rupees).
- Shopkeeper computes the change using Nikhilam (mental).
- Swap roles every 3 rounds.
- 10 scenarios per pair. Times recorded.

### Wrap-up (5 min)

- Quick discussion: *"Where in real life does this method save time?"* Most answers will be shop-related. Affirm and add: change-counting, expense splitting, deficit tracking.
- Preview Day 9: *"Tomorrow — speed test, both methods, head-to-head."*

## Student-facing content

> **General Subtraction with Complements**
>
> To compute `M − S`:
>
> 1. Pick a base `B` such that `B > S` and `B` is a power of 10 (so 100, 1000, 10 000, ...).
> 2. Compute the complement of S to B (using Nikhilam) — call it C.
> 3. Compute `M − B` (which is easy, since B is a round number).
> 4. Answer = `(M − B) + C`.
>
> Algebraic identity:
> **M − S = (M − B) + (B − S)**
>
> Verify by checking: `M − S` should equal your answer.
>
> Example: 8243 − 567 = (8243 − 1000) + 433 = 7243 + 433 = **7676**.

## Homework

- Solve 6 mixed subtractions using the combined method:
  - 7234 − 587 (base 1000)
  - 9 612 − 3 458 (base 10 000)
  - 5 100 − 67 (base 100)
  - 13 405 − 2 850 (base 10 000)
  - 800 − 39 (base 100)
  - 25 000 − 4 999 (base 10 000)
- For each, show the base, the complement, and the final answer.

## Differentiation

- **Tier up:** What if the subtrahend has *more* digits than the base needs? E.g. `8243 − 5567` — using base 10 000, complement of 5567 is 4433, and `8243 − 10 000 = −1757`, so answer = `−1757 + 4433 = 2676`. Verify: 8243 − 5567 = 2676. ✓. Negative intermediate results are fine.
- **Tier down:** Use base 100 for everything. Only graduate to 1000 when comfortable.

## Teacher notes

- The combined method introduces a real subtlety: students must now choose a base. Some over-pick (use 10 000 for `5172 − 89` when 100 would do). Some under-pick (use 100 for `8243 − 567`). Either causes errors. Teach: "pick the smallest base that still exceeds the subtrahend."
- The shopkeeper role-play tends to make this concrete. Make sure the "round notes" are physically present — the mental model "I have 1000 in my hand, I need to give 567 of it" makes the algebra intuitive.
- Some classes will benefit from spending the whole lesson on the shopkeeper drill and pushing the algebra to Day 9. That's a fine reordering.

## Citation(s) used in this lesson

- Tirthaji, *Vedic Mathematics* (1965), sūtra Nikhilam (#2) — primary source.
- *FUNDAMENTAL AND VEDIC MATHEMATICS .pdf*, Nikhilam chapter — provided the general-case worked examples that informed today's table.
