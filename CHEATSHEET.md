# Mental models

Spend 60–90 seconds establishing the contract. Ask 1–3 questions that affect the answer: duplicates? sorted? endpoint semantics? mutation? output order?

| Signal | Ask | Candidate approach |
|---|---|---|
| Repeated membership or counting | Can I retain prior work? | Hash set / frequency map |
| Pair inequality | Does ordering let me count a whole range? | Sorting + two pointers |
| Sorted sequence lookup | Can I eliminate half the range? | Binary search |
| Very unequal sorted input sizes | Must I scan the large input? | Search per small-input element |
| Events change concurrent state | What changes at each timestamp? | Sweep line / difference array |
| Only k extremes matter | Do I need a complete ordering? | Bounded heap |
| Hierarchy | What answer can a child return? | Recursive DFS |
| Reachability | What are nodes and edges? | DFS / BFS + visited |
| Unweighted shortest path | Can I expand one distance layer at a time? | BFS |
| Monotonic feasibility | Can I binary-search the answer? | Feasibility predicate |
| Contiguous sequence | What makes a window invalid? | Sliding window |
| Subarray sums with negatives | Can prefixes encode all prior starts? | Prefix sums + frequency map |

## Say your invariant
Two pointers: which pairs are still undecided?
Binary search: which interval can still contain the answer?
Heap: what exactly does the heap retain?
BFS: when is a node marked visited?
Sweep: does active describe before or after all events at t?

## Sanity-check aloud
Empty input; singleton; duplicates; equality boundary; negative values if allowed; disconnected/cyclic graph; tied scores; simultaneous login/logout. Check return type and input mutation.

## Complexity honesty
Include sorting and output construction. Python sorted() copies the input and sorting can use extra memory. Hash lookup is expected constant time, not worst-case guaranteed. Recursion costs stack space. Building a graph costs time even when reachability is small.
