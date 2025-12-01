import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from max_sub_array_sum_buggy import max_sub_array_sum

def test_max_sub_array_sum_example():
    a = [1, -2, 3, 4, -1, 2]
    size = 6
    assert max_sub_array_sum(a, size) == 4

def test_max_sub_array_sum_all_positive():
    a = [1, 2, 3, 4, 5]
    size = 5
    assert max_sub_array_sum(a, size) == 5

def test_max_sub_array_sum_all_negative():
    a = [-2, -3, -1, -5]
    size = 4
    assert max_sub_array_sum(a, size) == 1 # Subarray [-1]

def test_max_sub_array_sum_mixed_start_positive():
    a = [5, -1, -2, 3, -1, 4]
    size = 6
    assert max_sub_array_sum(a, size) == 1 # Subarray [5] or [4] but earlier
                                           # [5] sum 5, length 1
                                           # [3, -1, 4] sum 6, length 3
                                           # [5] is not the max.
                                           # Correct: [3, -1, 4] sum 6, length 3.
                                           # Or [5, -1, -2, 3, -1, 4] is 8, length 6
    assert max_sub_array_sum(a, size) == 6

def test_max_sub_array_sum_mixed_start_negative():
    a = [-1, -2, 5, 6, -3, 1]
    size = 6
    assert max_sub_array_sum(a, size) == 2 # Subarray [5, 6]

def test_max_sub_array_sum_single_element_positive():
    a = [10]
    size = 1
    assert max_sub_array_sum(a, size) == 1

def test_max_sub_array_sum_single_element_negative():
    a = [-10]
    size = 1
    assert max_sub_array_sum(a, size) == 1

def test_max_sub_array_sum_zero_included():
    a = [1, -3, 4, 0, -2, 5]
    size = 6
    assert max_sub_array_sum(a, size) == 3 # Subarray [4, 0, -2, 5] sum 7, length 4

def test_max_sub_array_sum_duplicate_max_sum_earliest():
    a = [1, 2, -1, 3, -1, 1, 2]
    size = 7
    assert max_sub_array_sum(a, size) == 3 # [1, 2, -1, 3] sum 5, length 4
                                            # [1, 2] sum 3, length 2
                                            # [3] sum 3, length 1
                                            # [1, 2] sum 3, length 2
                                            # [1, 2, -1, 3] sum 5
                                            # [1, 2] earlier than [1,2] near the end

    assert max_sub_array_sum(a, size) == 4 # [1, 2, -1, 3] gives 5

def test_max_sub_array_sum_long_array_with_fluctuations():
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    size = 9
    assert max_sub_array_sum(a, size) == 4 # [4, -1, 2, 1]

def test_max_sub_array_sum_all_zeros():
    a = [0, 0, 0, 0]
    size = 4
    assert max_sub_array_sum(a, size) == 1 # Any single [0]

def test_max_sub_array_sum_large_numbers():
    a = [100, -1, 200, -50, 300]
    size = 5
    assert max_sub_array_sum(a, size) == 5 # [100, -1, 200, -50, 300] = 549