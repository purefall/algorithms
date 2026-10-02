# Review after attempting

## Key insight
The write pointer records the accepted prefix; it never overtakes the read position.

## Complexity
O(n) time, O(1) extra space.

## Follow-up
Allow each value to occur at most twice.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
