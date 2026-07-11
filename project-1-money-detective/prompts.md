# Prompts Used — Money Detective

## Initial prompt (data + request)

> Paste my transaction data into the AI chat and ask it to write a script
> that finds recurring charges, possible forgotten subscriptions, and
> duplicate or repeated payments.

In practice, this was done conversationally: I uploaded my real bank
statement (PDF), and asked the AI to help build the Money Detective project
from the assignment.

## The Brief (refined prompt)

The AI helped me write a structured brief before generating code — see
`brief.md`. This is the "prompt" that actually drove the code generation.
Key parts of the brief that mattered most:

- **Rules section**: explicitly telling the AI that grocery stores (Kiwi,
  Extra, Obs, Europris, Rema, Normal, Lørenskog Dagli, Tenza, Snarkjøp) are
  everyday purchases, NOT subscriptions — this prevented false positives.
- **Rules section**: explicitly flagging "Til: X Betalt" transfers and named
  companies (Storebrand, Lyse Tele, Autosync, Anthropic) as the real
  recurring-charge candidates.
- **Edge cases**: two charges to the same merchant on the same day are not
  automatically duplicates unless the amount also matches.

## Verification prompt

> "Check the calculated closing balance against the balance the bank itself
> reported (10,006.43 NOK) as a known-answer test."

## Follow-up prompt (explanation)

> "Explain, step by step in plain English, what this code does, as if
> describing it to someone who can't read code."

## Result

On the first run, the code correctly reproduced the bank's exact closing
balance and correctly separated everyday purchases from real recurring
charges, requiring no further debugging iterations.
