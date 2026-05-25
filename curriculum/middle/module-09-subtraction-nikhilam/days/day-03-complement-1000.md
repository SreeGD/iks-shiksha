# Day 3 — Complement to 1000

**Module:** Nikhilam Subtraction · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will find the complement of any 3-digit number to 1000 in under 4 seconds, and will recognise the same pattern extends to 10 000, 100 000, and beyond.

## Materials

- Whiteboard
- Pair-drill sheets (20 three-digit numbers; second set with mixed 3- and 4-digit)
- Stopwatch
- Calculator (for self-verification only)

## Vocabulary

- *pūraka* — complement (introduced Day 2; reuse)

## Lesson flow

### Warm-up (5 min)

- Sūtra chant 3 times.
- Quick fire: teacher calls 2-digit numbers; students chorus the complement to 100.
  - 73 → 27, 41 → 59, 28 → 72, 86 → 14, 95 → 05, 60 → 40, 17 → 83.

### Core (15 min) — Three digits, same rule

1. **Pose:** *"What's the complement of 738 to 1000?"*
2. Walk through:
   ```
       1000
   −    738
   ————————
   ```
   - First digit (7): 9 − 7 = **2**
   - Second digit (3): 9 − 3 = **6**
   - Last digit (8): 10 − 8 = **2**
   - Answer: **262**.
   - Verify: 738 + 262 = 1000. ✓

3. *"Notice — same six-word rule. We just have one more 'from 9' step in the middle."*

4. **The general pattern:**

   For an n-digit number, the complement to `10ⁿ` is:
   ```
   (9 − d₁), (9 − d₂), …, (9 − dₙ₋₁), (10 − dₙ)
   ```
   where d₁ … dₙ are the digits left-to-right.

5. **Demo 4 more, with class chanting along:**

   | Number | Working | Complement | Check |
   |--------|---------|------------|-------|
   | 419 | 9-4, 9-1, 10-9 = 5, 8, 1 | **581** | 419 + 581 = 1000 ✓ |
   | 256 | 9-2, 9-5, 10-6 = 7, 4, 4 | **744** | 256 + 744 = 1000 ✓ |
   | 803 | 9-8, 9-0, 10-3 = 1, 9, 7 | **197** | 803 + 197 = 1000 ✓ |
   | 999 | 9-9, 9-9, 10-9 = 0, 0, 1 | **001** = 1 | 999 + 1 = 1000 ✓ |

6. **Quick extension to 10 000:** Complement of `2347` to 10 000?
   - 9-2, 9-3, 9-4, 10-7 = **7653**.
   - 2347 + 7653 = 10 000. ✓
   - *"Same rule. Just more digits."*

### Activity (15 min) — Speed drill

- Pair-drill: 20 three-digit numbers. Aim for all 20 in under 90 seconds.
- Self-check using a calculator: number + your complement should equal 1000.
- Second sheet: 10 four-digit numbers, complement to 10 000. Aim under 60 seconds for the set.

### Wrap-up + Formative quiz (10 min)

- Formative quiz Part A from `quizzes/formative.md` — 5 questions on slips of paper, 5 min.
- Collect. Next class includes the result.

## Student-facing content

> **Complement to 1000 (and beyond)**
>
> For any 3-digit number ABC:
> - First digit: **9 − A**
> - Second digit: **9 − B**
> - Last digit: **10 − C**
>
> Same six-word rule. Same approach for 4-digit numbers (one extra "from 9") and 5-digit numbers (two extra "from 9"s).
>
> Examples:
> - 738 → 262
> - 419 → 581
> - 2347 → 7653 (complement to 10 000)
>
> > "Nikhilaṁ navataścaramaṁ daśataḥ — *all from nine and the last from ten*." (Tirthaji, *Vedic Mathematics*, 1965, sūtra #2.) The "all" handles every digit except the last; "the last from ten" handles the last digit's special role.

## Homework

- Find the complement of each of these to 1000:
  - 156, 423, 789, 802, 64 (treat as 064), 7 (treat as 007), 555, 900.
- Find the complement of each of these to 10 000:
  - 3456, 1027, 8888, 75 (treat as 0075), 999.
- Time yourself. Total time goal: under 2 minutes.

## Differentiation

- **Tier up:** Complement of 5-digit numbers to 100 000. Time goal: under 6 sec each.
- **Tier down:** Stay on 3-digit complements. The four-digit and five-digit cases come naturally once 3-digit is automatic.

## Teacher notes

- The most common error: a number like 64 has only two digits; students forget the rule wants a 3-digit number, so they apply the rule to "64" (giving 36) instead of "064" (giving 936). Make sure they "pad with zeros" mentally.
- Another common error: the last digit being 0. For 800 → complement to 1000: digit-wise gives 9-8, 9-0, 10-0 = 1, 9, 10. The "10" carries. Easier reading: 800 + 200 = 1000, so complement is 200. The rule still works (1, 9, 10 → 1, 10, 0 → 200), but it's a place where the padding/carry interacts. Use this as a teachable moment; preview Day 6's algebraic justification.
- Some students will sniff out a shortcut: "the complement just makes everything add to 9 except the last column which adds to 10." Great — that *is* the rule, restated. Praise.

## Citation(s) used in this lesson

- Tirthaji, *Vedic Mathematics* (1965), sūtra Nikhilam (#2).
- *FUNDAMENTAL AND VEDIC MATHEMATICS .pdf*, Nikhilam chapter — worked 3-digit and 4-digit examples.
