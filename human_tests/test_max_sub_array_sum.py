import os
import sys
from hypothesis import given, strategies as st, assume

# Ensure bug_portfolio directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from max_sub_array_sum_buggy import max_sub_array_sum


def bruteforce_max_sub_array_length(a):
    """
    Reference implementation:
    - Compute maximum subarray sum by brute force.
    - On ties, keep the earliest subarray (smallest start index).
    - Return its length.
    """
    n = len(a)
    best_sum = None
    best_len = None
    best_start = None

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            if best_sum is None or current_sum > best_sum:
                best_sum = current_sum
                best_len = j - i + 1
                best_start = i
            # On equal sum, prefer earliest start index; do nothing on tie
    return best_len


# Strategy: lists of integers, length 1–20
list_strategy = st.lists(
    st.integers(min_value=-20, max_value=20),
    min_size=1,
    max_size=20,
)


@given(list_strategy)
def test_max_sub_array_sum_matches_bruteforce(a):
    """Length of max-sum subarray should match brute force definition."""
    size = len(a)
    result = max_sub_array_sum(a, size)
    expected = bruteforce_max_sub_array_length(a)
    assert result == expected


@given(list_strategy)
def test_max_sub_array_sum_length_bounds(a):
    """Returned length must be between 1 and len(a)."""
    size = len(a)
    length = max_sub_array_sum(a, size)
    assert 1 <= length <= size


@given(list_strategy)
def test_max_sub_array_sum_all_non_positive_returns_one(a):
    """
    If all numbers are non-positive, the best subarray is the single
    largest element, so length should be 1.
    """
    assume(all(x <= 0 for x in a))
    size = len(a)
    length = max_sub_array_sum(a, size)
    assert length == 1
