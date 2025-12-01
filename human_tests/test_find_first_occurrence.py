# test_find_first_occurrence.py
# Replace 'your_module' with the module path where find_first_occurrence() is defined.

import os, sys
from hypothesis import given, strategies as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))


from find_first_occurrence_buggy import find_first_occurrence   # <-- change to actual module


@given(st.lists(st.integers(), min_size=1).map(sorted), st.integers())
def test_correct_index_for_present_value(A, x):
    """
    Property: If x exists in A, the function must return the index of its first occurrence.
    Spec: For all sorted lists A and integers x, if x is present, then
          find_first_occurrence(A, x) == A.index(x).
    Constraints: A is a sorted list of integers; x is an integer.
    """
    if x in A:
        assert find_first_occurrence(A, x) == A.index(x)


@given(st.lists(st.integers(), min_size=1).map(sorted), st.integers())
def test_returns_minus_one_when_not_present(A, x):
    """
    Property: If x is not present in A, the function must return -1.
    Spec: For all sorted lists A and integers x, if x ∉ A,
          find_first_occurrence(A, x) must return -1.
    Constraints: A is a sorted list of integers; x is an integer.
    """
    if x not in A:
        assert find_first_occurrence(A, x) == -1


@given(st.lists(st.integers(), min_size=1).map(sorted))
def test_first_occurrence_correct_for_duplicates(A):
    """
    Property: For lists with duplicate values, the function must return the first index.
    Spec: If A contains repeated values, then for any value v ∈ A,
          find_first_occurrence(A, v) must equal the leftmost index where v appears.
    Constraints: A is a sorted list of integers.
    """
    # Pick any value from A
    x = A[len(A) // 2]  # guaranteed to be in A
    assert find_first_occurrence(A, x) == A.index(x)


@given(st.lists(st.integers(), min_size=1).map(sorted), st.integers())
def test_return_value_is_valid_index_or_minus_one(A, x):
    """
    Property: The return value must always be a valid index within range or -1.
    Spec: For any A and x:
          - If return value r != -1, then 0 <= r < len(A) and A[r] == x.
          - If x not in A, the return must be exactly -1.
    Constraints: A is a sorted list of integers; x is an integer.
    """
    r = find_first_occurrence(A, x)

    if r == -1:
        assert x not in A
    else:
        assert 0 <= r < len(A)
        assert A[r] == x
        if r > 0:
            assert A[r - 1] < x  # previous element must be strictly smaller


@given(st.lists(st.integers(), min_size=1).map(sorted), st.integers())
def test_monotonic_property(A, x):
    """
    Property: If x is present in A, then for any index k < returned index r,
              A[k] must not equal x.
    Spec: Guarantees that r is the FIRST occurrence.
    Constraints: A is a sorted list of integers; x is an integer.
    """
    r = find_first_occurrence(A, x)

    if x in A:
        assert r == A.index(x)
        for k in range(r):
            assert A[k] != x
