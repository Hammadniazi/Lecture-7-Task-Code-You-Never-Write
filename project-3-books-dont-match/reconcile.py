"""
The Books Don't Match — class trip fund reconciliation
---------------------------------------------------------
What this does:
  Reads roster.csv (who owes what) and payments.csv (the messy digital
  transfer record, exactly as received) and:
    1. States the expected total up front.
    2. Maps messy payer names to real roster names using known personal
       rules (nicknames, initials, a parent's account).
    3. Flags duplicate payments (same student, same amount, nearby dates)
       and counts them only once toward dues.
    4. Flags any payment that can't be matched to a roster name at all.
    5. Reports who still owes money, and the overall gap.

Expects: roster.csv, payments.csv in the same folder.
Rules encoded: see brief.md.
"""

import csv
from collections import defaultdict
from datetime import datetime

# Personal knowledge: messy name -> real roster name
NAME_MAP = {
    "Ahmed K": "Ahmed Khan",
    "M Ali": "Ali Muhammad",
    "Fatima's Mor": "Fatima Noor",
    "Bilal H": "Bilal Hussain",
    "Hassan A": "Hassan Ahmed",
    "Zainab K": "Zainab Khan",
    "Omar S": "Omar Sheikh",
    "Yusuf M": "Yusuf Malik",
    "Ayesha R": "Ayesha Raza",
}

DUPLICATE_WINDOW_DAYS = 3

# --- Load roster (the known truth) ---
roster = {}
with open("roster.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        roster[r["Name"]] = float(r["AmountDue"])

expected_total = sum(roster.values())
print(f"--- TARGET (known correct total, hand-counted from roster) ---")
print(f"{len(roster)} students x expected dues = {expected_total:,.2f} NOK\n")

# --- Load payments exactly as received, resolve names ---
payments_by_student = defaultdict(list)
unmatched = []

with open("payments.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        raw_name = r["PayerNameAsRecorded"].strip()
        amount = float(r["Amount"])
        date = datetime.strptime(r["Date"], "%Y-%m-%d")

        resolved = NAME_MAP.get(raw_name, raw_name if raw_name in roster else None)
        if resolved is None:
            unmatched.append((raw_name, amount, date))
        else:
            payments_by_student[resolved].append((amount, date))

# --- Detect duplicates and compute amount actually counted per student ---
counted_paid = {}
duplicate_flags = []

for name, entries in payments_by_student.items():
    entries.sort(key=lambda x: x[1])
    kept = []
    for amt, date in entries:
        is_dup = any(
            amt == k_amt and abs((date - k_date).days) <= DUPLICATE_WINDOW_DAYS
            for k_amt, k_date in kept
        )
        if is_dup:
            duplicate_flags.append((name, amt, date))
        else:
            kept.append((amt, date))
    counted_paid[name] = sum(a for a, d in kept)

# --- Per-student report ---
print("--- PER-STUDENT STATUS ---")
total_still_owed = 0.0
for name, due in roster.items():
    paid = counted_paid.get(name, 0.0)
    owed = round(due - paid, 2)
    total_still_owed += max(owed, 0)
    status = "PAID IN FULL" if owed <= 0 else f"OWES {owed:,.2f} NOK"
    print(f"{name:<18} due {due:>7,.2f}  paid {paid:>7,.2f}  -> {status}")

print(f"\n--- DUPLICATE / OVERPAYMENT FLAGS ---")
if duplicate_flags:
    for name, amt, date in duplicate_flags:
        print(f"{name} paid {amt:,.2f} NOK again on {date.date()} — extra payment, not owed, possibly needs refund")
else:
    print("None found.")

print(f"\n--- UNMATCHED PAYMENTS (could not be linked to any student) ---")
if unmatched:
    for raw_name, amt, date in unmatched:
        print(f"{date.date()}  '{raw_name}'  {amt:,.2f} NOK  -- needs follow-up")
else:
    print("None found.")

# --- Final summary ---
total_received_in_account = sum(a for entries in payments_by_student.values() for a, d in entries) \
                              + sum(a for _, a, _ in unmatched)
total_counted_toward_dues = sum(counted_paid.values())

print(f"\n--- SUMMARY ---")
print(f"Expected total (roster):            {expected_total:,.2f} NOK")
print(f"Total money received in account:    {total_received_in_account:,.2f} NOK "
      f"(includes duplicates & unmatched entries)")
print(f"Total counted toward student dues:  {total_counted_toward_dues:,.2f} NOK")
print(f"Total still outstanding (owed):      {total_still_owed:,.2f} NOK")
print(f"Gap = expected - counted toward dues: {expected_total - total_counted_toward_dues:,.2f} NOK")
