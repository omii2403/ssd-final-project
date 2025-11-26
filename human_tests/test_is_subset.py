import pytest
import random
import sys
import os
from hypothesis import given, strategies as st, assume

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from is_subset_buggy import is_subset


@given(st.lists(st.integers(), min_size=1))
def test_valid_subset(xs):
    """
    Property: arr2 created from elements of arr1 must always be a subset.
    Spec: If every element in arr2 is taken from arr1, is_subset(arr1, m, arr2, n) must return True.
    Constraints: arr1 and arr2 are lists; m and n are positive integers representing lengths.
    """
    arr1 = xs
    m = len(arr1)

    # Always generate a subset from arr1
    arr2 = xs[: max(1, len(xs) // 2)]
    n = len(arr2)

    assert is_subset(arr1, m, arr2, n) is True


@given(st.lists(st.integers(), min_size=1), st.integers())
def test_invalid_subset(xs, extra):
    """
    Property: If arr2 contains at least one element not present in arr1, the function must return False.
    Spec: is_subset(arr1, m, arr2, n) must return False if ∃ an element in arr2 not found in arr1.
    Constraints: arr1 and arr2 are lists; m and n are positive integers representing lengths.
    """
    arr1 = xs
    m = len(arr1)

    # Force an element guaranteed not to be in arr1
    if extra in arr1:
        extra = (max(arr1) + 1) if arr1 else extra + 1  

    # arr2 includes one invalid element
    arr2 = [arr1[0]] + [extra]
    n = len(arr2)

    assert is_subset(arr1, m, arr2, n) is False


@given(st.lists(st.integers(), min_size=1))
def test_order_irrelevant(xs):
    """
    Property: Subset behavior must not depend on the ordering of elements in arr2.
    Spec: Permutations of arr2 must not change the boolean output of is_subset().
    Constraints: arr1 and arr2 are lists; m and n are positive integers representing lengths.
    """
    arr1 = xs
    m = len(arr1)

    arr2 = xs[: max(1, len(xs) // 2)]
    n = len(arr2)

    arr2_shuffled = arr2[:]
    random.shuffle(arr2_shuffled)

    assert is_subset(arr1, m, arr2, n) == is_subset(arr1, m, arr2_shuffled, n)


@given(st.lists(st.integers(), min_size=1))
def test_single_element_subset(xs):
    """
    Property: A single element chosen from arr1 must always be recognized as a valid subset.
    Spec: If arr2 contains exactly one element from arr1, the function must return True.
    Constraints: arr1 and arr2 are lists; m and n are positive integers representing lengths.
    """
    arr1 = xs
    m = len(arr1)

    arr2 = [arr1[0]]
    n = 1

    assert is_subset(arr1, m, arr2, n) is True
