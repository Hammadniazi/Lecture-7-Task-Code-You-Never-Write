# Prompts Used — The Books Don't Match

## Initial prompt
> "State your expected total up front so the AI knows the target the
> records should add up to. Provide the payment records exactly as you
> received them, without cleaning them up first."

## The Brief (refined prompt)
See `brief.md`. Key parts that mattered most:
- **Rules**: an explicit name-mapping table translating nicknames/initials
  to real roster names — this personal knowledge is the whole reason a
  generic app couldn't do this.
- **Rules**: explicitly stating that "Fatima's Mor" (a parent's account)
  should count as Fatima's own payment.
- **Edge cases**: partial payments are NOT paid-in-full; duplicates count
  once toward dues but get flagged separately; anything unmatched must be
  flagged, never silently assigned.

## Verification prompt
> "State the expected total up front (18,000 NOK from my roster) before
> processing anything, so I can check the code's math against a number I
> already know is correct."

## Follow-up prompt
> "Show me the gap between the expected total and what's actually been
> collected, broken down by student, so I can hand-check the final number."

## Result
The code correctly resolved all nine name-mapping rules, correctly flagged
the one duplicate payment and the one unmatched entry, and its final
outstanding-balance figure matched my own hand calculation exactly on the
first run.
