# Review after attempting

## Key insight
OR makes repeated visits idempotent; all seven bits must be set.

## Complexity
Expected O(n+c log c) time; O(c) space.

## Follow-up
Partition a log that does not fit in memory by customer.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
