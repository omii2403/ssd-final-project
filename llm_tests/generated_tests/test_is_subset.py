import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from is_subset_buggy import is_subset


def test_basic_true():
    assert is_subset([1, 2, 3, 4, 5], 5, [2, 3], 2) is True

def test_basic_false():
    assert is_subset([1, 2, 3], 3, [4], 1) is False

def test_subset_with_duplicates_in_arr2():
    assert is_subset([1, 2, 3], 3, [2, 2], 2) is True

def test_subset_with_duplicates_in_arr1():
    assert is_subset([1, 1, 2, 3], 4, [1, 3], 2) is True

def test_same_arrays():
    assert is_subset([4, 5, 6], 3, [4, 5, 6], 3) is True

def test_arr2_empty():
    assert is_subset([1, 2, 3], 3, [], 0) is True

def test_arr1_empty_arr2_non_empty():
    assert is_subset([], 0, [1], 1) is False

def test_negative_numbers():
    assert is_subset([-1, -2, -3], 3, [-1, -3], 2) is True

def test_mixed_positive_negative():
    assert is_subset([0, -1, 2, -3, 4], 5, [-3, 0], 2) is True

def test_not_subset_due_to_missing_element():
    assert is_subset([10, 20, 30], 3, [10, 40], 2) is False

def test_repeated_missing_element():
    assert is_subset([1, 2, 3], 3, [4, 4], 2) is False

def test_large_values():
    assert is_subset([10**9, 10**8], 2, [10**9], 1) is True
