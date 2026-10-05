# Remembering Earlier Values

A 15-minute review based on your Two Sum and Nearby Duplicate attempts. Spend about 10 minutes reading and 5 minutes working through the questions with a pen.

## Minutes 0–3: Find the repeated work

Your first Two Sum approach was valid: for each number, calculate its complement and search the remaining list. Restricting the search to later positions ensures that the two indices are distinct.

For example, with `[2, 7, 11]` and target `9`, the complement of `2` is `7`. Finding `7` after index 0 gives the pair `(0, 1)`.

The cost comes from repeating that search. With n elements, you might inspect roughly n−1 remaining values, then n−2, then n−3, and so on. The total is:

```text
(n−1) + (n−2) + ... + 1 = n(n−1)/2
```

That is O(n²). In Python, `nums[i + 1:]` also creates a new list, while membership and `.index()` scan that list. Your code can scan a matching suffix twice. Removing slices would reduce copying but would not change the quadratic search pattern.

The useful optimization question is: **What am I repeatedly searching for, and could I store information that makes that search cheap?**

A dictionary maps a key to information about it. Python dictionary lookup and insertion take O(1) time on average. This lets us trade extra memory for fewer searches.

## Minutes 3–6: Store exactly what the question needs

Before choosing a container, identify what you need to retrieve.

| Question about earlier elements | Useful stored state |
| --- | --- |
| Has this value appeared? | Set of values |
| Where did this value appear? | Dictionary: value → index |
| How often has it appeared? | Dictionary: value → count |

Two Sum asks for indices, so a set alone is insufficient. We need the index of an earlier complement:

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None
```

Before processing index `i`, the dictionary contains information only about positions before `i`. That statement is the **loop invariant**: a fact that remains true whenever the loop reaches the same point.

Why does this find any existing pair? Suppose a valid pair has indices `a < b`. When we reach `b`, the value at `a` has already been stored. The lookup for the complement therefore succeeds. If its index was overwritten by another occurrence of the same value, that occurrence also forms a valid pair with `b`.

The algorithm visits each element once and performs a constant number of dictionary operations per visit: O(n) average time and O(n) space in the worst case.

## Minutes 6–8: Understand the order of operations

For Two Sum, inserting the current number before looking up its complement can accidentally match the number with itself. With `[3]` and target `6`, storing `{3: 0}` first would make the complement lookup return index 0, producing the invalid pair `(0, 0)`.

Checking first avoids this. With `[3, 3]`, target `6`, the first occurrence is stored and the second finds it.

Your Nearby Duplicate implementation uses another valid order:

```python
previous = last_seen.get(num, -1)
last_seen[num] = i
if previous >= 0 and i - previous <= k:
    return True
```

You saved the old index before overwriting it. The condition uses `previous`, not the newly stored index, so it still compares two different positions.

The underlying rule is: **make the decision using the appropriate earlier state.** Check-before-insert is one clear way to enforce it, but saving the earlier state also works.

Your `-1` sentinel is safe because valid list indices are nonnegative. Be careful with `if previous:`: index 0 is false in Python, even though it is a valid previous position. Use an explicit condition such as `previous >= 0`.

## Minutes 8–10: Why the latest index matters

Nearby Duplicate adds a distance constraint. If a value has appeared several times, which index should you retain?

For a current index `i` and earlier indices `a < b < i`:

```text
i - b < i - a
```

The latest occurrence is the closest. If even that occurrence is too far away, every older occurrence is too far away. If it is close enough, you already have a valid pair. This explains why one index per value is sufficient.

Consider `[8, 2, 8, 8]` with `k = 1`:

| Current index | Value | Previous index | Distance | Action |
| --- | --- | --- | --- | --- |
| 0 | 8 | None | — | Store 8 → 0 |
| 1 | 2 | None | — | Store 2 → 1 |
| 2 | 8 | 0 | 2 | Too far; update 8 → 2 |
| 3 | 8 | 2 | 1 | Return True |

If you retained only the first occurrence of `8`, you would miss the adjacent pair at indices 2 and 3. Updating after a failed distance check is therefore essential.

Its invariant is: **before each iteration, each stored value maps to its most recent index in the already processed prefix.** At the end of an unsuccessful iteration, updating the current value makes that invariant true for the next iteration.

## Minutes 10–15: Recall and explain

Try these without looking back. Explain the state and its meaning before writing any code.

1. Dry-run Two Sum on `[4, 4]` with target `8`. What is in `seen` before each iteration?
2. Why must Two Sum on `[4]` with target `8` return `None`?
3. Dry-run Nearby Duplicate on `[1, 2, 1, 1]` with `k = 1`. Which update makes the final match possible?
4. Why does Nearby Duplicate always return `False` when `k = 0`?
5. If the question asked only whether a list contains any duplicate, what information could you stop storing?
6. Say this aloud in your own words: “My baseline repeatedly ____. I can remember ____ using ____. Before each iteration, ____. This gives ____ time and ____ space.”

### Check your answers after trying

1. Initially `{}`; before index 1, `{4: 0}`. The second 4 finds the first.
2. A single position cannot supply two distinct indices.
3. At index 2, update the stored index of 1 from 0 to 2. At index 3, the distance to 2 is 1.
4. Distinct indices are at least one position apart.
5. Indices: a set of encountered values is enough.
6. For Nearby Duplicate: repeatedly search for nearby equal values; remember the latest index of each value; use a dictionary; store the latest indices from the processed prefix; O(n) average time and O(n) worst-case space.

For your next attempt, write the invariant before coding. It tells you what the dictionary means, which order of operations is safe, and which information you must update.
