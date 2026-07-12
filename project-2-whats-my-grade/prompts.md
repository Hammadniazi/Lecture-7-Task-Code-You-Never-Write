# Prompts Used — What's My Grade, Really

## Initial prompt
> "Paste your scores and your teacher's grading rules into the AI as plain
> text and ask it to write a script that calculates your current grade."

## The Brief (refined prompt)
See `brief.md` for the full structured brief. Key elements that mattered:

- **Rules**: stated the exact category weights (Quiz 10%, Assignment 30%,
  Midterm 25%, Final 35%) and the drop-lowest-quiz rule explicitly, rather
  than assuming the AI would guess a standard weighting.
- **Edge cases**: explicitly instructed that an untaken Final Exam should
  NOT be treated as a zero when reporting the current grade — this is a
  common way grade calculators mislead students.

## Verification prompt
> "Calculate the Quiz category by hand yourself and confirm it matches what
> the script reports."

## Follow-up prompt (target grade)
> "Tell me the exact score I need on the Final Exam to reach an overall
> grade of 85%. If it's mathematically impossible, tell me that plainly
> instead of giving a number over 100."

## Result
The script correctly separated "current grade so far" from a projected
final grade, correctly applied the drop-lowest-quiz rule, and calculated a
mathematically consistent required final-exam score on the first run.
