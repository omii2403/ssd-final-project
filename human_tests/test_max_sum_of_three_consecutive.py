import pytest
import sys
import os
from hypothesis import given, strategies as st, assume

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from max_sum_of_three_consecutive_buggy import max_sum_of_three_consecutive


# Property 1: Result cannot exceed sum of all positive elements
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=30))
def test_sum_upper_bound(arr):
    """The max sum with constraint cannot exceed the sum of all elements."""
    n = len(arr)
    result = max_sum_of_three_consecutive(arr, n)
    total_sum = sum(arr)
    assert result <= total_sum, \
        f"Max sum {result} cannot exceed total sum {total_sum}"


# Property 2: Single element returns that element
@given(st.integers(min_value=-100, max_value=100))
def test_single_element(value):
    """For array of length 1, result should be that element."""
    arr = [value]
    result = max_sum_of_three_consecutive(arr, 1)
    assert result == value, f"Single element {value} should return {value}, got {result}"


# Property 3: Two elements return their sum
@given(st.integers(min_value=-100, max_value=100), 
       st.integers(min_value=-100, max_value=100))
def test_two_elements(a, b):
    """For array of length 2, result should be sum of both."""
    arr = [a, b]
    result = max_sum_of_three_consecutive(arr, 2)
    expected = a + b
    assert result == expected, f"Two elements should return their sum {expected}, got {result}"


# Property 4: Known test cases from GeeksforGeeks
def test_known_values():
    """Test against known examples from GFG."""
    # Example 1: [1, 2, 3] -> 5 (take 2+3)
    arr1 = [1, 2, 3]
    assert max_sum_of_three_consecutive(arr1, 3) == 5
    
    # Example 2: [3000, 2000, 1000, 3, 10] -> 5013
    arr2 = [3000, 2000, 1000, 3, 10]
    assert max_sum_of_three_consecutive(arr2, 5) == 5013
    
    # Example 3: [100, 1000, 100, 1000, 1] -> 2101
    arr3 = [100, 1000, 100, 1000, 1]
    assert max_sum_of_three_consecutive(arr3, 5) == 2101


# Property 5: Monotonically increasing array
def test_increasing_array():
    """For increasing array [1,2,3,4,5], optimal is skip one element."""
    arr = [1, 2, 3, 4, 5]
    result = max_sum_of_three_consecutive(arr, 5)
    # Optimal: 1+2+4+5 = 12 (skip 3)
    assert result == 12, f"Expected 12, got {result}"


# Property 6: Array with zeros
@given(st.integers(min_value=1, max_value=10))
def test_array_with_zeros(n):
    """Array of all zeros should return 0."""
    arr = [0] * n
    result = max_sum_of_three_consecutive(arr, n)
    assert result == 0, f"Array of zeros should return 0, got {result}"


# Property 7: All same positive values with length 4
def test_uniform_array_length_4():
    """For [x, x, x, x], should skip one to avoid 4 consecutive."""
    arr = [10, 10, 10, 10]
    result = max_sum_of_three_consecutive(arr, 4)
    # Optimal: skip one element -> 30
    expected = 30
    assert result == expected, f"Expected {expected}, got {result}"


# Property 8: All same positive values with length 5
def test_uniform_array_length_5():
    """For [x, x, x, x, x], optimal pattern."""
    arr = [1, 1, 1, 1, 1]
    result = max_sum_of_three_consecutive(arr, 5)
    # Optimal: take 4 elements (e.g., indices 0,1,3,4) = 4
    expected = 4
    assert result == expected, f"Expected {expected}, got {result}"


# Property 9: Alternating high-low pattern
def test_alternating_pattern():
    """For alternating high-low values."""
    arr = [1000, 1, 1000, 1, 1000]
    result = max_sum_of_three_consecutive(arr, 5)
    # Optimal: 1000+1+1000 (indices 0,1,2) = 2001, or 1000+1000+1000 (indices 0,2,4) = 3000
    # Using DP: sum[4] = max(sum[3], sum[2]+arr[4], arr[4]+arr[3]+sum[1])
    # sum[0]=1000, sum[1]=1001, sum[2]=max(1001, max(1+1000, 1000+1000))=2000
    # sum[3]=max(2000, 1001+1, 1+1000+1000)=2001
    # sum[4]=max(2001, 2000+1000, 1000+1+1000)=3000
    expected = 3000
    assert result == expected, f"Expected {expected}, got {result}"


# Property 10: Large value domination
def test_large_value_domination():
    """A very large value should be included in result."""
    arr = [1, 1, 10000, 1, 1]
    result = max_sum_of_three_consecutive(arr, 5)
    assert result >= 10000, f"Result should include 10000, got {result}"


# Property 11: No four consecutive check
def test_no_four_consecutive():
    """Verify constraint: no 4 consecutive elements."""
    arr = [100, 100, 100, 100, 1]
    result = max_sum_of_three_consecutive(arr, 5)
    # Optimal: 100+100+100+1 = 301 (indices 0,1,2,4 or similar pattern)
    expected = 301
    assert result == expected, f"Expected {expected}, got {result}"


# Property 12: Three elements - check recurrence
def test_three_elements_recurrence():
    """For 3 elements, use recurrence: max(sum[1], arr[1]+arr[2], arr[0]+arr[2])."""
    # Test case where taking all 3 is NOT optimal
    arr = [1, 1, 1]
    result = max_sum_of_three_consecutive(arr, 3)
    # sum[2] = max(sum[1]=2, arr[1]+arr[2]=2, arr[0]+arr[2]=2) = 2
    expected = 2
    assert result == expected, f"Expected {expected}, got {result}"


# Property 13: Three elements where all is optimal
def test_three_elements_all():
    """For 3 elements where taking all is optimal."""
    arr = [10, 20, 30]
    result = max_sum_of_three_consecutive(arr, 3)
    # sum[2] = max(sum[1]=30, arr[1]+arr[2]=50, arr[0]+arr[2]=40) = 50
    expected = 50
    assert result == expected, f"Expected {expected}, got {result}"


# Property 14: Empty edge case handled by n >= 1 constraint
def test_single_positive():
    """Single positive element."""
    arr = [42]
    result = max_sum_of_three_consecutive(arr, 1)
    assert result == 42


# Property 15: Negative elements
def test_with_negatives():
    """Test with negative numbers - should skip negatives optimally."""
    arr = [10, -5, 20, -10, 30]
    result = max_sum_of_three_consecutive(arr, 5)
    # Should skip negatives: 10+20+30 = 60? But that's indices 0,2,4 (not 3 consecutive)
    assert result >= 50, f"Should skip negative optimally, got {result}"
