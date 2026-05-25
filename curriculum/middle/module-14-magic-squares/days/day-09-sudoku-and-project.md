# Day 9 — Sudoku Connection + Project Session

**Module:** Magic Squares (*Bhadragaṇita*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will (a) distinguish a Sudoku puzzle from a magic square (Sudoku constrains *placement* but not *sums*), and (b) make substantial progress on their module project.

## Materials

- Sample 9×9 Sudoku puzzle (one per pair, easy difficulty)
- Project materials (graph paper, markers, etc.)

## Vocabulary introduced today

- *Sudoku* — a 9×9 number-placement puzzle (Japanese name, from Japanese 数独). Standard rules: each row, each column, and each 3×3 block contains the digits 1–9 exactly once.
- *constraint satisfaction* — a problem type where you must place objects in a structure so that all "constraints" (rules) are satisfied. Magic squares and Sudoku are both constraint-satisfaction problems.

## Lesson flow

### Warm-up (5 min)

- *"Many of you have seen Sudoku. Is it a magic square?"* — take 3 student responses.
- Hold the answer. Promise: "we'll settle this in 10 minutes."

### Core (15 min)

1. **The rules side-by-side.** Write on the board:

   | Property | Magic Square (3×3, 1–9) | Sudoku (3×3 within 9×9) |
   |----------|-------------------------|-------------------------|
   | Uses digits 1–9? | yes — once each | yes — once each within each 3×3 block |
   | Each row uses each digit once? | no (a row has just 3 distinct values from 1–9) | yes (each row uses 1–9) |
   | Each column uses each digit once? | no | yes |
   | Diagonals sum to a constant? | yes | not required |
   | Rows sum to a constant? | yes (= 15) | not enforced |
   | Columns sum to a constant? | yes | not enforced |

   *"Magic squares constrain* sums *. Sudoku constrains* placement *. Different constraints — different puzzles."*

2. **Both are constraint-satisfaction problems.** Each gives you a structure (9 cells in 3×3, or 81 cells in 9×9) and a set of rules. You search for placements that satisfy all rules. Computers solve these the same way.

3. **A bridge example.** It is possible to have a 9×9 grid that is *both* a Sudoku AND a magic square (every row, column, *and* 3×3 block sums to 45 — which works because rows/columns automatically sum to 1+2+...+9 = 45). Such squares exist; they are rare. Show one if you have time. *(Not required at Middle band.)*

### Activity (20 min) — Project work

- Pairs work on their project. Teacher circulates.
- Required checkpoints by end of class:
  - The magic square is fully constructed (5×5 or larger).
  - Magic constant verified for at least 3 rows, 3 columns, both diagonals.
  - Citation is in place (Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14, 1356 CE).
  - At least one paragraph (or one slide of a video) of explanation drafted.

- The teacher does a 1-minute review with each pair to flag any errors before Day 10.

### Wrap-up (5 min)

- Quick poll: "On a scale of 1–5, how ready do you feel for Day 10's share?" Show of fingers.
- For 1–2 ratings: teacher schedules a 5-min meeting with that pair before Day 10.

## Student-facing content

> **Sudoku ≠ magic square.**
>
> | | Magic square (3×3, 1–9) | Sudoku 3×3 block |
> |---|---|---|
> | Cells | 9 distinct values from 1–9 | 9 distinct values from 1–9 |
> | Rows sum to a constant? | **Yes (15)** | No requirement |
> | Each row has all 9 digits? | No (only 3 cells) | **Yes** (in 9×9 Sudoku) |
> | Diagonals constrained? | **Sums** | Not required |
>
> Both are *constraint-satisfaction* problems. Different constraints — different puzzles. Sudoku appeared in modern form in the 1970s–80s (popularised in Japan from 1986). Magic squares are at least 2500 years old (Lo Shu).

## Homework

- Finish anything not finished in class. Tomorrow is the share, not the start.
- Time yourself: how fast can you construct a 5×5 magic square now, versus on Day 5?

## Differentiation

- **One tier up:** Find or construct a 9×9 grid that is both a Sudoku AND a magic square (every row/column/3×3 block sums to 45). Hint: rows and columns of a Sudoku already sum to 45. You only need to also make every 3×3 block sum to 45.
- **One tier down:** Use the class time to construct one more 5×5 magic square as practice for the summative. Speed is not the goal; correctness is.

## Teacher notes

- The Sudoku discussion is short on purpose. The point is to draw a clean distinction, not to teach Sudoku.
- Spend the project-work time circulating. Most errors are caught at this stage.
- Some students will worry about the "design-your-own" requirement. Remind them: choosing the size, the starting number, and the presentation format are all design choices. They are not expected to invent a new algorithm.

## Citation(s) used in this lesson

- Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE — paraphrased in projects.
