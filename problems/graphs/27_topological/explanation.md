# Review after attempting

## Key insight
Remove zero-indegree nodes; remaining nodes indicate a cycle. Deduplicate edges consistently.

## Complexity
O(E+V log(V+1)) time, O(V+E) space.

## Follow-up
Compute parallel execution layers instead.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
