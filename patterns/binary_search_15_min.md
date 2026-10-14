# Binary Search for Interviews

A 15-minute review to read before #16, #17 and #15. Spend about 10 minutes reading and 5 minutes working through the questions with a pen.

Binary search has one idea and many off-by-one traps. The cure is to learn **one template** and turn every problem into it, instead of improvising `<` vs `<=` and `mid ± 1` each time.

## Minutes 0–3: The one question binary search answers

Forget "find the target". Binary search answers:

> In a sequence that goes `False, False, …, False, True, True, …, True`, where is the **first True**?

The only requirement is that the condition is **monotonic**: once it becomes true, it stays true. Sorted order is just one way to get that.

```text
nums:        [1, 2, 2, 4]      target = 2
nums[i] >= 2: F  T  T  T        → first True at index 1
```

Every interview variant is this question with a different condition:

| You want | Condition to search for | Answer |
| --- | --- | --- |
| First index with value ≥ target (#16) | `nums[i] >= target` | first True |
| First index with value > target | `nums[i] > target` | first True |
| Last index with value ≤ target | `nums[i] > target` | first True − 1 |
| Does target exist? | `nums[i] >= target` | first True `i`, then check `nums[i] == target` |
| Smallest capacity that works (#17) | `can_ship(capacity)` | first True over capacities |

## Minutes 3–7: The template

```python
def first_true(lo, hi, cond):
    """Smallest x in [lo, hi) with cond(x) True, or hi if none."""
    while lo < hi:
        mid = (lo + hi) // 2
        if cond(mid):
            hi = mid          # mid might be the answer; keep it
        else:
            lo = mid + 1      # mid is definitely not the answer
    return lo
```

**Invariant:** the answer always lies in `[lo, hi]`. Everything before `lo` is known False; everything from `hi` on is known True, or past the end.

Why it can't loop forever: `mid` is always strictly less than `hi`, so `hi = mid` shrinks the range, and `lo = mid + 1` shrinks it too. The loop ends when `lo == hi`, at the first True.

Why `hi` starts at `len(nums)`, not `len(nums) - 1`: "no element qualifies" needs an answer too, and `len(nums)` is it. That's exactly what #16 asks for.

**Dry-run** with `nums = [1, 2, 2, 4]` and `cond = nums[i] >= 2`:

| lo | hi | mid | nums[mid] | cond | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 4 | 2 | 2 | T | hi = 2 |
| 0 | 2 | 1 | 2 | T | hi = 1 |
| 0 | 1 | 0 | 1 | F | lo = 1 |
| 1 | 1 | — | — | — | return 1 |

Cost: the range halves each step, so O(log n) time and O(1) space.

### The same thing written directly on a list

Without the `cond` function, this is what you'd write on a whiteboard. It does exactly what `bisect_left` does:

```python
def lower_bound(nums, target):
    """First index with nums[i] >= target, or len(nums) if none."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

And the classic "is it there?" search, built on top of it:

```python
def find(nums, target):
    """Index of target in sorted nums, or -1 if absent."""
    i = lower_bound(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

`find([1, 2, 2, 4], 2)` returns `1` and `find([1, 2, 2, 4], 3)` returns `-1`. With duplicates it always returns the **first** occurrence, which a hand-rolled "stop as soon as `nums[mid] == target`" version does not guarantee.

For the `>` variant (`bisect_right`), change only the condition to `nums[mid] > target`.

## Minutes 7–9: Python's `bisect` does this for you

```python
from bisect import bisect_left, bisect_right

nums = [1, 2, 2, 4]
bisect_left(nums, 2)    # 1  first index with nums[i] >= 2
bisect_right(nums, 2)   # 3  first index with nums[i] >  2
bisect_left(nums, 5)    # 4  not found → len(nums)
```

Two extras that matter for #15:

```python
pairs = [(1, 3), (5, 2), (100, 4)]
bisect_left(pairs, 5, key=lambda p: p[0])          # 1  search on the index part, no copy (Python 3.10+)
bisect_left(pairs, 5, lo=1, key=lambda p: p[0])    # start the search from position 1
```

`key=` compares only the index part of each pair, so you never build a separate list of indices. `lo=` lets the next search skip what you've already passed.

In an interview, say which one you're using: write the template when they want to see binary search, and use `bisect` when the search is only one step of a bigger problem.

## Minutes 9–12: Searching for the answer, not in an array

In #17 there is no sorted list to search. What *is* monotonic is feasibility:

```text
capacity:      ...  7   8   9   10  11  ...
can_ship(c):        F   F   T   T   T
```

If capacity `c` works, any larger capacity works too. So binary-search the **capacity**:

1. **Range:** the smallest capacity that could possibly work, and the largest you'd ever need. Think about which weight you can never split across days, and which capacity ships everything in one day.
2. **Condition:** a greedy check, `can_ship(c)`, that packs each day as full as possible and counts the days. That's O(n).
3. **Answer:** `first_true(lo, hi + 1, can_ship)`.

Total: O(n log(range)). The skill being tested is noticing the monotonic condition. Phrases like *minimum X such that…* and *maximum X such that…* are the cue.

## Minutes 12–15: Recall and explain

Try these without looking back.

1. In the template, why is it `hi = mid` but `lo = mid + 1`?
2. What does `first_true` return when the condition is False everywhere? When it's True everywhere?
3. Using only `bisect_left` and `bisect_right`, count how many times `target` appears in a sorted list.
4. Find the last index with `nums[i] <= target`. Which condition do you search for, and what do you return?
5. What breaks if you write `while lo <= hi` with `hi = mid`?
6. For #17 with weights `[1, 2, 3, 4, 5]`: what are the smallest and largest capacities worth trying?
7. Say this aloud in your own words: "The condition ____ is monotonic because ____. The answer is the first True in ____, so the cost is O(____)."

### Check your answers after trying

1. When `cond(mid)` is True, `mid` might be the first True, so you keep it. When it's False, `mid` can't be the answer, so you skip past it.
2. All False: `hi`, the "not found" value. All True: the starting `lo`.
3. `bisect_right(nums, target) - bisect_left(nums, target)`.
4. Search for the first `nums[i] > target` (that's `bisect_right`) and return that index − 1. A result of −1 means no element qualifies.
5. Once `lo == hi`, `mid == hi`, and `hi = mid` changes nothing, so the loop runs forever.
6. Smallest: 5, the heaviest single weight, which can't be split. Largest: 15, the total, which ships everything in one day.
7. For #16: "The condition `nums[i] >= target` is monotonic because the list is sorted. The answer is the first True in `[0, len(nums))`, so the cost is O(log n)."

Next step: solve #16 with the template from memory, then #17 (write `can_ship` first and test it on its own), then come back to #15.
