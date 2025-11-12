import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from bitonic_sequence_buggy import lbs

def test_empty_list():
    assert lbs([]) == 0

def test_single_element():
    assert lbs([5]) == 1

def test_all_increasing():
    assert lbs([1, 2, 3, 4, 5]) == 5

def test_all_decreasing():
    assert lbs([9, 8, 7, 6, 5]) == 5

def test_bitonic_normal_case():
    assert lbs([1, 11, 2, 10, 4, 5, 2, 1]) == 6

def test_bitonic_large_pattern():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert lbs(arr) == 7

def test_strictly_decreasing_with_peaks():
    assert lbs([80, 60, 30, 40, 20, 10]) == 5

def test_with_duplicates():
    assert lbs([1, 2, 2, 3, 2, 1]) == 5

def test_flat_sequence():
    assert lbs([2, 2, 2, 2, 2]) == 1

def test_peak_in_middle():
    assert lbs([1, 3, 5, 4, 2]) == 5

def test_multiple_bitonic_segments():
    assert lbs([1, 2, 1, 2, 3, 2, 1]) == 5

def test_long_random_like_sequence():
    arr = [10, 20, 30, 25, 20, 15, 10, 5, 1]
    assert lbs(arr) == 9
