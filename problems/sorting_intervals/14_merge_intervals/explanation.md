# Review after attempting

## Key insight
Sort by start, then compare only with the current merged interval.

## Complexity
O(n log n) time, O(n) space.

## Follow-up
What changes for half-open intervals?

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
