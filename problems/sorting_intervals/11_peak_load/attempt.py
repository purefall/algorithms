"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""

from collections import Counter


def solve_old(sessions: list) -> tuple(int, tuple(int, int)):

    # Drop zero lengths
    sessions = [(s, e) for s, e in sessions if e > s]

    points = sorted({t for s, e in sessions for t in (s, e)})

    counts = [sum(1 for t in points[:-1] for s, e in sessions if s <= t < e)]

    peak_count = max(counts)
    peak_index = counts.index(peak_count)
    stretch_end_index = peak_index
    while stretch_end_index < len(counts) and counts[stretch_end_index] == peak_count:
        stretch_end_index += 1

    return peak_count, (points[peak_index], points[stretch_end_index])


def solve(sessions: list) -> tuple(int, tuple(int, int)):
    sessions = [(s, e) for s, e in sessions if s < e]  # drop zero-length
    if not sessions:
        return (0, None)
    delta = Counter()
    for s, e in sessions:
        delta[s] += 1
        delta[e] -= 1
    points = sorted(delta)

    counts, cur_count = []

    for ii, point in enumerate(points):
        cur_count += delta[point]

        counts.append(cur_count)

    max_count = max(counts)
