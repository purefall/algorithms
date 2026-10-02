# Review after attempting

## Key insight
Snapshot the queue length to separate the current frontier from the next level.

## Complexity
O(V) time, O(w) auxiliary space plus output.

## Follow-up
Return the rightmost value at each level.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
