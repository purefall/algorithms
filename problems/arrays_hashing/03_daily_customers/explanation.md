# Review after attempting

## Key insight
Filter to the target window before counting unique days.

## Complexity
Expected O(n+c log c) time including output sorting; O(c) space for a fixed seven-day window.

## Follow-up
Replace the per-customer sets with a bit mask.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
