# Project 2 — What's My Grade, Really

## The Problem
Generic grade-tracking apps don't know my teacher's specific rules: category
weights, and that the lowest quiz score gets dropped. I wanted my true
current grade and the exact score I need on the final exam to hit a target
grade — calculated using my teacher's actual policy, not a simple average.

## AI Tool Used
Claude (Claude.ai / Claude Sonnet), using its code-execution ("write and run
code") capability.

## Data
`scores.csv` — sample scores across 4 categories: 5 quizzes, 4 assignments,
1 midterm, and a not-yet-taken final exam.

(Note: for this submission, illustrative/sample data was used to demonstrate
the method, since my available real transcript data was a full diploma
record rather than a single in-progress course with a final exam.)

## The Brief I Gave the AI
See `brief.md`. Key rules encoded:
- Weights: Quizzes 10%, Assignments 30%, Midterm 25%, Final Exam 35%
- Lowest quiz score is dropped before averaging
- The Final Exam, if not yet taken, must NOT be counted as a zero

## How I Verified the Result
I calculated the Quiz category by hand: scores were 7, 9, 4, 8, 10 (out of
10 each). Dropping the lowest (4), the remaining scores are 7+9+8+10 = 34
out of 40 = **85.0%**.

The code's output for the Quiz category:
```
Quiz           85.0%   (weight: 10%)
```
This matches my hand calculation exactly, so I trust the rest of the
category calculations and the final weighted result that I did not check
by hand.

## Result
- Current grade so far (using only completed categories): **82.4%**
- To reach a target overall grade of **85%**, I need **89.9 out of 100** on
  the Final Exam.

## What Worked / What Didn't
- Worked well: explicitly stating "don't count the ungraded final as a zero"
  in the Edge Cases section prevented a common mistake — early drafts of
  the brief without this rule would have shown a misleadingly low current
  grade.
- Worked well: asking for a hand-checkable category (Quiz, with a simple
  drop rule) made verification fast and gave real confidence in the more
  complex weighted final calculation.

## Files in This Folder
- `grade_calculator.py` — the final script
- `scores.csv` — the score data used
- `brief.md` — the 5-part brief given to the AI
- `prompts.md` — the prompts used
- `screenshots/` — screenshots of the run and results
