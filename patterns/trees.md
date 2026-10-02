# Trees

Review after attempts.

## Maximum Tree Depth

Each subtree answers the same question; combine with max and add the root.

O(V) time, O(h) recursion stack.

## Tree Level Order

Snapshot the queue length to separate the current frontier from the next level.

O(V) time, O(w) auxiliary space plus output.

## Validate Strict BST

Bounds come from all ancestors; checking only parent-child pairs is insufficient.

O(V) time, O(h) stack.

## Root to Leaf Sum

Carry the remaining target; accept only at a leaf.

O(V) time, O(h) stack.

