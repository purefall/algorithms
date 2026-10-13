# Sorting as a Tool

A 15-minute review based on your peak-load work (#11, #11b). Spend about 10 minutes reading and 5 minutes working through the questions with a pen.

In interviews you almost never write a sorting algorithm. You **call** one, and the skill is knowing what to sort, by which key, and what the sorted order lets you do next.

## Minutes 0–3: The Python toolkit

```python
nums = [5, 1, 4]
sorted(nums)     # [1, 4, 5]  new list; nums unchanged
nums.sort()      # sorts nums in place, returns None
```

`sorted()` accepts any iterable and always returns a list:

```python
sorted({5: 'a', 1: 'b'})       # [1, 5]      a dict iterates its keys
sorted("cab")                  # ['a', 'b', 'c']
sorted({3, 1, 2})              # [1, 2, 3]
```

A common bug is `x = nums.sort()`, which sets `x` to `None`.

Both run Timsort: O(n log n) time in the worst case, O(n) extra space, and close to O(n) on input that is already nearly sorted.

## Minutes 3–7: Keys, tuples and ties

`key=` tells Python what to compare. It is called once per element:

```python
words = ["bb", "a", "ccc"]
sorted(words, key=len)                       # ['a', 'bb', 'ccc']
jobs = [(1, 5, 2), (3, 8, 4)]
sorted(jobs, key=lambda j: j[2])             # by memory
```

Tuples compare element by element, left to right. That gives you multi-key sorting for free:

```python
sorted([(2, 'b'), (1, 'z'), (2, 'a')])       # [(1, 'z'), (2, 'a'), (2, 'b')]
```

To sort one key ascending and another descending, negate the numeric one:

```python
scores = [("ann", 90), ("bob", 95), ("cid", 90)]
sorted(scores, key=lambda s: (-s[1], s[0]))  # highest score first, then name A→Z
# [('bob', 95), ('ann', 90), ('cid', 90)]
```

`reverse=True` flips the whole order. It cannot reverse just one key.

**Stability:** Python's sort keeps elements with equal keys in their original order. That means you can sort in two passes, secondary key first:

```python
people = sorted(people, key=lambda p: p.name)  # secondary
people = sorted(people, key=lambda p: p.age)   # primary; names stay A→Z within an age
```

**Ties carry meaning in interval problems.** If you sort `(time, delta)` events as tuples, `(4, -1)` comes before `(4, +1)`, so ends are processed before starts at the same time. That is the right rule for half-open intervals. Your `Counter` version avoided the issue entirely by summing every delta at the same time first.

## Minutes 7–10: Why sort at all?

Sorting costs O(n log n). Pay it when the order makes the rest of the algorithm cheap:

| After sorting, you can… | Problems in this repo |
| --- | --- |
| Walk two pointers from each end or side by side | #07 Sorted Pairs Below K, #08 Sparse Dot |
| Sweep events in time order with a running total | #11, #11b, #12 |
| Compare each interval only with the last merged one | #14 Merge Intervals |
| Find things with binary search | #15, #16, #17 |
| Bring equal items next to each other | #05 Group Anagrams (`sorted(word)` as the key) |

The question to ask: **would this be easy if the input were in order?** If yes, and the input isn't already sorted, an O(n log n) sort followed by an O(n) pass is often the intended answer.

When *not* to sort:
- A hash map already gives O(n) (#01 Two Sum: sorting would lose the original indices).
- You only need the top k of n items: a heap gives O(n log k) (#18).
- The values come from a small range: see the next section.

## Minutes 10–12: Beating O(n log n) when values are small

O(n log n) is the limit only for sorts that compare elements. When the keys are integers in a small range `0..T`, you can count them instead:

```python
def counting_sort(nums, T):
    count = [0] * (T + 1)
    for x in nums:
        count[x] += 1
    return [x for x in range(T + 1) for _ in range(count[x])]
```

That's O(n + T) time and O(T) space. #13 Bounded Timestamp Peak uses the same idea: a difference array indexed by time replaces sorting the events.

## Minutes 12–15: Recall and explain

Try these without looking back.

1. What does `x = [3, 1, 2].sort()` set `x` to? Why?
2. What does `sorted({"b": 1, "a": 2})` return?
3. Write a `key` that sorts `(name, age)` pairs by age descending, then name ascending.
4. Sort the events `[(4, +1), (2, +1), (4, -1)]` as tuples. In what order do the two time-4 events come out, and why does that matter for half-open intervals?
5. Two Sum can be solved by sorting plus two pointers. What does that version lose compared with the dictionary version?
6. You need the 3 largest of 10 million scores. Why not sort?
7. Say this aloud in your own words: “Sorting by ____ lets me ____, so the total is O(____) instead of O(____).”

### Check your answers after trying

1. `None`. `.sort()` works in place and returns nothing.
2. `['a', 'b']`. Iterating a dict yields its keys.
3. `key=lambda p: (-p[1], p[0])`.
4. `[(2, 1), (4, -1), (4, 1)]`. The end comes before the start, so a handoff at time 4 never counts as an overlap.
5. The original indices (unless you sort `(value, index)` pairs), and it takes O(n log n) instead of O(n) average.
6. A size-3 min-heap takes O(n log 3), which is effectively O(n). Sorting does O(n log n) work to order 9,999,997 values you don't need.
7. For #14: “Sorting by start lets me compare each interval only with the last merged one, so the total is O(n log n) instead of O(n²).”

Next step: solve #14 Merge Closed Intervals. It's the cleanest "sort first, then one pass" problem in the repo.
