# Review after attempting

## Key insight
Feasibility is monotonic in capacity; binary-search the answer, not an array.

## Complexity
O(n log(S-M+1)) time for sum S and max M; O(1) space.

## Follow-up
What changes if packages may be reordered?

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
