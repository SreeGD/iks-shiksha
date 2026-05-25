# Day 4 — Both Numbers Above 100

**Module:** Nikhilam Multiplication · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will solve any 2-digit × 2-digit (or 3-digit) multiplication where both factors are slightly *above* 100 (101–112) using the Nikhilam method.

## Materials

- Whiteboard with the vertical-line template.
- Day 3 formative quiz returned with marks.
- Drill sheet (10 problems with both factors above 100).
- Stopwatch per pair.

## Lesson flow

### Warm-up (5 min)

- **Complement-to-100 round** (same as Day 3).
- Add the new round: **excess from 100.** Teacher says "103," class says "+3." "108" → "+8." "112" → "+12." "101" → "+1."
- Hand back yesterday's formative.

### Core (15 min) — Both above 100: use excess, cross-ADD

1. **The key change:** instead of *deficit* (negative), we now have *excess* (positive). Instead of cross-subtract, we **cross-add**.

2. **The template** (vertical line, base = 100):

   ```
       103 │ +3       ← excess from 100
     × 104 │ +4
     ─────┼──────
       ?   │  ?
   ```

3. **Walk through `103 × 104`:**
   - Excesses: +3, +4.
   - LEFT: 103 **+** 4 = **107**. (Or 104 + 3 = 107. ✓ Either cross.)
   - RIGHT: 3 × 4 = **12**. Pad to 2 digits: `12`.
   - Answer: **10712**. ✓ (Calculator check: 103 × 104 = 10712.)

4. **Walk through `108 × 107`:**
   - Excesses: +8, +7.
   - LEFT: 108 + 7 = **115**.
   - RIGHT: 8 × 7 = **56**. Pad to 2 digits: `56`.
   - Answer: **11556**. ✓

5. **The pattern:**

   | Both below | Both above |
   |---|---|
   | Cross-**subtract** | Cross-**add** |
   | Deficit × deficit | Excess × excess |
   | Right part is product of POSITIVE numbers (deficits) | Right part is product of POSITIVE numbers (excesses) |

   *In both cases* the right part is a positive product. The sign issue only appears in the *mixed* case (Day 5).

6. **The overflow case (rare here): `112 × 113`.**
   - Excesses: +12, +13.
   - LEFT: 112 + 13 = **125**.
   - RIGHT: 12 × 13 = **156**. Right part should be 2 digits; the leading 1 overflows.
   - **Carry:** left = 125 + 1 = **126**; right = `56`.
   - Answer: **12656**. ✓

### Activity (20 min) — Drill

Drill sheet (10 problems):

```
1.  103 × 104        2.  102 × 105        3.  108 × 107
4.  109 × 102        5.  101 × 106        6.  111 × 104
7.  112 × 113        8.  106 × 109        9.  103 × 103
10. 105 × 105
```

- 5 min individual silent.
- 5 min paired check.
- 10 min mixed: alternate problems from yesterday (both below) and today (both above) on the same drill sheet — call it the "mixed-base" sheet. Students need to first **decide** whether each is "both below" or "both above" before applying the right cross-operation.

Answer key (teacher):
| Q | Sign | Cross | Left | Right | Answer |
|---|------|-------|------|-------|--------|
| 1 | both above | + | 107 | 12 | 10712 |
| 2 | both above | + | 107 | 10 | 10710 |
| 3 | both above | + | 115 | 56 | 11556 |
| 4 | both above | + | 111 | 18 | 11118 |
| 5 | both above | + | 107 | 06 | 10706 |
| 6 | both above | + | 115 | 44 | 11544 |
| 7 | both above | + | 125+1=126 | 56 | 12656 |
| 8 | both above | + | 115 | 54 | 11554 |
| 9 | both above | + | 106 | 09 | 10609 |
| 10 | both above | + | 110 | 25 | 11025 |

### Wrap-up (5 min)

- **Formative quiz Part B (3 min)** — see `quizzes/formative.md`.
- Preview Day 5: *"Tomorrow — what happens when ONE number is above and ONE is below? Sign care needed."*

## Student-facing content

> **Both numbers above 100**
>
> | Step | What you do |
> |---|---|
> | 1 | Find each number's **excess** above 100 (positive number). |
> | 2 | **Cross-ADD** for the LEFT part. |
> | 3 | **Multiply** the two excesses for the RIGHT part. |
> | 4 | **Pad the RIGHT part to 2 digits.** |
> | 5 | If the RIGHT part overflows, **carry** the overflow into the LEFT. |
>
> **Examples:**
> - 103 × 104 → 107 | 12 → **10712**
> - 108 × 107 → 115 | 56 → **11556**
> - 112 × 113 → 126 | 56 → **12656** (right part overflowed)
>
> Same sūtra, mirror operation: when deficits become excesses, subtraction becomes addition.

## Homework

- 10 mixed problems (both-below AND both-above mixed). Decide first, then solve. Bring tomorrow.

## Differentiation

- **Tier up:** Try `1003 × 1004` (base 1000). The right part should be 3 digits. Confirm `1003 × 1004 = 1007012`.
- **Tier down:** Stay with `103 × 104`, `102 × 103`, `104 × 105` until comfortable.

## Teacher notes

- The "decide which sign first" step on the mixed drill sheet is the most important habit-builder of this day. Reinforce: *before* you start cross-adding or cross-subtracting, **glance at both numbers** and decide whether they're both below, both above, or split.
- A few students will try to carry into the right part from the left (instead of the other way). Walk through the place-value reasoning: a "100" overflow on the right is *one more in the next column up*, which is the left part.

## Citation(s) used in this lesson

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA) — Nikhilam multiplication, "above the base" examples.
- *Vedic_Maths.pdf* (ISKCON Desire Tree) — practice problems for above-base multiplication.
