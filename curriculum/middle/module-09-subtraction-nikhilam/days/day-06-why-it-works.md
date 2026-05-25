# Day 6 — Why It Works

**Module:** Nikhilam Subtraction · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will explain *why* the Nikhilam rule produces the correct answer, using the identity `10ⁿ − A = (10ⁿ − 1) − A + 1`, and will draw a bar-model that shows the same idea visually.

## Materials

- Whiteboard
- Worksheet: "explain to a friend" prompt + space
- Coloured pencils for the bar model
- The 16-sūtra list (`Microsoft Word - sutras1.pdf`) visible

## Lesson flow

### Warm-up (5 min)

- Sūtra chant.
- Quick fire: 4 complements (mix of 2-digit and 3-digit).
- Return graded formatives. Acknowledge the common errors.

### Core (20 min) — The mathematical reason

1. **The core identity (write boxed on the board):**

   > **10ⁿ − A = (10ⁿ − 1) − A + 1**

2. **Why this identity?** *"`10ⁿ` is `1` followed by `n` zeros — e.g. 1000 = 10³. `10ⁿ − 1` is the same number minus one — e.g. 999. That's just 'all nines.' So the identity says: subtracting A from a round base equals (subtracting A from all-nines) plus 1."*

3. **Why does that help?** *"Subtracting any digit from 9 is trivial — there's no borrow. We always have `9 ≥ digit`. So `(10ⁿ − 1) − A` is a clean digit-by-digit subtraction with no borrow. Then we add 1 at the end."*

4. **Where does the "+1" go?** *"Into the last digit. So instead of doing 'from 9' on the last digit and then '+1,' we just do 'from 10' on the last digit. Same thing. That's why the sūtra says 'all from nine and **the last from ten**.'"*

5. **Walk through a concrete example with full algebra:**

   ```
   1000 − 567
   = (1000 − 1) − 567 + 1     ← identity
   = 999 − 567 + 1
   = (9-5)(9-6)(9-7) + 1      ← digit-wise from 9 — no borrow!
   = 4 3 2 + 1
   = 432 + 1
   = 433.                     ✓
   ```

   Now compare with the sūtra direct version:

   ```
   1000 − 567
   = (9-5)(9-6)(10-7)         ← Nikhilam, last from 10
   = 4 3 3
   = 433.                     ✓
   ```

   *"Same answer. The sūtra is just the identity, made into a mnemonic."*

6. **Bar model.**

   Draw a long horizontal bar labelled `1000`. Inside, mark off a left segment labelled `567` and a right segment labelled `?` (the unknown). *"What we want is the right segment."*

   Now ask: *"What's the length of the bar minus 1?"* — Answer: `999`.

   Mark a tiny `+1` sliver at the right end of the bar. Now `999 = 567 + (right segment − 1)`, so right segment = `(999 − 567) + 1 = 432 + 1 = 433`.

   *"That's the picture-version of the algebra. Same thing."*

### Activity (15 min) — Explain to a friend

- Worksheet prompt:

  > Imagine your Grade 4 cousin asks: *"Why does Nikhilam work? Isn't it just magic?"* In 4–6 sentences, explain why it's NOT magic. Use the words **nine**, **ten**, **plus one**, and **place value**.

- 10 min individual writing.
- 5 min pair-share: each partner reads their paragraph; partner says one thing that's clear and one that's unclear.

### Wrap-up (5 min)

- Read one strong paragraph aloud (with permission).
- Honest historical note: *"Tirthaji's book (1965) gives this rule. The rule itself is genuinely correct. Tirthaji's claim that it comes from a Vedic appendix has not been verified by other Sanskritists. We use the rule because it works. The history is younger than the name suggests."*
- Preview Day 7: *"Tomorrow — a surprise. The same rule is built into how computers subtract. It's called 'two's complement.'"*

## Student-facing content

> **Why Nikhilam works**
>
> The key identity:
>
> **10ⁿ − A = (10ⁿ − 1) − A + 1**
>
> - `10ⁿ − 1` is "all nines" (e.g. 9999).
> - Subtracting A from "all nines" is trivial digit-by-digit — there's no borrow because 9 ≥ any digit.
> - The "+ 1" at the end gets absorbed into the last digit, turning "9 − last_digit" into "10 − last_digit."
>
> That's the whole proof.
>
> Tirthaji's *Vedic Mathematics* (1965) packages this proof into six Sanskrit words: *Nikhilaṁ Navataścaramaṁ Daśataḥ* — "all from nine and the last from ten." The math is real. The Sanskrit is from a 20th-century synthesis, not a Vedic text.
>
> **It is not magic. It is good notation.**

## Homework

- Find ONE moment in your daily life where you naturally "round to the nearest 100 / 1000" without thinking. Write 2 sentences describing it. (E.g. tipping at a restaurant. Counting change. Comparing prices.)
- Practise: complement of `4321` to 10 000. Show the algebraic identity for this one (the same way the lesson did 1000 − 567).

## Differentiation

- **Tier up:** Write the explanation for a Grade 11 student. Use formal notation. Show the identity holds for any base b: `bⁿ − A = (bⁿ − 1) − A + 1`. Preview Day 7's binary case.
- **Tier down:** Skip the written explanation. Verbalise to your partner. Use the bar-model picture as scaffold.

## Teacher notes

- The most common student error in the paragraph: confusing "the last digit takes from 10" with "you add 1 at the end." These are the SAME operation, just expressed differently — `10 − x = (9 − x) + 1`. Some students will write both; that's fine.
- Some students prefer the visual bar-model; some prefer the algebra. Both are valid. Honour the choice and ask them to draw the OTHER one as homework.
- Honest provenance is essential here. Don't oversell. Some students (or parents) believe Nikhilam is "ancient Vedic mathematics." Clarify gently; preview the Senior-band treatment of the historicity question.

## Citation(s) used in this lesson

- Tirthaji, *Vedic Mathematics* (1965), sūtra Nikhilam (#2) — primary source.
- *Microsoft Word - sutras1.pdf* — wall reference for the full 16 sūtra list.
