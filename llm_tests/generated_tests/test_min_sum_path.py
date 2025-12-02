import pytest
from target import min_sum_path


@pytest.mark.parametrize(
    "triangle, expected",
    [
        ([[5]], 5),  # single element
        ([[2], [3, 4]], 5),  # two rows, choose smaller child
        (
            [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
            11,  # classic example: 2 + 3 + 5 + 1
        ),
        (
            [[1], [2, 3], [4, 5, 6]],
            7,  # 1 -> 2 -> 4 is minimum
        ),
        (
            [[-1], [2, 3], [1, -1, -3]],
            -1,  # path -1 -> 3 -> -3
        ),
        (
            [[0], [0, 0], [0, 0, 0]],
            0,  # all zeros
        ),
        (
            [[5], [9, 6], [4, 6, 8], [0, 7, 1, 5]],
            18,  # minimum path sum 18
        ),
        (
            [[2], [-3, 4], [2, -5, 1], [6, 1, -1, 2]],
            -7,  # path 2 -> -3 -> -5 -> -1
        ),
        (
            [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],
            17,  # known example, minimum path
        ),
    ],
)
def test_min_sum_path(triangle, expected):
    assert min_sum_path(triangle) == expected
