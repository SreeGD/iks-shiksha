# Day 7 — Why It Works: The Algebra

**Module:** Nikhilam Multiplication · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will state the algebraic identity behind the Nikhilam method `(B − a)(B − b) = B(B − a − b) + ab`, derive it on paper, and explain in their own words why this matches the procedure.

## Materials

- Whiteboard.
- The 16-sūtra list (`Microsoft Word - sutras1.pdf`) — printed and visible.
- Worksheet: "explain to a friend" prompt + space.

## Lesson flow

### Warm-up (5 min)

- Quick Nikhilam round on `97 × 96` (chorus answer: 9312) and `103 × 104` (10712).
- *"You've been doing this for a week. Today we prove why it works."*

### Core (20 min) — The algebraic proof

1. **Set the variables.** Call the base `B` (= 100, say). Call the two factors `B − a` and `B − b`, where `a` and `b` are the deficits.

   For 97 × 96: `B = 100`, `a = 3`, `b = 4`. Then 97 = `B − a` and 96 = `B − b`.

2. **Multiply directly:**
   ```
   (B − a)(B − b) = B² − Ba − Bb + ab
                  = B² − B(a + b) + ab
                  = B(B − a − b) + ab
                  = B · LEFT + RIGHT
   ```
   where `LEFT = B − a − b` and `RIGHT = ab`.

3. **Match this to the Nikhilam procedure.**

   | Algebra | Nikhilam step |
   |---|---|
   | `B − a − b` | Cross-subtract: take one number minus the *other's* deficit |
   | `ab` | Multiply the deficits for the RIGHT part |
   | `B · LEFT + RIGHT` | Concatenate (with the right pad) |

4. **Check: cross-subtract gives `B − a − b`.**
   - `(B − a) − b = B − a − b`. ✓ (97 − 4 = 93.)
   - `(B − b) − a = B − a − b`. ✓ (Either cross gives the same.)

5. **Why concatenation works.**
   - The "LEFT" digit pattern, placed in the next-higher slot, means we're multiplying it by B. (E.g. `93|12` = `93 × 100 + 12` = 9300 + 12 = 9312.)
   - So `93|12` is exactly `B · LEFT + RIGHT` = `100 · 93 + 12` = `9312`.
   - That's exactly what the formula said.

6. **The "above the base" case.** Use `(B + x)(B + y)`:
   ```
   (B + x)(B + y) = B² + Bx + By + xy
                  = B(B + x + y) + xy
                  = B · LEFT + RIGHT
   ```
   Now LEFT = `B + x + y` — cross-**add**. RIGHT = `xy`. Sign flips, procedure mirrors.

7. **The mixed case.** Use `(B + x)(B − y)`:
   ```
   (B + x)(B − y) = B² − By + Bx − xy
                  = B(B + x − y) + (−xy)
                  = B · LEFT + RIGHT
   ```
   LEFT = `B + x − y` (signed cross). RIGHT = `−xy` (negative). The negative right part is the sign issue from Day 5.

8. **Why the pad-width = zeros in base.** Because `B · LEFT + RIGHT` requires RIGHT to occupy the slots from 0 up to `B − 1`. If B = 100, RIGHT is at most a 2-digit number; if it overflows to 100 or more, the overflow rolls into LEFT. That's the "carry overflow" rule from Day 3.

### Activity (15 min) — Explain to a friend

- Worksheet prompt:
  > Imagine your Grade 4 cousin asks: *"Why does that Nikhilam trick work? Is it magic?"* In 5–7 sentences, explain why it's NOT magic. Use the words **base**, **deficit**, and **algebra**.

- 10 min individual writing. 5 min pair-sharing: read your paragraph to your partner; they tell you one part that's clear and one part that's unclear.

### Wrap-up (5 min)

- Read aloud one strong paragraph (with permission).
- The sūtra connection: write on the board:

  > "*Nikhilam Navataścaramaṁ Daśataḥ*" — "all from 9 and the last from 10" — is the rule for computing the **deficit** quickly (which we drilled on Day 2). The *multiplication* technique uses that deficit via the algebra above.

- Preview Day 8: *"Tomorrow — when is this method actually faster? And when should you use long multiplication?"*

## Student-facing content

> **The algebra behind Nikhilam**
>
> Let `B` be the base. Let `a` and `b` be the deficits.
>
> `(B − a)(B − b) = B(B − a − b) + ab`
>
> - `B − a − b` is the LEFT part (cross-subtract).
> - `ab` is the RIGHT part (product of deficits).
> - The concatenation `LEFT | RIGHT` equals `B × LEFT + RIGHT` — which is exactly what the algebra produces.
>
> **For excess (both above base):** `(B + x)(B + y) = B(B + x + y) + xy`. Cross-ADD; right part is positive.
>
> **For mixed:** `(B + x)(B − y) = B(B + x − y) + (−xy)`. Negative right part.
>
> The sūtra *Nikhilam Navataścaramaṁ Daśataḥ* names the technique for computing the deficit fast. The multiplication shortcut is the algebraic application.

## Homework

- Write a 1-paragraph explanation suitable for a Grade 7 student (your own grade level). Include one worked example with the algebra shown.
- Prove (B + x)(B − x) = B² − x² using the above identity. Find an example where this is faster than long multiplication. (Hint: 101 × 99.)

## Differentiation

- **Tier up:** Generalise. For three factors `(B − a)(B − b)(B − c)`, expand. Does the Nikhilam pattern extend? (Yes — for three factors near a base, see *Vedic Mathematics Batch1.pdf* extension section.)
- **Tier down:** Skip the formal algebra. Verify the identity by plugging in numbers (B=100, a=3, b=4 → both sides give 9312).

## Teacher notes

- The honest framing in one sentence: *"The Sanskrit sūtra names the deficit-computation rule. The algebraic identity is what makes the multiplication trick work, and that identity is just standard FOIL / distributivity."*
- A few students will object: *"If the algebra is just algebra, why call it Vedic?"* Honest answer: *"Good catch. The procedure has a Sanskrit name and was published in 1965 by Tirthaji. The math itself is older than any name — it's the distributive property. The Vedic-mathematics framing is contested among historians; we'll engage with that more at Senior band."*
- Reinforce: this is *not* a debunking. It's an honesty about what's old (algebra), what's modern (the packaging as 16 sūtras), and what's contested (the Vedic provenance).

## Citation(s) used in this lesson

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA) — Nikhilam multiplication, "why it works" section.
- *Microsoft Word - sutras1.pdf* — list of 16 Tirthaji sūtras.
- Optional teacher reference: *FUNDAMENTAL AND VEDIC MATHEMATICS .pdf*.
