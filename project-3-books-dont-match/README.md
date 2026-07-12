# Project 3 — The Books Don't Match

## The Problem
I collected trip dues from 12 students (1,500 NOK each = 18,000 NOK total,
a number I know is correct because I counted the roster myself). The digital
payment record is messy: nicknames, initials, a payment made from a parent's
account, a duplicate transfer, and one entry that doesn't match anyone. I
needed to know exactly who still owes money and what the unexplained entries
are.

## AI Tool Used
Claude (Claude.ai / Claude Sonnet), using its code-execution ("write and run
code") capability.

## Data
- `roster.csv` — the known-correct list: 12 students, 1,500 NOK due each.
- `payments.csv` — the messy digital transfer record, used exactly as
  received, with inconsistent name formatting.

(Note: this is a realistic sample scenario built to demonstrate the method,
following the same structure as a real trip-fund reconciliation.)

## The Brief I Gave the AI
See `brief.md`. Key personal rules encoded:
- Name mappings for nicknames/initials (e.g. "Ahmed K" = Ahmed Khan)
- "Fatima's Mor" = a payment made by Fatima Noor's mother on her behalf
- Partial payments are NOT treated as paid in full
- Duplicate payments (same student, same amount, close dates) count once
  toward dues, with the extra flagged separately
- Anything that doesn't match a roster name is flagged as unmatched, never
  silently assigned to a student

## How I Verified the Result
I stated the expected total up front: 12 students x 1,500 NOK = **18,000
NOK** — a number I know is correct because it comes directly from my own
roster count.

I also hand-checked the final gap: Bilal owes 750 + Imran owes 1,500 +
Layla owes 1,500 = **3,750 NOK**, which matches the code's own
"Total still outstanding" figure exactly.

```
Total still outstanding (owed): 3,750.00 NOK
Gap = expected - counted toward dues: 3,750.00 NOK
```

## Result / Catch
- **10 of 12 students paid in full**, correctly matched despite messy names.
- **3,750 NOK still outstanding**: Bilal Hussain owes 750 (partial payment),
  Imran Qureshi and Layla Farooq owe the full 1,500 each (never paid).
- **A duplicate payment caught**: Sara Iqbal was charged/paid twice for the
  same amount — likely a mistaken double transfer, worth refunding or
  double-checking.
- **An unexplained entry found**: a 1,500 NOK payment from "Karim Store AS"
  that doesn't match any student — needs follow-up before it can be
  explained or corrected.

## What Worked / What Didn't
- Worked well: giving the AI an explicit name-mapping table up front meant
  it never had to guess who "M Ali" or "Fatima's Mor" was — this is exactly
  the kind of personal knowledge no app could infer on its own.
- Worked well: explicitly telling it NOT to assign the unmatched "Karim
  Store AS" entry to anyone prevented a wrong guess that would have hidden
  a real problem.
- Important design choice: distinguishing "total money received in the
  account" from "total counted toward student dues" avoided a false sense
  that the books balanced when they didn't.

## Files in This Folder
- `reconcile.py` — the final script
- `roster.csv` — the known-correct expected amounts
- `payments.csv` — the messy digital payment record
- `brief.md` — the 5-part brief given to the AI
- `prompts.md` — the prompts used
- `screenshots/` — screenshots of the run and results
