# Day 3 — Why It Works

**Module:** ×11 (*Ekādhikena Pūrveṇa*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will derive the identity (10*a* + *b*) × 11 = 100*a* + 10(*a* + *b*) + *b* and explain in their own words why the ×11 trick is not a coincidence.

## Materials

- Whiteboard.
- Worksheet: "explain to a friend" prompt with space for student algebra.

## Lesson flow

### Warm-up (5 min)

- Neighbour-sum chorus: 15 quick ×11 problems, mix of carry and no-carry.
- *"By now your hands know the trick. Today your brain catches up."*

### Core (20 min) — The algebra

1. **Write any 2-digit number as 10*a* + *b*.** Make sure every student gets this.

   ```
   23 = 10·2 + 3   →  a = 2, b = 3
   87 = 10·8 + 7   →  a = 8, b = 7
   ```

2. **Distribute the multiplication by 11.** Step by step on the board, students copy:

   ```
   (10a + b) × 11
       = (10a + b) × (10 + 1)
       = (10a + b) × 10  +  (10a + b) × 1
       = 100a + 10b      +  10a + b
       = 100a + 10a + 10b + b
       = 100a + 10(a + b) + b
   ```

3. **Read the final line out loud.** *"100a + 10(a+b) + b. What does this say in plain language?"*
   - 100*a* — the **hundreds** digit is *a* (the original first digit).
   - 10(*a*+*b*) — the **tens** digit is *a* + *b* (the digit sum).
   - + *b* — the **units** digit is *b* (the original second digit).

   *"That IS the trick. The algebra spells out: first digit, sum, last digit."*

4. **Check on 23:**

   ```
   a = 2, b = 3.
   100·2 + 10·5 + 3 = 200 + 50 + 3 = 253. ✓
   ```

5. **Now the carry case** — where does the carry come from?

   ```
   a = 8, b = 7.
   100·8 + 10·15 + 7 = 800 + 150 + 7 = 957.
   ```

   *"Notice: 10 × 15 = 150 = 100 + 50. The 100 contribution slides into the hundreds column — that IS the carry. So the algebra ALSO explains why we add 1 to the leftmost digit when the sum is ≥ 10."*

### Activity (15 min) — Explain to a friend

- Worksheet prompt:

  > Imagine a Grade 4 cousin asks: *"Why does the ×11 trick work? Isn't it just magic?"* Write 5–7 sentences explaining why it's NOT magic. Use the words **distribute**, **digit sum**, and **place value**.

- 10 min individual writing.
- 5 min pair-sharing: read your paragraph to your partner; they tell you one part that's clear and one part that's unclear.

### Wrap-up (5 min)

- Read aloud one strong paragraph (with permission).
- Preview Day 4: *"Tomorrow — extend the trick to 3-digit numbers. The algebra will scale."*

## Student-facing content

> **Why the ×11 trick works**
>
> Write any 2-digit number as 10*a* + *b* — the first digit is worth 10, the second is worth 1.
>
> Distribute the multiplication by 11 = 10 + 1:
>
> (10*a* + *b*) × 11 = (10*a* + *b*) × 10 + (10*a* + *b*) × 1
> = 100*a* + 10*b* + 10*a* + *b*
> = **100*a* + 10(*a* + *b*) + *b*.**
>
> In plain language: **hundreds = *a*, tens = (*a* + *b*), units = *b*.** That's the trick.
>
> When *a* + *b* ≥ 10, the "10(*a*+*b*)" term overflows the tens place by exactly one hundred — that's the carry.
>
> **It is not magic. It is the distributive law.**

## Homework

- Apply the proof to a number you choose. Pick any 2-digit number, write it as 10*a* + *b*, distribute by 11, and show the final form. Show all 5 lines.

## Differentiation

- **Tier up:** Prove the same identity for ×111 (multiplication by 111). What's the equivalent "split-and-add" pattern? Test it on 23 × 111.
- **Tier down:** Don't worry about the carry-case derivation. Get the no-carry version of the proof working.

## Teacher notes

- This is the conceptual core of the module. Don't rush.
- Students who can write the algebra but can't *speak* it should be pushed to verbalise — "distribute" is the verb that matters here.
- The most common error in student paragraphs: confusing "the trick" with "the answer." The trick is the algorithm; the algebra justifies the algorithm.
- About 20% of students will object: *"But this is just multiplication, not anything special."* That's the right reaction. Honour it: *"You're right — and that's the deeper point. The 'special' name (*Ekādhikena Pūrveṇa*) is a label; the math underneath is regular algebra."*

## Citation(s) used in this lesson

- (None required for the algebra itself — it is original derivation.)
- Optional teacher reference: Tirthaji (1965), sūtra 1, for the framing.
