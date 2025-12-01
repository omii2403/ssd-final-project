import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from longest_increasing_subsequence_buggy import longest_increasing_subsequence

def test_single_element():
    assert longest_increasing_subsequence([5]) == 1

def test_strictly_increasing():
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_strictly_decreasing():
    assert longest_increasing_subsequence([9, 7, 5, 3, 1]) == 1

def test_example_case():
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6

def test_all_elements_equal():
    assert longest_increasing_subsequence([4, 4, 4, 4]) == 1

def test_two_increasing_runs():
    assert longest_increasing_subsequence([3, 4, 5, 1, 2, 3]) == 3

def test_lis_in_middle():
    assert longest_increasing_subsequence([9, 1, 2, 3, 0]) == 3

def test_large_jump_values():
    assert longest_increasing_subsequence([1, 100, 2, 200, 3, 300]) == 4

def test_negative_values():
    assert longest_increasing_subsequence([-5, -4, -3, -10, -2, -1]) == 5

def test_mixed_increasing_and_equal():
    assert longest_increasing_subsequence([1, 2, 2, 3, 4]) == 4

def test_lis_only_at_end():
    assert longest_increasing_subsequence([8, 7, 6, 3, 4, 5]) == 3

def test_lis_only_at_start():
    assert longest_increasing_subsequence([1, 2, 3, 9, 8, 7]) == 4

def test_alternating_high_low():
    assert longest_increasing_subsequence([1, 10, 2, 9, 3, 8, 4, 7]) == 5

def test_random_pattern():
    assert longest_increasing_subsequence([4, 10, 4, 3, 8, 9]) == 3

def test_duplicate_clusters():
    assert longest_increasing_subsequence([2, 2, 2, 3, 3, 4, 1, 1]) == 3
