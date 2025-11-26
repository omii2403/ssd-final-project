from typing import List
import os, sys
from hypothesis import given, strategies as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from count_duplic_buggy import count_duplic


@given(st.lists(st.integers(), min_size=1))
def test_lengths_match(xs: List[int]) -> None:
    """
    Property: Output lengths match
    Spec: count_duplic(lists) returns (elements, counts) where len(elements) == len(counts).
    Constraint: 'lists' is a non-empty list of integers.
    """
    elements, counts = count_duplic(xs)
    assert isinstance(elements, list)
    assert isinstance(counts, list)
    assert len(elements) == len(counts)


@given(st.lists(st.integers(), min_size=1))
def test_no_adjacent_duplicates(xs: List[int]) -> None:
    """
    Property: No adjacent duplicates in `elements`
    Spec: Consecutive elements returned must be different since duplicates are grouped.
    Constraint: 'lists' is a non-empty list of integers.
    """
    elements, counts = count_duplic(xs)
    for i in range(len(elements) - 1):
        assert elements[i] != elements[i + 1]


@given(st.lists(st.integers(), min_size=1))
def test_counts_positive(xs: List[int]) -> None:
    """
    Property: All counts are positive integers
    Spec: Every run-length must be >= 1.
    Constraint: 'lists' is a non-empty list of integers.
    """
    elements, counts = count_duplic(xs)
    assert all(isinstance(c, int) for c in counts)
    assert all(c >= 1 for c in counts)


@given(st.lists(st.integers(), min_size=1))
def test_reconstruction(xs: List[int]) -> None:
    """
    Property: Reconstructing list gives original list
    Spec: Expanding elements by their counts must exactly rebuild the original input list.
    Constraint: 'lists' is a non-empty list of integers.
    """
    elements, counts = count_duplic(xs)
    rebuilt: List[int] = [e for e, c in zip(elements, counts) for _ in range(c)]
    assert rebuilt == xs


@given(st.lists(st.integers(), min_size=1))
def test_preserves_order(xs: List[int]) -> None:
    """
    Property: `elements` preserves order of first appearance (for consecutive runs)
    Spec: The sequence of unique consecutive elements must match the original order of runs.
    Constraint: 'lists' is a non-empty list of integers.
    """
    elements, _ = count_duplic(xs)

    expected: List[int] = []
    for x in xs:
        if not expected or expected[-1] != x:
            expected.append(x)

    assert elements == expected
