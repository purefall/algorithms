# Mixed

Review after attempts.

## Sparse Cosine Similarity

Exploit sparse intersection for the numerator, but norms require all entries.

Expected O(m+n) time, O(1) extra space.

## Longest Unique Event Window

Move the left boundary past the last duplicate, never backward.

Expected O(n) time, O(u) space.

## Count Target-Sum Windows

A subarray sum is the difference of two prefixes; count prior complementary prefixes.

Expected O(n) time, O(n) space.

