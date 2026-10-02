# Review after attempting

## Key insight
Move the left boundary past the last duplicate, never backward.

## Complexity
Expected O(n) time, O(u) space.

## Follow-up
Allow at most k distinct event IDs.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
