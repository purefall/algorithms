# Review after attempting

## Key insight
Use an immutable character-frequency signature as the grouping key.

## Complexity
Expected O(total characters + number of words) time; O(total output size) space.

## Follow-up
What changes for arbitrary Unicode text?

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
