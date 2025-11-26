import pytest
import math
import sys
import os

# Correct the path to the bug_portfolio directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../bug_portfolio")))

from count_Pairs_buggy import count_Pairs

@pytest.mark.parametrize("arr, n, expected", [
    # No pairs
    ([], 0, 0),
    ([1], 1, 0),
    ([1, 2, 3], 3, 0),

    # Single pair
    ([1, 1], 2, 1),

    # Multiple pairs, same element
    ([1, 1, 1, 1], 4, 6),          # 4C2 = 6
    ([2, 2, 2], 3, 3),             # 3C2 = 3

    # Mixed values
    ([1, 2, 1, 2], 4, 2),          # pairs: (1s → 1), (2s → 1)
    ([3, 3, 3, 1], 4, 3),          # only 3s → 3 pairs

    # Larger mixed case
    ([5, 5, 1, 1, 5], 5, 4),       # 5s → 3 pairs, 1s → 1 pair

    # Negative numbers
    ([-1, -1, 2, -1], 4, 3),       # -1 appears 3 times → 3 pairs

    # Non-consecutive duplicates
    ([7, 8, 7, 9, 7], 5, 3),       # 7 appears 3 times
])
def test_count_Pairs(arr, n, expected):
    assert count_Pairs(arr, n) == expected
