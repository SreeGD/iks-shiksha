# Day 2 — Complement to 100

**Module:** Nikhilam Subtraction · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will find the complement (*pūraka*) of any 2-digit number to 100 in under 3 seconds, using the Nikhilam rule applied to two digits.

## Materials

- Whiteboards or scrap paper for live drills
- A printed wall poster: `9, 9, 9, 9, 9, ... 10` showing the digit-wise rule visually
- Pair-drill sheets (20 two-digit numbers each)
- Stopwatch (one per pair)

## Vocabulary introduced today

- *pūraka* (IAST: pūraka; lit. "that which completes") — the **complement**: the number you add to fill up to 100, 1000, etc.

## Lesson flow

### Warm-up (5 min)

- Sūtra chant 3 times.
- Make-10 reflex: 10 quick digit-partners.

### Core (15 min) — The pattern

1. **Pose:** *"What's the complement of 73 to 100?"* Take guesses.
2. Walk through it the Nikhilam way:
   ```
        100
   −     73
   ———————
   ```
   - First digit (7): 9 − 7 = **2**
   - Last digit (3): 10 − 3 = **7**
   - Answer: **27**.
   - Verify: 73 + 27 = 100. ✓

3. **Why "all from 9, last from 10"?** Show on the board:
   ```
   99  +  1  = 100
   ```
   - If we subtract each digit *from 9* we get the complement to **99**, not 100.
   - The "+1" needed to bridge 99 → 100 is exactly what "the last from 10" provides:
     `10 − x` is the same as `(9 − x) + 1`.
   - That's the whole trick. The last digit absorbs the "+1." Every other digit just goes "from 9."

4. **Demo 4 more, quickly, with the class chanting along:**

   | Number | First digit | Last digit | Complement | Check |
   |--------|-------------|------------|------------|-------|
   | 41 | 9 − 4 = 5 | 10 − 1 = 9 | **59** | 41 + 59 = 100 ✓ |
   | 28 | 9 − 2 = 7 | 10 − 8 = 2 | **72** | 28 + 72 = 100 ✓ |
   | 86 | 9 − 8 = 1 | 10 − 6 = 4 | **14** | 86 + 14 = 100 ✓ |
   | 95 | 9 − 9 = 0 | 10 − 5 = 5 | **05** = 5 | 95 + 5 = 100 ✓ |

5. **Edge case: trailing zero.** What is the complement of 30? Apply the rule: 9 − 3 = 6 (for tens), 10 − 0 = 10 (for units). But 10 isn't a digit — it carries. So you get `6 | 10` → `70`. Easier: notice that the last *non-zero* digit gets the "from 10" treatment; trailing zeros stay as zeros.

   Or more simply: 30 + 70 = 100, so complement of 30 is 70. The rule still works, you just respect place value.

### Activity (20 min) — Paired drill

- Pairs face each other across desks. One holds the drill sheet (20 two-digit numbers); the other says complements out loud.
- Round 1: 60 seconds. Count correct answers.
- Swap roles. Round 2.
- Round 3: swap to a new sheet (different numbers). Aim to beat your Round 1 count.

### Wrap-up (5 min)

- Quick poll: who got 15+ in 60 sec? 18+? 20?
- Recall paraphrase: *"To complete to 100, take each digit from 9; the last digit takes from 10."*
- Preview Day 3: *"Tomorrow — same idea, but complement to 1000."*

## Student-facing content

> **Complement (*pūraka*) to 100**
>
> For any 2-digit number AB:
>
> - Tens digit: **9 − A**
> - Units digit: **10 − B**
>
> Examples:
> - 73 → 27 (9−7=2, 10−3=7)
> - 41 → 59 (9−4=5, 10−1=9)
> - 95 → 05 (9−9=0, 10−5=5)
>
> Verify by adding: number + complement = 100.
>
> > Tirthaji's *Vedic Mathematics* (1965) gives the rule as *Nikhilaṁ Navataścaramaṁ Daśataḥ* — and a "complement to 100" is just the rule applied to two digits.

## Homework

- Memorise complements to 100 of the multiples of 5: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95. These should become automatic.
- Time yourself: 20 random complements in under 60 seconds. Practise twice.

## Differentiation

- **Tier up:** Try complements to 200, 300, 500. The rule modifies — find complement to 100, then adjust. (Tier-up students should be able to articulate that adjustment by the end of class.)
- **Tier down:** Use the rule only when both digits of the number are non-zero. Trailing zeros will be drilled on Day 3.

## Teacher notes

- Most common error today: 9 − 0 = 9 (correct) but 10 − 0 = 10 (cannot be a digit). Students will write `0` and lose 10. Reinforce: if the last digit is 0, the complement's last digit is also 0, and the "10" gets absorbed into the next column. Or: just note that the rule cleanly handles non-zero last digits; trailing zeros are a quick edge-case.
- Many students try to do this in their head WITHOUT going digit-by-digit. That's fine if they get the right answer — but make sure they can *show* the digit-wise method when asked. Day 6's "why it works" depends on the digit-wise framing.
- Pair students with different reflexes. The faster-reflex student often models; the slower benefits.

## Citation(s) used in this lesson

- Tirthaji, *Vedic Mathematics* (1965), sūtra Nikhilam (#2) — the source of the digit-wise rule.
