# Project 1 — Money Detective

## The Problem

Instead of starting a new budget going forward, I examined my real June 2026
bank statement to hunt for spending leaks: recurring/subscription charges,
possible forgotten subscriptions, and duplicate payments. These are the kind
of personal-rule leaks a generic budgeting app can't find, because it doesn't
know which of my "Til:" transfers are bills vs. one-off payments.

## AI Tool Used

Claude (Claude.ai / Claude Sonnet), using its code-execution ("write and run
code") capability.

## Data

`transactions.csv` — 97 transactions extracted from my real SpareBank 1
Nord-Norge account statement for the period 01.06.2026–30.06.2026.
Columns: Date, Description, Out (NOK), In (NOK).

## The Brief I Gave the AI

See `brief.md` for the full 5-part brief (Goal, Input, Output, Rules, Edge
cases). In short: find recurring/subscription charges, flag likely
duplicates, separate foreign-currency transactions, and rank spend by
merchant — while treating everyday grocery stores (Kiwi, Extra, Obs, etc.)
as normal spending, not subscriptions.

## How I Verified the Result

The bank statement itself states the closing balance for the period:
**10,006.43 NOK**. I had the AI's code independently calculate the closing
balance (opening balance + total money in − total money out) from the raw
transaction list, without telling it the answer in advance.

```
Calculated closing balance: 10,006.43 NOK
Bank-reported closing balance: 10,006.43 NOK
MATCH: True
```

Since the code's independently calculated number matched the bank's own
printed number exactly, I trust the rest of its output (the recurring-charge
list, duplicate check, and merchant ranking) that I could not otherwise
verify line-by-line by hand.

## Result / Catch

- **All money accounted for**: the calculated balance matched the bank's
  reported balance exactly, confirming no transactions were missed or
  misread.
- **Four recurring/subscription charges identified**: Storebrand Forsikring
  (insurance, 948 NOK), Lyse Tele/ice (phone/internet, 299.25 NOK), Autosync
  AS (524 NOK), and an Anthropic Claude subscription (242.88 NOK).
- **No duplicate charges found** this month under the rule "same merchant +
  same amount + same/next day."
- **Biggest real spending category**: a single Kiwi grocery store location,
  totaling 3,973.20 NOK for the month — nearly 4x the insurance bill, and
  the single largest spend line overall.
- **Foreign currency spend**: 4,424.57 NOK spent in Sweden (SEK) on 27.06,
  correctly separated from local duplicate-detection so it wasn't
  mis-flagged.

## What Worked / What Didn't

- Worked well: giving the AI explicit "Rules" (e.g., which merchants are
  everyday purchases vs. likely subscriptions) prevented it from
  mis-classifying frequent grocery visits as suspicious recurring charges.
- Challenge: the source PDF's raw text needed manual transcription into a
  clean CSV before analysis, since column alignment was lost when extracting
  text from the PDF.

## Files in This Folder

- `analyze.py` — the final script
- `transactions.csv` — the (anonymized) transaction data used
- `brief.md` — the 5-part brief given to the AI
- `prompts.md` — the prompts used, in order
- `screenshots/` — screenshots of the run and results
