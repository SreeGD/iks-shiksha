# Day 6 — *Anurūpyeṇa*: Extending to ×12, ×13, …, ×19

**Module:** ×11 (*Ekādhikena Pūrveṇa*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will apply Tirthaji's *Anurūpyeṇa* sub-sūtra ("proportionally") to multiply any 2-digit number by 12, 13, …, 19, with at least 80% accuracy on a mixed worksheet.

## Materials

- Whiteboard.
- `activities/activity-02-anurupyena.md` worksheet.
- Stopwatch.

## Vocabulary introduced today

- *Anurūpyeṇa* (IAST: anurūpyeṇa; lit. "proportionally") — a sub-sūtra in Tirthaji's corpus. We use it as the name for the proportional scaling that extends the ×11 pattern to ×12, ×13, …, ×19.

## Lesson flow

### Warm-up (5 min)

- Recall: state the ×11 trick in one sentence.
- *"Outer digits unchanged; middle is the digit sum."*

### Core (18 min) — The scaling pattern

1. **Question.** *"What does ×12 look like? Try 23 × 12 by long multiplication first."*

   ```
   23 × 12 = 23 × 10 + 23 × 2 = 230 + 46 = 276.
   ```

2. **Derive.** *"Now distribute (10a + b) × 12 = (10a + b)(10 + 2):*
   ```
   = 100a + 10b + 20a + 2b
   = 100a + 10(b + 2a) + 2b
   ```

   Hmm — that's awkward. *2b* in the units, *(b + 2a)* in the tens. Let's organise it more cleanly.

3. **The Tirthaji pattern.** For *N* in {11, 12, …, 19}, write *N* = 10 + *k* where *k* ∈ {1, 2, …, 9}. Then:

   ```
   (10a + b) × (10 + k)
       = 100a + 10b·k + 10ka + bk
                Wait — let's redo carefully:
       = (10a + b) × 10 + (10a + b) × k
       = 100a + 10b + 10ak + bk
       = 100a + 10(b + ak) + bk
   ```

   Hmm — *bk* could be 2 digits. The pattern is: **scale each digit by k as you slide along.**

   *Easier form for students*: For ×*N* = ×(10 + *k*):
   - Start with the leftmost digit.
   - Multiply it by *k*, add the next digit, write the units of that sum (carry as needed).
   - Continue right.
   - The rightmost step: multiply the last digit by *k*.

   This is the **Tirthaji form of the *Anurūpyeṇa* extension**.

4. **Worked example: 23 × 13. (k = 3.)**

   ```
   Set up: 0  2  3  (pad with 0 on left to track the carry-out)
   Right to left:
     - Units: last digit × k = 3 × 3 = 9. Write 9.
     - Tens: middle digit × k + next-right digit = 2 × 3 + 3 = 9. Write 9.
     - Hundreds: leftmost digit × k + next-right = 0 × 3 + 2 = 2. Wait — we want the LEFTMOST as just itself with the carry...
   ```

   *(Pause — this is getting confusing. Let's use a different presentation.)*

5. **Cleaner presentation for ×12 to ×19.**

   For *N* × 12 of a 2-digit number *ab*: simply use long multiplication mentally, but in the order:
   - units of answer = *b* × 2 (carry if ≥ 10)
   - tens of answer = *a* × 2 + *b* (plus carry; carry if ≥ 10)
   - hundreds of answer = *a* (plus carry)

   For *N* × 13: replace ×2 with ×3 everywhere.

   General: **For ×(10 + k), multiply each digit by k and add the digit to its right (the "running scan").**

6. **Examples** (boxed):

   ```
   23 × 12:
     units: 3·2 = 6
     tens: 2·2 + 3 = 7
     hundreds: 2 (no carry)
     → 276 ✓

   23 × 13:
     units: 3·3 = 9
     tens: 2·3 + 3 = 9
     hundreds: 2
     → 299 ✓

   45 × 13:
     units: 5·3 = 15 → write 5, carry 1
     tens: 4·3 + 5 + 1 = 18 → write 8, carry 1
     hundreds: 4 + 1 = 5
     → 585 ✓
   ```

   Check 45 × 13: 45 × 10 + 45 × 3 = 450 + 135 = **585**. ✓

7. **The name.** *"Tirthaji (1965) calls this proportional scaling **Anurūpyeṇa** — 'proportionally.' The ×11 case is the special case k = 1, where the scaling is trivial."*

### Activity (15 min) — Mixed drill

See `activities/activity-02-anurupyena.md`.

- 16 problems across ×12, ×13, ×14, ×17, ×19.
- Paired self-check.

### Wrap-up (2 min)

- *"How does ×11 fit into the ×12–×19 family?"* (It's the k=1 special case.)
- Preview Day 7: *"What about ×23? ×47? When does the trick stop helping?"*

## Student-facing content

> **The ×12 to ×19 family — *Anurūpyeṇa***
>
> For any *N* = 10 + *k* (where *k* is 1 to 9), multiply a 2-digit number *ab* × *N* by:
> 1. Units = *b* × *k* (carry if ≥ 10).
> 2. Tens = *a* × *k* + *b* (plus any carry; carry if ≥ 10).
> 3. Hundreds = *a* (plus any carry).
>
> When *k* = 1 (i.e. ×11), this is the original "split and add" trick.
>
> Tirthaji (1965) names this scaling pattern ***Anurūpyeṇa*** — "proportionally."

## Homework

- 12 problems mixing ×12, ×13, ×14: see worksheet attached. Self-check with long multiplication on any 4.

## Differentiation

- **Tier up:** Try 3-digit × 13 problems. Use the right-to-left running-scan from Day 4 with the *k*-scaling from today.
- **Tier down:** Focus only on ×12 today. Build fluency before adding higher *k*.

## Teacher notes

- *Anurūpyeṇa* is the pattern-naming step. Some students will object: *"This is just long multiplication done right-to-left."* They are correct. Honour the observation; reframe: *"The win is doing it MENTALLY in one pass, with a clear rhythm."*
- The procedural complexity grows quickly with *k*. ×17 and ×19 are harder than ×11 by a real margin. Calibrate the problem set accordingly.
- This day is genuinely harder than Days 1–5. If the class is shaky, slow down — skip the harder *k* values and revisit on Day 9.

## Citation(s) used in this lesson

- Tirthaji (1965), sub-sūtra *Anurūpyeṇa*.
- *Microsoft Word - sutras1.pdf* — for the sub-sūtra list.
