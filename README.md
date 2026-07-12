# Code You Never Write — Real-World AI Coding Projects

**Name:** Muhammad Hammad Khan

## Summary

This repository contains four hands-on projects completed as part of the
"Code You Never Write" lecture task. In each project, I acted as the
client, not the programmer: I described a real problem in plain language,
had an AI write and run the code, and verified every result against a fact
or total I already knew to be true — before trusting or acting on it.

## Full Report

📄 [View the full report (Google Drive)](https://drive.google.com/file/d/1Z85MqOn4VnqC9blWBiFsDXXfsjyGOhK2/view?usp=sharing)

## AI Tools Used

Claude (Claude Sonnet), using its built-in code-execution ("write and run
code") capability, for all four projects.

## Projects

| Folder                         | Project                 | What it solves                                                                                                                                                          |
| ------------------------------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project-1-money-detective/`   | Money Detective         | Found recurring charges, subscriptions, and spending patterns in a real June 2026 bank statement, verified against the bank's own reported closing balance.             |
| `project-2-whats-my-grade/`    | What's My Grade, Really | Calculated a true weighted course grade using specific category weights and a drop-lowest-quiz rule, and found the exact final-exam score needed to hit a target grade. |
| `project-3-books-dont-match/`  | The Books Don't Match   | Reconciled a hand-counted expected total (class trip fund) against a messy digital payment record full of nicknames, a duplicate, and an unmatched entry.               |
| `project-4-organize-the-mess/` | Organize the Mess       | Safely cleaned up a cluttered Downloads-style folder using a backup-first, dry-run-before-execution safety ritual — and caught a real bug during plan review.           |

## Repository Structure

```
README.md                          <- this file
REPORT.md                          <- full write-up covering all 4 projects
project-1-money-detective/
    analyze.py
    transactions.csv
    brief.md
    prompts.md
    README.md
    screenshots/
project-2-whats-my-grade/
    grade_calculator.py
    scores.csv
    brief.md
    prompts.md
    README.md
    screenshots/
project-3-books-dont-match/
    reconcile.py
    roster.csv
    payments.csv
    brief.md
    prompts.md
    README.md
    screenshots/
project-4-organize-the-mess/
    organize.py
    brief.md
    prompts.md
    README.md
    screenshots/
```
