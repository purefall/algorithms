# Arrays Hashing

Review after attempts.

## Two Sum

Store prior indices; lookup the complement before inserting the current value.

Expected O(n) time, O(n) space.

## Count Equal-Sum Pairs

A frequency map counts all earlier matching elements, including duplicates.

Expected O(n) time, O(n) space.

## Customers Active Every Day

Filter to the target window before counting unique days.

Expected O(n+c log c) time including output sorting; O(c) space for a fixed seven-day window.

## Compact Daily Activity

OR makes repeated visits idempotent; all seven bits must be set.

Expected O(n+c log c) time; O(c) space.

## Group Anagrams

Use an immutable character-frequency signature as the grouping key.

Expected O(total characters + number of words) time; O(total output size) space.

