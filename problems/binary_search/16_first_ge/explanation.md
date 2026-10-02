# Review after attempting

## Key insight
Maintain a half-open search range; the first feasible index remains in [lo, hi].

## Complexity
O(log(n+1)) time, O(1) space.

## Follow-up
Return the first value strictly greater than target.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
