# Brief: The Books Don't Match — Class Trip Fund

## Goal
Reconcile the money that should have been collected for the class trip
(hand-counted expected total, based on my roster) against the messy digital
payment record, so I know exactly who still owes money, who's paid in full,
and which entries are unexplained.

## Input
Two files, provided exactly as received (not cleaned up):
- `roster.csv`: Name, AmountDue — my known-correct list of 12 students, each
  owing 1500 NOK. Expected total: 18,000 NOK.
- `payments.csv`: Date, PayerNameAsRecorded, Amount — the digital transfer
  record, with inconsistent name formatting (nicknames, initials, and one
  payment made from a parent's account).

## Output
1. State the target total up front (18,000 NOK) before processing anything.
2. For each student on the roster: amount paid so far, amount still owed
   (0 if paid in full).
3. Any payment in the digital record that could NOT be matched to a student
   on the roster — list separately for follow-up.
4. Any duplicate payment (same payer, same amount, on nearby dates) — flag
   it, but only count it once toward that student's dues.
5. A final summary: total collected, total still outstanding, and the gap
   between the expected total and what's actually been collected.

## Rules (my personal knowledge of who's who)
- "Ahmed K" = Ahmed Khan
- "M Ali" = Ali Muhammad (name written in reversed/short order)
- "Fatima's Mor" = a payment made by Fatima Noor's mother, on Fatima's
  behalf — count it as Fatima Noor's payment
- "Bilal H" = Bilal Hussain
- "Hassan A" = Hassan Ahmed
- "Zainab K" = Zainab Khan
- "Omar S" = Omar Sheikh
- "Yusuf M" = Yusuf Malik
- "Ayesha R" = Ayesha Raza
- Any name in the payment record that does NOT match one of the above
  mappings or an exact roster name (e.g. "Karim Store AS") is NOT a student
  payment — flag it as unmatched, do not assign it to anyone.

## Edge cases
- A payment smaller than the amount due (e.g. Bilal's 750) is a PARTIAL
  payment — the remaining balance is still owed, not treated as paid in
  full or as an error.
- Two payments from the same matched student, same amount, on nearby dates:
  treat as a duplicate/overpayment — count only one toward dues, and
  flag the extra amount separately (it may need to be refunded or was a
  mistaken double-transfer).
- A student on the roster with NO matching payment at all: full amount
  still owed.
