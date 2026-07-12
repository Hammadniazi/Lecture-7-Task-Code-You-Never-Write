"""
What's My Grade, Really — grade calculator
--------------------------------------------
What this does:
  Reads scores.csv (Category, Item, Score, MaxScore) and, using the
  teacher's actual grading policy encoded below:
    1. Calculates my percentage in each category (dropping the lowest
       quiz score, per the teacher's rule).
    2. Calculates my current overall grade using only completed categories.
    3. Calculates the exact score needed on the Final Exam to reach a
       target overall grade of 85%.

Expects: scores.csv in the same folder.
Rules encoded: see brief.md.
"""

import csv
from collections import defaultdict

WEIGHTS = {
    "Quiz": 0.10,
    "Assignment": 0.30,
    "Midterm": 0.25,
    "Final": 0.35,
}
TARGET_GRADE = 85.0

by_category = defaultdict(list)
final_max = 100

with open("scores.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        cat = r["Category"].strip()
        score = r["Score"].strip()
        max_score = float(r["MaxScore"])
        if cat == "Final":
            final_max = max_score
            if score == "":
                continue  # not yet taken — don't count as zero
        if score == "":
            continue
        by_category[cat].append((float(score), max_score))

# --- Category percentages ---
category_pct = {}

# Quizzes: drop lowest score first
quiz_scores = by_category.get("Quiz", [])
if quiz_scores:
    lowest = min(quiz_scores, key=lambda x: x[0] / x[1])
    kept = [s for s in quiz_scores if s != lowest] if len(quiz_scores) > 1 else quiz_scores
    total_score = sum(s for s, m in kept)
    total_max = sum(m for s, m in kept)
    category_pct["Quiz"] = round(100 * total_score / total_max, 1)

# Assignments and Midterm: straight average of percentages
for cat in ["Assignment", "Midterm"]:
    items = by_category.get(cat, [])
    if items:
        total_score = sum(s for s, m in items)
        total_max = sum(m for s, m in items)
        category_pct[cat] = round(100 * total_score / total_max, 1)

print("--- CATEGORY PERCENTAGES ---")
for cat, pct in category_pct.items():
    print(f"{cat:<12} {pct:>6.1f}%   (weight: {WEIGHTS[cat]*100:.0f}%)")

# Manual verification note for Quiz category (do this by hand too!)
print("\n--- HAND-CHECK (Quiz category) ---")
print(f"Raw quiz scores/max: {quiz_scores}")
print(f"Lowest dropped: {lowest}")
kept_str = " + ".join(str(int(s)) for s, m in kept)
print(f"Remaining: {kept_str} out of {int(sum(m for s,m in kept))} "
      f"= {sum(s for s,m in kept)}/{sum(m for s,m in kept)} "
      f"= {category_pct['Quiz']}%")

# --- Current grade so far (completed categories only, weights renormalized) ---
completed_weight = sum(WEIGHTS[c] for c in category_pct)
weighted_sum = sum(category_pct[c] * WEIGHTS[c] for c in category_pct)
current_grade_renormalized = round(weighted_sum / completed_weight, 1)

print(f"\n--- CURRENT GRADE (so far, Final not yet taken) ---")
print(f"Weighted sum across completed categories: {round(weighted_sum,2)}")
print(f"Completed weight so far: {completed_weight*100:.0f}%")
print(f"Current grade (renormalized to 100%): {current_grade_renormalized}%")

# --- Score needed on Final to reach target ---
final_weight = WEIGHTS["Final"]
needed_final_pct = (TARGET_GRADE - weighted_sum) / final_weight
needed_final_score = round(needed_final_pct / 100 * final_max, 1)

print(f"\n--- WHAT I NEED ON THE FINAL ---")
print(f"Target overall grade: {TARGET_GRADE}%")
print(f"Required Final Exam percentage: {round(needed_final_pct,1)}%")
if needed_final_pct > 100:
    print(f"NOT POSSIBLE: would require {round(needed_final_pct,1)}% on the "
          f"final, which exceeds 100%. Target grade cannot be reached from "
          f"current standing.")
else:
    print(f"Required Final Exam score (out of {final_max}): {needed_final_score}")
