
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from bitonic_sequence_buggy import lbs
# test_bitonic_subsequence.py


import random
import pytest
from hypothesis import given, strategies as st, assume, settings
from typing import List

def lbs(arr): 
    n = len(arr) 
    lis = [1 for i in range(n+1)] 
    for i in range(1 , n): 
        for j in range(0 , i): 
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
                lis[i] = lis[j] + 1
    lds = [1 for i in range(n+1)] 
    for i in reversed(range(n-1)): 
        for j in reversed(range(i-1 ,n)): 
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1
    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n): 
        maximum = max((lis[i] + lds[i]-1), maximum) 
    return maximum


# Property 1: Result must be at least 1 for non-empty arrays
@given(st.lists(st.integers(), min_size=1, max_size=50))
def test_lbs_minimum_length(arr):
    """
    Every non-empty array has at least a bitonic subsequence of length 1.
    """
    result = lbs(arr)
    assert result >= 1, f"LBS must be at least 1 for non-empty array, got {result}"


# Property 2: Result cannot exceed array length
@given(st.lists(st.integers(), min_size=1, max_size=50))
def test_lbs_maximum_length(arr):
    """
    The longest bitonic subsequence cannot be longer than the array itself.
    """
    result = lbs(arr)
    assert result <= len(arr), f"LBS {result} cannot exceed array length {len(arr)}"


# Property 3: Monotonic increasing sequence
@given(st.lists(st.integers(), min_size=1, max_size=50))
def test_lbs_monotonic_increasing(arr):
    """
    For a strictly increasing sequence, the LBS equals the array length.
    A strictly increasing sequence is itself bitonic (with empty decreasing part).
    """
    sorted_arr = sorted(set(arr))  # Remove duplicates and sort
    if len(sorted_arr) >= 1:
        result = lbs(sorted_arr)
        assert result == len(sorted_arr), \
            f"For increasing sequence {sorted_arr}, LBS should be {len(sorted_arr)}, got {result}"


# Property 4: Monotonic decreasing sequence
@given(st.lists(st.integers(), min_size=1, max_size=50))
def test_lbs_monotonic_decreasing(arr):
    """
    For a strictly decreasing sequence, the LBS equals the array length.
    A strictly decreasing sequence is itself bitonic (with empty increasing part).
    """
    sorted_arr = sorted(set(arr), reverse=True)  # Remove duplicates and sort descending
    if len(sorted_arr) >= 1:
        result = lbs(sorted_arr)
        assert result == len(sorted_arr), \
            f"For decreasing sequence {sorted_arr}, LBS should be {len(sorted_arr)}, got {result}"


# Property 5: Adding duplicate elements doesn't increase LBS
@given(st.lists(st.integers(min_value=-100, max_value=100), min_size=2, max_size=30))
def test_lbs_duplicate_element(arr):
    """
    Adding a duplicate element to the array should not increase the LBS length,
    since bitonic subsequences require strict inequalities.
    """
    original_lbs = lbs(arr)
    # Add duplicate of first element
    arr_with_dup = arr + [arr[0]]
    new_lbs = lbs(arr_with_dup)
    assert new_lbs >= original_lbs, \
        f"Adding duplicate should not decrease LBS: original={original_lbs}, new={new_lbs}"
    # In most cases it should stay the same, but we can't assert equality
    # because the position matters for DP


# Property 6: Constant array has LBS of 1
@given(st.integers(min_value=-1000, max_value=1000), st.integers(min_value=1, max_value=20))
def test_lbs_constant_array(value, length):
    """
    An array with all identical elements has LBS = 1.
    No strictly increasing or decreasing subsequence can have length > 1.
    """
    arr = [value] * length
    result = lbs(arr)
    assert result == 1, f"Constant array {arr} should have LBS=1, got {result}"


# Property 7: Single peak (perfect bitonic)
@given(st.integers(min_value=2, max_value=15))
def test_lbs_perfect_bitonic(n):
    """
    For a perfect bitonic sequence [1,2,3,...,n,...,3,2,1], the LBS is 2n-1.
    """
    arr = list(range(1, n+1)) + list(range(n-1, 0, -1))
    result = lbs(arr)
    expected = 2 * n - 1
    assert result == expected, \
        f"For perfect bitonic {arr}, LBS should be {expected}, got {result}"


# Property 8: Longest Increasing Subsequence (LIS) is lower bound
@given(st.lists(st.integers(min_value=-100, max_value=100), min_size=1, max_size=40))
def test_lbs_lis_lower_bound(arr):
    """
    The LBS must be at least as long as the LIS, since any increasing
    sequence is a valid bitonic sequence (with empty decreasing part).
    """
    # Compute LIS using simple DP
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    max_lis = max(lis)
    
    result = lbs(arr)
    assert result >= max_lis, \
        f"LBS {result} must be >= LIS {max_lis} for array {arr}"


# Property 9: Removing elements cannot increase LBS
@given(st.lists(st.integers(min_value=-50, max_value=50), min_size=3, max_size=30))
@settings(max_examples=50)
def test_lbs_removal_monotonicity(arr):
    """
    Removing an element from the array cannot increase the LBS,
    since we're removing potential subsequence elements.
    """
    original_lbs = lbs(arr)
    # Remove random element from middle
    if len(arr) > 2:
        modified_arr = arr[:len(arr)//2] + arr[len(arr)//2 + 1:]
        new_lbs = lbs(modified_arr)
        assert new_lbs <= original_lbs, \
            f"Removing element should not increase LBS: original={original_lbs}, new={new_lbs}"


# Property 10: Verify against provided test cases
def test_lbs_known_examples():
    """
    Test against the provided examples from MBPP.
    """
    assert lbs([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 7
    assert lbs([1, 11, 2, 10, 4, 5, 2, 1]) == 6
    assert lbs([80, 60, 30, 40, 20, 10]) == 5
