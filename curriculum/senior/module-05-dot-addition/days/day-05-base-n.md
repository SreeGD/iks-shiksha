# Day 5 — Base-n Generalisation

**Module:** Bindu Paddhati (Senior) · **Time:** 45 min

## Learning objective

Students extend the dot method to base 8 and base 16, identify what changes and what stays the same, and complete the formative quiz.

## Materials

- Whiteboard
- Base-conversion reference card
- Mixed-base practice sheets

## Flow

### Warm-up (5 min)

- Provocation: "Does the dot method work in base 8? Base 2?"
- Take 2 student guesses. Don't resolve yet.

### Core (20 min) — Generalisation

1. **In base 10:** the dot represents "10 used up" → 1 carried.
2. **In base 8:** the dot represents "8 used up" → 1 carried.
3. **In base 16:** the dot represents "16 used up" → 1 carried.

4. **What changes:** the *target sum* (8 or 16 instead of 10).
5. **What stays the same:** scan procedure; dot count = carry; units = leftover.

6. **Worked example in base 8:**
   ```
   Column (base 8): 4, 7, 3, 6, 5
   - Start total: 0
   - +4 → 4
   - +7 → 11_(10) = 13_(8). Wait — in base 8, 8 is "10". So 4+7 = 11_(10), which is 1 "8" + 3, so DOT on 7, total = 3.
   - +3 → 6
   - +6 → 12_(10) = 14_(8). That's 1 "8" + 4. DOT on 6, total = 4.
   - +5 → 9_(10) = 11_(8). That's 1 "8" + 1. DOT on 5, total = 1.
   - Final units (base 8): 1. Carries: 3.
   ```

   Check: 4+7+3+6+5 = 25_(10) = 31_(8). Units = 1, "tens" (i.e. 8s) = 3. ✓

7. **The general rule:**

   > In base *n*, mark a dot every time the running total reaches or exceeds *n*. Subtract *n* from the running total. Final running total = units. Dot count = "carry to next column."

### Practice (10 min)

3 problems:
- Base 8: column of 6 single-digit (in base 8: 0–7) numbers.
- Base 16: column of 4 single-digit (0–F) numbers. (Hex.)
- Base 10: a real 4×4 multi-column for comparison.

### Formative quiz Part B (8 min)

- 5 questions: mostly base-conversion and base-*n* dot method.

### Wrap-up (2 min)

- Preview Day 6: *"Tomorrow — the historicity question. Was 'Vedic mathematics' actually Vedic?"*

## Differentiation

- **Tier up:** Base 2 (binary) dot method. (Trivial: every column entry is 0 or 1; the dot marks whenever you have 2 ones.)
- **Tier down:** Stay in base 10; review the procedure.

## Teacher notes

- The base-*n* extension is a beautiful "of course it works" moment for math-track students. Lean into it.
- For computer-science-track students, base 2 dot method = binary half-adder logic.

## Citation(s) used

- (No new RAG/SutraGanita citations — this is original mathematical extension.)
