"""
Clarifications:
Baseline:
Approach and invariant:
Time:
Space:
Manual dry-run:
"""


def solve(a: list, b: list) -> int:

    index_dict = {}
    sparse_product = 0
    max_len = max(len(a), len(b))

    for ii in range(max_len):
        if ii < len(a):
            matrix_index = a[ii][0]
            index_dict.setdefault(matrix_index, []).append(a[ii][1])

        if ii < len(b):
            matrix_index = b[ii][0]
            index_dict.setdefault(matrix_index, []).append(b[ii][1])
    for ii, elem in index_dict.items():
        if len(elem) == 2:
            sparse_product += elem[0] * elem[1]
    return sparse_product


assert solve([(1, 3), (5, 2), (100, 4)], [(1, 2), (3, 7), (100, 5)]) == 26
assert solve([(2, 4)], [(2, 5)]) == 20
assert solve([(1, 3)], [(2, 5)]) == 0
assert solve([], [(1, 2)]) == 0
assert solve([(0, -2)], [(0, 3)]) == -6
assert solve([(1, 2), (2, 3), (3, 4)], [(3, 10)]) == 40
assert solve([(1, 5), (9, 1)], [(2, 7), (3, 7), (4, 7), (9, 2)]) == 2
assert solve([(4, 0)], [(4, 9)]) == 0
print("All is well!")
