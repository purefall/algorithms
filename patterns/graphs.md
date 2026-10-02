# Graphs

Review after attempts.

## Affected Components

Build forward edges and mark discovered nodes immediately to prevent repeated work and cycles.

O(E+R+R log R) time including sorted output; O(V+E) space.

## Shortest Unweighted Route

BFS visits vertices in nondecreasing distance in an unweighted graph.

O(V+E) time and space.

## Pipeline Execution Order

Remove zero-indegree nodes; remaining nodes indicate a cycle. Deduplicate edges consistently.

O(E+V log(V+1)) time, O(V+E) space.

