# test_longest_increasing_subsequence_fixed.py
# Adjust module path below if needed. This file tests the implementation
# at ../bug_portfolio/longest_increasing_subsequence_buggy.py as in your example.

import sys
import os
from typing import List

# Fix import path (keeps your original layout)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from hypothesis import given, strategies as st
from longest_increasing_subsequence_buggy import longest_increasing_subsequence

@given(st.lists(st.integers(), min_size=0))
def test_result_bounds(arr: List[int]) -> None:
    """
    Property: Result must be within valid bounds.
    Spec: 0 <= LIS_length <= len(arr). For an empty list, LIS_length == 0.
    Constraint: 'arr' is a list of integers (can be empty or contain duplicates).
    """
    r = longest_increasing_subsequence(arr)
    assert isinstance(r, int)
    assert 0 <= r <= len(arr)
    if len(arr) == 0:
        assert r == 0


@given(st.integers(min_value=0, max_value=200))
def test_strictly_increasing_input(n: int) -> None:
    """
    Property: If the input array is strictly increasing, LIS equals the full length.
    Spec: For any non-negative integer n, the strictly increasing list
          range(0, n) has LIS == n.
    Constraint: We construct A = [0,1,2,...,n-1] which is strictly increasing.
    """
    arr = list(range(n))
    assert longest_increasing_subsequence(arr) == n


@given(st.integers(min_value=0, max_value=200))
def test_strictly_decreasing_input(n: int) -> None:
    """
    Property: If the input array is strictly decreasing, LIS must be 1 (unless empty).
    Spec: For A = [n, n-1, ..., 1] (length n), the LIS length is 1 when n >= 1, else 0.
    Constraint: We construct a strictly decreasing array to validate the behavior.
    """
    if n == 0:
        arr: List[int] = []
        assert longest_increasing_subsequence(arr) == 0
        return

    arr = list(range(n, 0, -1))  # length n, strictly decreasing
    assert longest_increasing_subsequence(arr) == 1


@given(st.integers(min_value=0, max_value=200), st.integers())
def test_repeated_values_have_lis_one(n: int, v: int) -> None:
    """
    Property: Repeated equal values are not considered increasing.
    Spec: An array consisting of the same value v repeated n times has LIS == 1 if n>0, else 0.
    Constraint: 'arr' can be empty (n==0) or have duplicates.
    """
    if n == 0:
        arr: List[int] = []
        assert longest_increasing_subsequence(arr) == 0
        return

    arr = [v] * n
    assert longest_increasing_subsequence(arr) == 1


@given(st.lists(st.integers(), min_size=0))
def test_subsequence_property(arr: List[int]) -> None:
    """
    Property: The LIS length must be at least as large as the length of any strictly increasing subsequence.
    Spec: For any strictly increasing subsequence s formed by taking elements at increasing indices,
          its length len(s) must be <= longest_increasing_subsequence(arr).
    Constraint: 'arr' is a list of integers (can be empty or contain duplicates).
    Implementation detail: we construct a valid increasing subsequence by selecting indices
                        where values strictly increase and check the returned LIS is >= that length.
    """
    # Build one strictly increasing subsequence greedily (not necessarily maximal)
    subseq_len = 0
    last = None
    for x in arr:
        if subseq_len == 0 or x > last:
            subseq_len += 1
            last = x

    # The greedy subsequence above is a valid increasing subsequence,
    # so the LIS must be at least subseq_len.
    result = longest_increasing_subsequence(arr)
    assert result >= subseq_len
