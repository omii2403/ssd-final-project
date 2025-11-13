import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from sort_by_dnf_buggy import sort_by_dnf

@pytest.mark.parametrize("arr, n, expected", [
    # Basic cases
    ([0], 1, [0]),
    ([1], 1, [1]),
    ([2], 1, [2]),

    # All identical values
    ([0, 0, 0], 3, [0, 0, 0]),
    ([1, 1, 1], 3, [1, 1, 1]),
    ([2, 2, 2], 3, [2, 2, 2]),

    # Already sorted
    ([0, 1, 2], 3, [0, 1, 2]),
    ([0, 0, 1, 1, 2, 2], 6, [0, 0, 1, 1, 2, 2]),

    # Reverse sorted
    ([2, 2, 1, 1, 0, 0], 6, [0, 0, 1, 1, 2, 2]),

    # Edge cases with missing values
    ([0, 1, 1, 0], 4, [0, 0, 1, 1]),
    ([2, 1, 2, 1], 4, [1, 1, 2, 2]),
    ([0, 2, 0, 2], 4, [0, 0, 2, 2]),

    # Larger variety but still small enough
    ([2, 0, 2, 1, 0, 1, 2, 0], 8, [0, 0, 0, 1, 1, 2, 2, 2]),
])
def test_sort_by_dnf(arr, n, expected):
    result = sort_by_dnf(arr, n)
    assert result == expected
