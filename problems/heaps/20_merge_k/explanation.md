# Review after attempting

## Key insight
Keep one frontier element per list; replace the consumed head with its successor.

## Complexity
O(k+N log(k+1)) time, O(k) auxiliary space plus output.

## Follow-up
Return a generator to avoid storing the output.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
