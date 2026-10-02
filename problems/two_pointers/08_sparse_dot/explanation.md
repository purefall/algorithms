# Review after attempting

## Key insight
Only matching nonzero indices contribute; advance the smaller index.

## Complexity
O(m+n) time, O(1) extra space.

## Follow-up
One vector has only 100 entries and the other has a million.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
