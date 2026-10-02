# Review after attempting

## Key insight
Exploit sparse intersection for the numerator, but norms require all entries.

## Complexity
Expected O(m+n) time, O(1) extra space.

## Follow-up
Cache norms for repeated comparisons; discuss floating-point overflow.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
