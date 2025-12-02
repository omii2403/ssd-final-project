import pytest
import os, sys
from hypothesis import given, strategies as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from get_median_buggy import get_median

# Strategy: sorted lists of equal length n
def sorted_list_strategy(n):
    return st.lists(st.integers(-10_000, 10_000), min_size=n, max_size=n).map(sorted)

# 1. Median symmetry: swapping arr1 and arr2 must not change result
@given(
    n=st.integers(min_value=1, max_value=50),
    arr1=st.lists(st.integers(-500, 500), min_size=50, max_size=50),
    arr2=st.lists(st.integers(-500, 500), min_size=50, max_size=50)
)
def test_symmetry(n, arr1, arr2):
    arr1 = sorted(arr1[:n])
    arr2 = sorted(arr2[:n])
    m1 = get_median(arr1, arr2, n)
    m2 = get_median(arr2, arr1, n)
    assert m1 == pytest.approx(m2)


# 2. Non-decreasing arrays: median should lie between min and max of merged
@given(
    n=st.integers(min_value=1, max_value=40),
    arr1=sorted_list_strategy(40),
    arr2=sorted_list_strategy(40)
)
def test_value_bounds(n, arr1, arr2):
    arr1 = arr1[:n]
    arr2 = arr2[:n]
    merged = arr1 + arr2
    med = get_median(arr1, arr2, n)
    assert min(merged) <= med <= max(merged)


# 3. Median for arrays with duplicates
@given(
    n=st.integers(min_value=1, max_value=30),
    v=st.integers(-1000, 1000)
)
def test_all_duplicates(n, v):
    arr1 = [v] * n
    arr2 = [v] * n
    assert get_median(arr1, arr2, n) == pytest.approx(v)



# 4. Median always lies between the two middle elements of merged
@given(
    n=st.integers(min_value=1, max_value=40),
    arr1=sorted_list_strategy(40),
    arr2=sorted_list_strategy(40)
)
def test_median_between_middle_two(n, arr1, arr2):
    arr1 = arr1[:n]
    arr2 = arr2[:n]
    merged = sorted(arr1 + arr2)
    mid1 = merged[n - 1]
    mid2 = merged[n]
    med = get_median(arr1, arr2, n)
    assert mid1 <= med <= mid2
