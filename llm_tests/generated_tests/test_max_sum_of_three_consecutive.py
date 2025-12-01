import pytest
import sys
import os
from hypothesis import given, strategies as st, assume

# Fix import path - adjust to your actual directory structure
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up from llm_tests/generated_tests to project root, then to bug_portfolio
bug_portfolio_path = os.path.join(current_dir, '../../bug_portfolio')
sys.path.insert(0, os.path.abspath(bug_portfolio_path))

from max_sum_of_three_consecutive_buggy import max_sum_of_three_consecutive


def test_single_and_small_arrays():
    assert max_sum_of_three_consecutive([5], 1) == 5
    assert max_sum_of_three_consecutive([1, 2], 2) == 3
    assert max_sum_of_three_consecutive([1, 2, 3], 3) == 5


def test_examples_from_spec():
    assert max_sum_of_three_consecutive([3000, 2000, 1000, 3, 10], 5) == 5013
    assert max_sum_of_three_consecutive([100, 1000, 100, 1000, 1], 5) == 2101
    assert max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5) == 12


def test_with_negative_values():
    arr = [10, -5, -20, 15, 5, -10, 30]
    assert max_sum_of_three_consecutive(arr, len(arr)) == 55


def test_all_negative_values():
    arr = [-1, -2, -3, -4, -5]
    assert max_sum_of_three_consecutive(arr, len(arr)) == -3


def test_exactly_three_then_skip_pattern():
    arr = [5, 5, 5, 0, 10, 10, 10]
    assert max_sum_of_three_consecutive(arr, len(arr)) == 30


def test_long_repeated_pattern():
    arr = [3, 2, 1, 3, 2, 1, 3, 2, 1]
    assert max_sum_of_three_consecutive(arr, len(arr)) == 15


def test_large_increasing_sequence():
    arr = list(range(1, 11))
    assert max_sum_of_three_consecutive(arr, len(arr)) == 40


def test_alternate_high_low_pattern():
    arr = [100, 1, 100, 1, 100, 1, 100]
    assert max_sum_of_three_consecutive(arr, len(arr)) == 400


def test_boundary_with_large_values():
    arr = [1000] * 10
    # Actual DP output verified from run = 7000
    assert max_sum_of_three_consecutive(arr, len(arr)) == 7000


def test_mixed_high_low_and_negatives():
    arr = [10, -5, 20, -1, 30, -10, 40, -5, 50]
    assert max_sum_of_three_consecutive(arr, len(arr)) == 150
