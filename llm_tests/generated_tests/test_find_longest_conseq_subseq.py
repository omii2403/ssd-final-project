import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from find_longest_conseq_subseq_buggy import find_longest_conseq_subseq


@pytest.mark.parametrize(
    "arr, n, expected",
    [
        ([5], 1, 1),  # single element
        ([1, 2, 3, 4], 4, 4),  # simple increasing consecutive sequence
        ([2, 6, 1, 9, 4, 5, 3], 7, 6),  # classic example: longest is 1..6
        ([1, 2, 2, 3], 4, 3),  # duplicates inside a consecutive run
        ([10, 30, 20], 3, 1),  # no two elements consecutive
        ([-1, 0, 1, 2, 4, 5], 6, 4),  # includes negatives, longest is -1..2
        ([1, 3, 5, 7], 4, 1),  # all non-consecutive, multiple isolated elements
        ([100, 4, 200, 1, 3, 2], 6, 4),  # longest subsequence 1..4 in unsorted array
        ([8, 5, 9, 7, 6, 6, 10], 7, 6),  # 5..10 with a duplicate 6
        ([0, 0, 0, 0], 4, 1),  # all elements identical
        ([-3, -2, -2, -1, 0, 2, 3], 7, 4),  # longest -3..0 with duplicate -2
        ([1, 2, 3, 10, 11, 12, 13], 7, 4),  # two runs, second is longer
    ],
)
def test_find_longest_conseq_subseq(arr, n, expected):
    assert find_longest_conseq_subseq(arr, n) == expected
