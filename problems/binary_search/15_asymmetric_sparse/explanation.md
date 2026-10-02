# Review after attempting

## Key insight
Binary-search directly into the larger vector for each smaller-vector index.

## Complexity
O(s log(L+1)) time, O(1) extra space.

## Follow-up
Compare against a prebuilt hash map for repeated queries.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
