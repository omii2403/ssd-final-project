import os, sys
from hypothesis import given, strategies as st

# Ensure correct import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from find_Max_buggy import find_Max


# --- Strategy to generate valid rotated sorted arrays ---
def rotated_sorted_arrays():
    """Generates random sorted-then-rotated integer arrays."""
    base = st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1, max_size=20).map(sorted)
    return base.flatmap(
        lambda s: st.integers(min_value=0, max_value=len(s) - 1).map(
            lambda k: s[k:] + s[:k]
        )
    )


# --- Helper: valid (low, high) indices ---
def valid_indices(arr):
    return st.tuples(st.integers(min_value=0, max_value=len(arr) - 1),
                     st.integers(min_value=0, max_value=len(arr) - 1)).filter(lambda x: x[0] <= x[1])


# Property 1: The result must be one of the elements within arr[low:high+1]
@given(rotated_sorted_arrays())
def test_result_in_subarray(arr):
    low = 0
    high = len(arr) - 1
    result = find_Max(arr, low, high)
    assert result in arr[low:high + 1]


# Property 2: The result must equal the built-in max() over the same subrange
@given(rotated_sorted_arrays())
def test_matches_builtin_max(arr):
    low = 0
    high = len(arr) - 1
    result = find_Max(arr, low, high)
    expected = max(arr[low:high + 1])
    assert result == expected


# Property 3: For an already sorted (not rotated) array, maximum should be arr[high]
@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1, max_size=20).map(sorted))
def test_sorted_array_max_is_last(arr):
    low = 0
    high = len(arr) - 1
    result = find_Max(arr, low, high)
    assert result == arr[high]


# Property 4: For a rotated array, result should be >= both arr[low] and arr[high]
@given(rotated_sorted_arrays())
def test_rotated_array_result_is_extreme(arr):
    low = 0
    high = len(arr) - 1
    result = find_Max(arr, low, high)
    assert result >= arr[low] and result >= arr[high]


# Property 5: Single-element array → result == that element
@given(st.integers(min_value=-1000, max_value=1000))
def test_single_element_case(x):
    arr = [x]
    result = find_Max(arr, 0, 0)
    assert result == x
