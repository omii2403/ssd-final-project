import pytest
import os, sys
from hypothesis import given, strategies as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from largest_subset_buggy import largest_subset

# Strategy: list of positive integers
positive_list = st.lists(
    st.integers(min_value=1, max_value=100),
    min_size=1,
    max_size=10
)

# 1. Result is always at least 1 for non-empty lists
@given(a=positive_list)
def test_minimum_size(a):
    assert largest_subset(a, len(a)) >= 1


# 2. If all elements are identical → full list is valid
@given(
    value=st.integers(min_value=1, max_value=50),
    n=st.integers(min_value=1, max_value=10)
)
def test_identical_values(value, n):
    a = [value] * n
    assert largest_subset(a, n) == n


# 3. Strictly increasing primes → no divisibility → result = 1
@given(n=st.integers(min_value=1, max_value=5))
def test_strict_primes(n):
    # fixed list of odd primes (no divisibility between them)
    primes = [3, 5, 11, 17, 23][:n]
    assert largest_subset(primes, n) == 1


# 4. If list contains 1 → 1 can join any valid chain (≥2 elements)
@given(a=st.lists(st.integers(min_value=2, max_value=100), min_size=1, max_size=9))
def test_including_one(a):
    a.append(1)
    assert largest_subset(a, len(a)) >= 2


# 5. Perfectly divisible chain → entire list is valid
@given(
    start=st.integers(min_value=1, max_value=5),
    n=st.integers(min_value=1, max_value=7)
)
def test_perfect_chain(start, n):
    a = [start * (2 ** i) for i in range(n)]
    assert largest_subset(a, n) == n


# 6. Duplicate chain mixed with invalid values → largest subset = duplicates
@given(
    base=st.integers(min_value=2, max_value=20),
    k=st.integers(min_value=2, max_value=8)
)
def test_duplicate_chain(base, k):
    a = [base] * k + [base + 1]  # base+1 not divisible by base
    assert largest_subset(a, len(a)) == k


# 7. Result never exceeds n
@given(a=positive_list)
def test_upper_bound(a):
    assert largest_subset(a, len(a)) <= len(a)


# 8. Single element → result = 1
@given(x=st.integers(min_value=1, max_value=200))
def test_single_element(x):
    assert largest_subset([x], 1) == 1


# 9. All values are multiples of a base number → full list valid
@given(
    base=st.integers(min_value=1, max_value=10),
    n=st.integers(min_value=1, max_value=8)
)
def test_all_multiples(base, n):
    a = [base * (i + 1) for i in range(n)]
    result = largest_subset(a, n)

    if n == 1:
        assert result == 1
    else:
        # base divides all elements, so at least 2 elements can chain
        assert result >= 2
        # cannot exceed list length
        assert result <= n



# 10. Powers of two always form a valid chain
@given(n=st.integers(min_value=1, max_value=8))
def test_powers_of_two(n):
    a = [2 ** i for i in range(n)]
    assert largest_subset(a, n) == n


# 11. Smallest element repeated k times → result ≥ k
@given(a=positive_list)
def test_smallest_repetition(a):
    smallest = min(a)
    k = a.count(smallest)
    assert largest_subset(a, len(a)) >= k
