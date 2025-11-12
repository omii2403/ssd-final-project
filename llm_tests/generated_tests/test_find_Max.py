import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from find_Max_buggy import find_Max


def test_basic_case():
    assert find_Max([4, 5, 6, 7, 0, 1, 2], 0, 6) == 7

def test_full_rotation():
    assert find_Max([7, 0, 1, 2, 3, 4, 5, 6], 0, 7) == 7

def test_no_rotation():
    assert find_Max([1, 2, 3, 4, 5, 6, 7], 0, 6) == 7

def test_single_element():
    assert find_Max([10], 0, 0) == 10

def test_two_elements_rotated():
    assert find_Max([9, 2], 0, 1) == 9

def test_partial_subarray():
    assert find_Max([4, 5, 6, 7, 0, 1, 2], 2, 5) == 7

def test_subarray_in_rotated_part():
    assert find_Max([4, 5, 6, 7, 0, 1, 2], 4, 6) == 2

def test_all_same_elements():
    assert find_Max([3, 3, 3, 3, 3], 0, 4) == 3

def test_negative_numbers():
    assert find_Max([-4, -3, -2, -10, -9], 0, 4) == -2

def test_large_numbers():
    assert find_Max([100000, 200000, 300000, 10, 20, 30], 0, 5) == 300000
