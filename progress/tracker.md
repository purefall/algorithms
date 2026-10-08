# Progress

Ratings: 0 no approach; 1 major hint; 2 approach but incomplete code; 3 minor issue; 4 independent correct solution; 5 independent plus follow-up. Record multiple rows for retries.

| ID | Problem | Attempt/date | Minutes | Hint | Manual dry-run | Tests | Rating | Retry |
|---|---|---|---:|---|---|---|---:|---|
| 01 | Two Sum | 1 / 2026-10-02 | Not recorded | Read solution; discussed seen map | Not recorded | Not run in review | 2* | 2026-10-04–05: implement O(n) approach from scratch |
| 01b | Nearby Duplicate | 1 / 2026-10-02 | Not recorded | Prior discussion of seen maps; no implementation hint | Not recorded | 4 submitted assertions; 8,744 exhaustive small cases passed | 4 | 2026-10-04–05: explain invariant and rewrite from memory |
| 02 | Count Equal-Sum Pairs | | | | | | | |
| 03 | Customers Active Every Day | 1 / 2026-10-08 | Not recorded | Clarified example (`b` misses days 1–6); test cases supplied, no approach hint | Not recorded | 7 supplied assertions passed; fails `start=-1` edge case | 3 | 2026-10-10–11: rewrite with `len(days) == 7` check, no sum trick |
| 04 | Compact Daily Activity | | | | | | | |
| 05 | Group Anagrams | | | | | | | |
| 06 | Count Pairs Below K | | | | | | | |
| 07 | Sorted Pairs Below K | | | | | | | |
| 08 | Sparse Dot Product | | | | | | | |
| 09 | Merge Sorted Streams | | | | | | | |
| 10 | Deduplicate Sorted Array | | | | | | | |
| 11 | Peak Load and Earliest Interval | | | | | | | |
| 12 | All Peak Load Intervals | | | | | | | |
| 13 | Bounded Timestamp Peak | | | | | | | |
| 14 | Merge Closed Intervals | | | | | | | |
| 15 | Asymmetric Sparse Dot Product | | | | | | | |
| 16 | First Value at Least Target | | | | | | | |
| 17 | Minimum Daily Capacity | | | | | | | |
| 18 | Top K Scores | | | | | | | |
| 19 | Kth Largest in a Stream | | | | | | | |
| 20 | Merge K Sorted Lists | | | | | | | |
| 21 | Maximum Tree Depth | | | | | | | |
| 22 | Tree Level Order | | | | | | | |
| 23 | Validate Strict BST | | | | | | | |
| 24 | Root to Leaf Sum | | | | | | | |
| 25 | Affected Components | | | | | | | |
| 26 | Shortest Unweighted Route | | | | | | | |
| 27 | Pipeline Execution Order | | | | | | | |
| 28 | Sparse Cosine Similarity | | | | | | | |
| 29 | Longest Unique Event Window | | | | | | | |
| 30 | Count Target-Sum Windows | | | | | | | |

## Session notes — 2026-10-02

- Two Sum: wrote a correct O(n²) baseline using searches of the remaining suffix. Identified repeated searching as the cost, then understood how a dictionary of earlier values supports average O(n) time with O(n) extra space.
- *Two Sum rating 2 refers to progress toward the optimized approach: the baseline is correct, but an optimized implementation has not been submitted. The solution was consulted, so this was not an independent optimized solve.
- Nearby Duplicate: independently implemented the new exercise after the earlier discussion. Stored each value's most recent index and compared the saved previous index with the current one. Keeping the latest occurrence is sufficient because it is the closest earlier occurrence.
- Clarified that check-before-insert protects against reusing the current element. Updating first is also valid when the old index has already been saved and the comparison uses that saved index.
- Review suggestion: replace `abs(ii - last_seen_idx)` with `ii - last_seen_idx`; previous indices are always smaller. Average time O(n), worst-case space O(n).
- Next practice: fill in approach/invariant and complexity notes before coding; manually dry-run repeated values and `k = 0` before running tests. Timing and manual dry-runs were not reported today.
- Reading: [Remembering Earlier Values: a 15-minute review](../patterns/seen_maps_15_min.md).

## Session notes — 2026-10-08

- Customers Active Every Day: independently built the right structure, a dict from each customer to the set of in-window days, with sorted output. All 7 supplied assertions passed.
- Minor issue: completeness was checked with `sum(days) == arithmetic-series sum` instead of `len(days) == 7`. A sum only identifies the full set when every term is positive; the `+1` shift covers `start = 0` but not a window that spans zero. Counterexample: `solve([('a', d) for d in range(0, 6)], -1)` returns `['a']` but should return `[]`, because day -1 shifts to 0 and adds nothing to the sum.
- Cleanup notes: use `//` rather than `/` (float); drop the unused `enumerate` index; check once at the end instead of re-summing per log; `setdefault(c, set()).add(d)` replaces get-then-store; `LOYALITY_DURATION = 6` invites an off-by-one because the window holds 7 days.
- Lesson: to test "does this set contain all N items?", filter to valid items and compare `len(...) == N`. Avoid checksums like sums.
- Clarifications/baseline/complexity docstring in `attempt.py` left blank again. Fill it before coding next time.
