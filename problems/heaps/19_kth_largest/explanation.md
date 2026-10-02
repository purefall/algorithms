# Review after attempting

## Key insight
The min-heap holds the k largest values seen; its root is the current kth largest.

## Complexity
O(n log(k+1)) time, O(k) space.

## Follow-up
Expose a class with add() and query() methods.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
