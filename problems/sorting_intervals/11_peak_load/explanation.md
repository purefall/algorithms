# Review after attempting

## Key insight
Aggregate simultaneous events before assessing load between timestamps; merge adjacent equal-peak spans.

## Complexity
O(n log n) time, O(n) space.

## Follow-up
Return all maximal peak intervals.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
