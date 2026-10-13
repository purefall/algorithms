"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""

from collections import Counter


def solve(jobs: list[tuple[int, int, int]]) -> tuple[int, tuple[int, int]] | None:

    if not jobs:
        return (0, None)

    jobs = [(s, e, m) for (s, e, m) in jobs if e > s]

    delta_mem = Counter()

    for s, e, m in jobs:
        delta_mem[s] += m
        delta_mem[e] -= m

    points = sorted(delta_mem)

    cur_rolling_mem = 0
    mem_list_per_pt = []

    for pt in points:
        cur_rolling_mem += delta_mem[pt]
        mem_list_per_pt.append(cur_rolling_mem)

    max_memory = max(mem_list_per_pt)
    max_memory_index = mem_list_per_pt.index(max_memory)
    max_memory_session_end_idx = max_memory_index
    while (
        max_memory_session_end_idx < len(points)
        and mem_list_per_pt[max_memory_session_end_idx] == max_memory
    ):
        max_memory_session_end_idx += 1

    return max_memory, (points[max_memory_index], points[max_memory_session_end_idx])
