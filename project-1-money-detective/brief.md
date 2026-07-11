# Brief: Money Detective — June 2026 Account Statement

## Goal
Find spending leaks in my real bank statement: recurring/subscription charges,
possible forgotten subscriptions, and duplicate or repeated payments — patterns
a generic budgeting app wouldn't know to look for in my specific data.

## Input
One file, transactions.csv, extracted from my SpareBank 1 Nord-Norge account
statement for the period 01.06.2026 - 30.06.2026. Columns: Date, Description,
Out (money leaving the account, NOK), In (money entering the account, NOK).
About 97 rows. Opening balance was 905.03 NOK.

## Output
1. Total money out and total money in for the month.
2. A calculated closing balance (opening + in - out), to check against the
   real bank-reported closing balance of 10 006.43 NOK.
3. Recurring/subscription-like charges: same or very similar description,
   appearing on a regular (e.g. monthly) cycle, similar amount.
4. Likely duplicate charges: same description AND same amount on the same or
   adjacent day.
5. A ranked list of total spend per merchant/description, to spot where money
   actually goes.

## Rules
- "Kiwi", "Extra", "Obs", "Europris", "Rema", "Normal", "Lørenskog Dagli",
  "Tenza", "Snarkjøp" style entries are everyday grocery/convenience purchases
  — not subscriptions, even though Kiwi appears extremely often.
- "Til: X Betalt" and named recurring senders (e.g. Storebrand Forsikring,
  Lyse Tele, Autosync, Anthropic Claude Sub) are the candidates most likely to
  be actual subscriptions/recurring bills — flag these explicitly.
- Foreign currency purchases (marked with *6469, SEK or USD amounts) should be
  identified separately since they are foreign transactions, not local
  duplicates, even if descriptions repeat (e.g. multiple "Skogar 1:50 AB").
- Treat "Out" as money spent and "In" as money received. Do not merge the two.

## Edge cases
- If a row can't be parsed as a number, skip it and list it separately.
- Two charges to the same merchant on the same day are NOT automatically
  duplicates if the amounts differ (that's just two separate purchases).
- Round amounts to 2 decimals throughout.
