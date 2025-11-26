import pytest
import sys
import os

# Correct the path to the bug_portfolio directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../bug_portfolio")))

from count_duplic_buggy import count_duplic

def test_single_element():
    assert count_duplic([5]) == ([5], [1])

def test_no_duplicates():
    assert count_duplic([1, 2, 3, 4]) == ([1, 2, 3, 4], [1, 1, 1, 1])

def test_all_same():
    assert count_duplic([7, 7, 7, 7]) == ([7], [4])

def test_mixed_simple():
    assert count_duplic([1, 1, 2, 3, 3]) == ([1, 2, 3], [2, 1, 2])

def test_alternating_values():
    # No consecutive duplicates even though values repeat
    assert count_duplic([1, 2, 1, 2, 1]) == ([1, 2, 1, 2, 1], [1, 1, 1, 1, 1])

def test_large_run_at_end():
    assert count_duplic([4, 5, 5, 5, 5]) == ([4, 5], [1, 4])

def test_negatives_and_zero():
    assert count_duplic([0, 0, -1, -1, -1, 2]) == ([0, -1, 2], [2, 3, 1])

def test_two_runs_same_value_non_consecutive():
    # Ensures function does not merge non-consecutive duplicates
    assert count_duplic([3, 3, 1, 3, 3, 3]) == ([3, 1, 3], [2, 1, 3])

def test_boundary_transition_many_small_runs():
    assert count_duplic([9, 9, 8, 8, 7, 7, 7, 6]) == ([9, 8, 7, 6], [2, 2, 3, 1])

def test_long_list_varied():
    data = [1,1,1,2,3,3,4,4,4,4,5]
    assert count_duplic(data) == ([1,2,3,4,5], [3,1,2,4,1])
