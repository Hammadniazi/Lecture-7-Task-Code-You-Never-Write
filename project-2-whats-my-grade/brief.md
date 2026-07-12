# Brief: What's My Grade, Really

## Goal
Calculate my true current grade in this course using my teacher's exact
grading policy (not a generic percentage average), and find out exactly what
score I need on the final exam to reach my target grade of 85% (a B).

## Input
One file, scores.csv, with columns: Category, Item, Score, MaxScore.
Categories: Quiz (5 quizzes so far), Assignment (4 assignments), Midterm
(1 exam), Final (not yet taken, Score left blank).

## Output
1. My percentage in each category (after applying the drop rule for quizzes).
2. My current overall weighted grade, using ONLY completed categories,
   clearly stated as "current grade so far" (not padded with a zero for the
   final).
3. The exact score (out of 100) I need on the Final Exam to reach an overall
   85%, given the category weights below.
4. If 85% is mathematically impossible (i.e. requires >100 on the final),
   say so plainly.

## Rules (the teacher's actual policy)
- Category weights: Quizzes = 10%, Assignments = 30%, Midterm = 25%,
  Final Exam = 35%. Weights sum to 100%.
- Quizzes: the single lowest quiz score is dropped before averaging the rest.
- All other categories: straight average of the items in that category.
- Final grade = weighted sum of each category's percentage x its weight.

## Edge cases
- The Final Exam row has no score yet — treat it as "not yet taken," not as
  a zero, when reporting the CURRENT grade.
- If a score is missing/blank in a category that already has other scores,
  ignore that blank item entirely (don't count it as zero) unless it's the
  Final.
- Round all percentages to 1 decimal place.
