"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""

from bisect import bisect_left


def solve(large: list[tuple[int, int]], small: list[tuple[int, int]]) -> int:
    """The idea should be searching index in the small in large ones.
    since it is sorted if an element is found the search for the next element of small in large
    should start from that index.

    Args:
        large (_type_): _description_
        small (_type_): _description_

    Raises:
        NotImplementedError: _description_
    """
    if not large or not small:
        raise ValueError("Input lists cannot be empty")
    if len(small) == 0 or len(large) == 0:
        raise ValueError("Input lists cannot be empty")

    search_span_st = 0
    search_span_end = len(large)
    dot_product = 0
    for ii, (small_index, small_val) in enumerate(small):
        found_index = bisect_left(
            large,
            small_index,
            lo=search_span_st,
            hi=search_span_end,
            key=lambda x: x[0],
        )

        # Found case
        if found_index != len(large) and large[found_index][0] == small_index:
            dot_product += large[found_index][1] * small_val

        search_span_st = found_index + 1

    return dot_product
