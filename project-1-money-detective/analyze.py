"""
Money Detective — June 2026 statement analysis
------------------------------------------------
What this does:
  Reads transactions.csv (Date, Description, Out, In) and:
    1. Totals money out / in, and checks the resulting closing balance
       against the real bank-reported closing balance.
    2. Flags likely recurring/subscription charges (named senders like
       insurance, phone, software subscriptions).
    3. Flags likely duplicate charges (same description + same amount,
       same/adjacent day).
    4. Ranks total spend by merchant/description.
    5. Separately lists foreign-currency (SEK/USD) transactions.

Expects: transactions.csv in the same folder, columns Date, Description, Out, In.
Rules encoded: see brief.md.
"""

import csv
from collections import defaultdict
from datetime import datetime

OPENING_BALANCE = 905.03
BANK_REPORTED_CLOSING_BALANCE = 10006.43

rows = []
skipped = []

with open("transactions.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        try:
            out_amt = float(r["Out"]) if r["Out"].strip() else 0.0
            in_amt = float(r["In"]) if r["In"].strip() else 0.0
            date = datetime.strptime(r["Date"], "%Y-%m-%d")
            rows.append({
                "date": date,
                "desc": r["Description"].strip(),
                "out": out_amt,
                "in": in_amt,
            })
        except Exception:
            skipped.append(r)

print(f"Rows read: {len(rows)}   Rows skipped (unparseable): {len(skipped)}")

# 1. Totals + balance check (known-answer test)
total_out = round(sum(r["out"] for r in rows), 2)
total_in = round(sum(r["in"] for r in rows), 2)
calculated_closing = round(OPENING_BALANCE + total_in - total_out, 2)

print("\n--- BALANCE CHECK (verification against bank's own reported number) ---")
print(f"Opening balance:            {OPENING_BALANCE:,.2f} NOK")
print(f"Total money in:             {total_in:,.2f} NOK")
print(f"Total money out:            {total_out:,.2f} NOK")
print(f"Calculated closing balance: {calculated_closing:,.2f} NOK")
print(f"Bank-reported closing bal.: {BANK_REPORTED_CLOSING_BALANCE:,.2f} NOK")
print(f"MATCH: {calculated_closing == BANK_REPORTED_CLOSING_BALANCE}")

# 2. Recurring / subscription-like charges
recurring_keywords = ["Storebrand", "Lyse Tele", "Autosync", "Anthropic", "Til:"]
recurring = [r for r in rows if any(k.lower() in r["desc"].lower() for k in recurring_keywords)]

print("\n--- LIKELY RECURRING / SUBSCRIPTION CHARGES ---")
for r in sorted(recurring, key=lambda x: x["date"]):
    print(f"{r['date'].date()}  {r['desc']:<35}  {r['out']:>10.2f} NOK")

# 3. Likely duplicate charges: same description + same amount, within 1 day
by_key = defaultdict(list)
for r in rows:
    if r["out"] > 0:
        by_key[(r["desc"], r["out"])].append(r["date"])

print("\n--- LIKELY DUPLICATE CHARGES (same merchant, same amount, same/adjacent day) ---")
found_dupe = False
for (desc, amt), dates in by_key.items():
    dates = sorted(dates)
    for i in range(1, len(dates)):
        gap = (dates[i] - dates[i-1]).days
        if gap <= 1:
            found_dupe = True
            print(f"{desc:<35} {amt:>10.2f} NOK on {dates[i-1].date()} and {dates[i].date()}")
if not found_dupe:
    print("None found under current rule (same desc + same amount + <=1 day apart).")

# 4. Foreign currency transactions (separate — not duplicates just because they repeat)
foreign = [r for r in rows if "SEK" in r["desc"] or "USD" in r["desc"]]
print("\n--- FOREIGN CURRENCY TRANSACTIONS (flagged separately per rules) ---")
for r in sorted(foreign, key=lambda x: x["date"]):
    print(f"{r['date'].date()}  {r['desc']:<35}  {r['out']:>10.2f} NOK")
print(f"Total spent abroad: {sum(r['out'] for r in foreign):,.2f} NOK")

# 5. Spend ranked by merchant/description
spend_by_merchant = defaultdict(float)
for r in rows:
    spend_by_merchant[r["desc"]] += r["out"]

print("\n--- TOP 10 BY TOTAL SPEND (merchant/description) ---")
for desc, amt in sorted(spend_by_merchant.items(), key=lambda x: -x[1])[:10]:
    print(f"{desc:<40} {amt:>10.2f} NOK")

if skipped:
    print("\n--- SKIPPED ROWS ---")
    for s in skipped:
        print(s)
