# Two Pointers

Review after attempts.

## Count Pairs Below K

Sorting makes every partner up to right valid when the largest partner is valid.

O(n log n) time, O(n) space for the sorted copy.

## Sorted Pairs Below K

Each pointer movement eliminates a whole family of candidate pairs.

O(n) time, O(1) extra space.

## Sparse Dot Product

Only matching nonzero indices contribute; advance the smaller index.

O(m+n) time, O(1) extra space.

## Merge Sorted Streams

The next output is the smaller of the two unconsumed heads.

O(m+n) time and output space.

## Deduplicate Sorted Array

The write pointer records the accepted prefix; it never overtakes the read position.

O(n) time, O(1) extra space.

