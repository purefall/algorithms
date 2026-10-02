# Review after attempting

## Key insight
Build forward edges and mark discovered nodes immediately to prevent repeated work and cycles.

## Complexity
O(E+R+R log R) time including sorted output; O(V+E) space.

## Follow-up
Return a valid recomputation order for an acyclic graph.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
