# Review after attempting

## Key insight
Select only k extremes; explicitly define tie behavior.

## Complexity
O(n log(k+1)+k log(k+1)) time for 0<k<n; O(n log n) when k>=n; O(min(n,k)) space.

## Follow-up
Implement the bounded heap yourself.

## Review questions
What work does the baseline repeat? Why is each update safe? Which contract assumption makes the approach valid? Explain the invariant before reading the reference code again.
