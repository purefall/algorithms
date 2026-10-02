# Binary Search

Review after attempts.

## Asymmetric Sparse Dot Product

Binary-search directly into the larger vector for each smaller-vector index.

O(s log(L+1)) time, O(1) extra space.

## First Value at Least Target

Maintain a half-open search range; the first feasible index remains in [lo, hi].

O(log(n+1)) time, O(1) space.

## Minimum Daily Capacity

Feasibility is monotonic in capacity; binary-search the answer, not an array.

O(n log(S-M+1)) time for sum S and max M; O(1) space.

