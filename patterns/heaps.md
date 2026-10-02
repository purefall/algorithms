# Heaps

Review after attempts.

## Top K Scores

Select only k extremes; explicitly define tie behavior.

O(n log(k+1)+k log(k+1)) time for 0<k<n; O(n log n) when k>=n; O(min(n,k)) space.

## Kth Largest in a Stream

The min-heap holds the k largest values seen; its root is the current kth largest.

O(n log(k+1)) time, O(k) space.

## Merge K Sorted Lists

Keep one frontier element per list; replace the consumed head with its successor.

O(k+N log(k+1)) time, O(k) auxiliary space plus output.

