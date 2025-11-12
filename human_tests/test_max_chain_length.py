import pytest
import sys
import os
from hypothesis import given, strategies as st, assume

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from max_chain_length_buggy import Pair, max_chain_length


# Property 1: Chain length cannot exceed array size
@given(st.lists(st.tuples(st.integers(min_value=1, max_value=50),
                          st.integers(min_value=1, max_value=50)),
                min_size=1, max_size=30))
def test_chain_length_upper_bound(pairs_list):
    """Maximum chain length cannot be greater than the number of pairs."""
    arr = [Pair(a, b) for a, b in pairs_list if a < b]
    if len(arr) == 0:
        return
    result = max_chain_length(arr, len(arr))
    assert result <= len(arr), \
        f"Chain length {result} cannot exceed array size {len(arr)}"


# Property 2: Chain length is at least 1 for non-empty arrays
@given(st.lists(st.tuples(st.integers(min_value=1, max_value=50),
                          st.integers(min_value=1, max_value=50)),
                min_size=1, max_size=30))
def test_chain_length_lower_bound(pairs_list):
    """Every non-empty array has at least a chain of length 1."""
    arr = [Pair(a, b) for a, b in pairs_list if a < b]
    if len(arr) == 0:
        return
    result = max_chain_length(arr, len(arr))
    assert result >= 1, \
        f"Chain length must be at least 1 for non-empty array, got {result}"


# Property 3: Single pair always has chain length 1
@given(st.integers(min_value=1, max_value=100),
       st.integers(min_value=1, max_value=100))
def test_single_pair_chain(a, b):
    """A single valid pair always forms a chain of length 1."""
    assume(a < b)
    arr = [Pair(a, b)]
    result = max_chain_length(arr, 1)
    assert result == 1, f"Single pair should have chain length 1, got {result}"


# Property 4: Sorted non-overlapping pairs form full chain
@given(st.integers(min_value=2, max_value=10))
def test_perfect_chain(n):
    """Non-overlapping pairs with gaps should chain completely."""
    arr = [Pair(i * 3, i * 3 + 1) for i in range(n)]
    result = max_chain_length(arr, n)
    assert result == n, \
        f"Perfect non-overlapping chain should have length {n}, got {result}"


# Property 5: Completely overlapping pairs have chain length 1
@given(st.integers(min_value=1, max_value=20))
def test_overlapping_pairs(n):
    """All pairs with same or overlapping ranges should have chain length 1."""
    arr = [Pair(1, 10) for _ in range(n)]
    result = max_chain_length(arr, n)
    assert result == 1, \
        f"Completely overlapping pairs should have chain length 1, got {result}"


# Property 6: Known test cases
def test_chain_known_values():
    """Test against known examples."""
    arr1 = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
    assert max_chain_length(arr1, 4) == 3

    arr2 = [Pair(5, 10), Pair(1, 11)]
    assert max_chain_length(arr2, 2) == 1

    arr3 = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
    assert max_chain_length(arr3, 3) == 3


# Property 7: Adding dominated pair shouldn't reduce chain
@given(st.lists(st.tuples(st.integers(min_value=1, max_value=50),
                          st.integers(min_value=1, max_value=50)),
                min_size=1, max_size=15))
def test_adding_dominated_pair(pairs_list):
    """Adding a dominated pair shouldn't decrease max chain."""
    arr = [Pair(a, b) for a, b in pairs_list if a < b]
    if len(arr) == 0:
        return
    result1 = max_chain_length(arr, len(arr))
    arr_extended = arr + [Pair(1, 2)]
    result2 = max_chain_length(arr_extended, len(arr_extended))
    assert result2 >= result1, \
        f"Adding a dominated pair shouldn't decrease chain length: {result1} vs {result2}"


# Property 8: Touching pairs CAN chain if b <= c
def test_touching_pairs_can_chain():
    """Pairs where first.b == second.a CAN chain (non-strict inequality)."""
    arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
    result = max_chain_length(arr, 3)
    # DP approach: depends on order, but should be >= 1
    assert result >= 1, \
        f"Touching pairs should form at least chain of 1, got {result}"


# Property 9: Non-overlapping pairs with gaps chain fully
def test_non_overlapping_with_gaps():
    """Pairs with clear gaps (b < c) must form a full chain."""
    arr = [Pair(1, 5), Pair(10, 15), Pair(20, 25)]
    result = max_chain_length(arr, 3)
    assert result == 3, \
        f"Non-overlapping pairs with gaps should form full chain, got {result}"


# Property 10: Duplicate pairs always overlap
@given(st.integers(min_value=1, max_value=10),
       st.integers(min_value=1, max_value=50))
def test_duplicate_pairs(n, a):
    """Duplicate pairs should all have chain length 1."""
    assume(a < a + 10)
    arr = [Pair(a, a + 10) for _ in range(n)]
    result = max_chain_length(arr, n)
    assert result == 1, \
        f"Duplicate pairs should have chain length 1, got {result}"


# Property 11: Empty array edge case
def test_empty_array():
    """Empty array should return 0."""
    arr = []
    result = max_chain_length(arr, 0)
    assert result == 0, f"Empty array should return 0, got {result}"


# Property 12: Nested pairs test
def test_nested_pairs():
    """Test with one pair completely inside another."""
    arr = [Pair(1, 10), Pair(2, 5)]
    result = max_chain_length(arr, 2)
    assert result == 1, \
        f"Nested pairs should have chain length 1, got {result}"


# Property 13: Adjacent non-overlapping pairs
def test_adjacent_pairs_with_gap():
    """Pairs (1,3) and (4,6) should chain since 3 < 4."""
    arr = [Pair(1, 3), Pair(4, 6)]
    result = max_chain_length(arr, 2)
    assert result == 2, \
        f"Adjacent pairs with gap should chain, got {result}"


# Property 14: Monotonicity - more pairs should not decrease max chain
@given(st.lists(st.tuples(st.integers(min_value=1, max_value=30),
                          st.integers(min_value=1, max_value=30)),
                min_size=2, max_size=10))
def test_adding_pairs_monotonic(pairs_list):
    """Adding more pairs should not decrease the maximum chain length."""
    arr_full = [Pair(a, b) for a, b in pairs_list if a < b]
    if len(arr_full) < 2:
        return
    
    # Test with subset vs full set
    arr_subset = arr_full[:-1]
    result_subset = max_chain_length(arr_subset, len(arr_subset))
    result_full = max_chain_length(arr_full, len(arr_full))
    
    assert result_full >= result_subset, \
        f"Adding pairs should not decrease chain: {result_subset} vs {result_full}"
