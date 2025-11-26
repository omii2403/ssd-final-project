import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from find_first_occurrence_buggy import find_first_occurrence

@pytest.mark.parametrize("arr, target, expected", [
    ([1], 1, 0),                     # single element, match
    ([1], 2, -1),                    # single element, no match
    ([1, 2, 3, 4], 3, 2),            # normal case
    ([1, 2, 2, 2, 3], 2, 1),         # multiple duplicates
    ([2, 2, 2, 2], 2, 0),            # all elements same
    ([1, 3, 5, 7], 2, -1),           # target not in list
    ([1, 2, 3, 4, 5], 1, 0),         # first element
    ([1, 2, 3, 4, 5], 5, 4),         # last element
    ([0, 0, 0, 1, 1, 2], 1, 3),      # duplicates in middle
    ([10, 20, 20, 30, 40], 20, 1),   # duplicate block
    ([-5, -3, -3, -3, 0, 2], -3, 1), # negative numbers
    ([-10, -5, -2, -2, -1], -1, 4),  # last element negative
])
def test_find_first_occurrence(arr, target, expected):
    assert find_first_occurrence(arr, target) == expected
