# Day 6 — Near 1000: Padding the Right Part to 3 Digits

**Module:** Nikhilam Multiplication · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will solve 3-digit × 3-digit multiplications where both factors are within ~15 of 1000, correctly padding the right part to 3 digits.

## Materials

- Whiteboard.
- Drill sheet (8 problems near 1000).
- Reference card: "deficits from 1000" (a few worked: 998 → 2, 991 → 9, 988 → 12, 1003 → +3, etc.).

## Lesson flow

### Warm-up (5 min)

- Mixed sign-and-magnitude round: teacher says a number, class says deficit (if below 1000) or excess (if above).
- 1003 → +3. 998 → −2. 991 → −9. 1012 → +12. 988 → −12.

### Core (15 min) — Same rule, bigger pad

1. **The rule is unchanged.** Set up the vertical line, find deficits/excesses, cross-subtract or cross-add, multiply the deficits/excesses.

2. **The ONE change: pad the right part to 3 digits.** Base 1000 has 3 zeros. The right part must be exactly 3 digits.

3. **Walk through `998 × 997`:**
   - Deficits from 1000: 2, 3.
   - LEFT: 998 − 3 = **995**. (Or 997 − 2 = 995. ✓)
   - RIGHT: 2 × 3 = `6`. Pad to **3 digits**: `006`.
   - Answer: **995006**. ✓ (Calculator: 998 × 997 = 995006.)

4. **Walk through `1003 × 1004`:**
   - Excesses: +3, +4.
   - LEFT: 1003 + 4 = **1007**.
   - RIGHT: 3 × 4 = `12`. Pad to 3 digits: `012`.
   - Answer: **1007012**. ✓

5. **The overflow case: `988 × 985`:**
   - Deficits: 12, 15.
   - LEFT: 988 − 15 = **973**. (Or 985 − 12 = 973. ✓)
   - RIGHT: 12 × 15 = **180**. Pad to 3 digits: `180` (already 3 digits, no overflow).
   - Answer: **973180**. ✓

6. **The harder overflow: `985 × 978`:**
   - Deficits: 15, 22.
   - LEFT: 985 − 22 = **963**. (Or 978 − 15 = 963. ✓)
   - RIGHT: 15 × 22 = **330**. Already 3 digits.
   - Answer: **963330**.
   - Verify: 985 × 978 = 963330. ✓

7. **The hard overflow: `970 × 965`:**
   - Deficits: 30, 35.
   - LEFT: 970 − 35 = **935**.
   - RIGHT: 30 × 35 = **1050**. That's 4 digits — overflow! Carry the leading 1: left = 935 + 1 = **936**; right = `050`.
   - Answer: **936050**. ✓

8. **Mixed-sign case near 1000:** `1002 × 998`:
   - Excess +2, deficit −2.
   - LEFT: 1000 (either cross).
   - RIGHT: +2 × −2 = −4.
   - Answer: 1000 × 1000 − 4 = **999996**. ✓

### Activity (20 min) — Drill

Drill sheet:

```
1.  998 × 997        2.  996 × 995        3.  999 × 998
4.  988 × 985        5.  1003 × 1004      6.  1005 × 1002
7.  1002 × 998       8.  970 × 965
```

- 10 min individual silent.
- 10 min paired check + redo errors.

Answer key (teacher):
| Q | Sign | Deficits/excesses | Left | Right (padded) | Answer |
|---|------|---|---|---|---|
| 1 | below | 2, 3 | 995 | 006 | 995006 |
| 2 | below | 4, 5 | 991 | 020 | 991020 |
| 3 | below | 1, 2 | 997 | 002 | 997002 |
| 4 | below | 12, 15 | 973 | 180 | 973180 |
| 5 | above | 3, 4 | 1007 | 012 | 1007012 |
| 6 | above | 5, 2 | 1007 | 010 | 1007010 |
| 7 | mixed | +2, −2 | 1000 | −4 | 999996 |
| 8 | below | 30, 35 | 935+1=936 | 050 | 936050 |

### Wrap-up (5 min)

- **Formative quiz Part C (3 min)** — see `quizzes/formative.md`.
- Preview Day 7: *"Tomorrow we prove why this works. One line of algebra."*

## Student-facing content

> **Near 1000 — 3-digit pad**
>
> The rule is unchanged. The **only** change: pad the right part to **3 digits** (because base 1000 has 3 zeros).
>
> **Examples:**
> - 998 × 997 → 995 | **006** → **995006**
> - 1003 × 1004 → 1007 | **012** → **1007012**
> - 970 × 965 → 935+1=936 | **050** → **936050** (right part overflowed)
> - 1002 × 998 → 1000 | −4 → **999996** (mixed)
>
> **General rule:** the right-part pad-width equals the number of zeros in the base.

## Homework

- 8 problems on the back of today's worksheet, mixed near-1000.
- Compute one of them with long multiplication. How much longer did long take?

## Differentiation

- **Tier up:** Try `9998 × 9997` (base 10000). Right part pad = 4 digits. Confirm answer: 99950006.
- **Tier down:** Stay with the easy near-1000 problems (998 × 997, 999 × 998). Build up.

## Teacher notes

- The padding rule is the only new thing today. If students have Day 3 fluent, this lesson is mostly drill.
- Forgetting to pad is the most common error. A student who writes `998 × 997 = 9956` instead of 995006 has forgotten to pad to 3 digits. The diagnostic: their answer has the wrong number of digits.
- The "general rule" (pad-width = number of zeros in base) is a real generalisation worth boxing on the board. It sets up Day 7's algebra.

## Citation(s) used in this lesson

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA) — Nikhilam multiplication, base-1000 examples.
