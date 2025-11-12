import sys
import os
from hypothesis import given, strategies as st

# Ensure target_functions directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from sumofFactors_buggy import sumofFactors

# -------------------------------------------------------
# Property 1: The result of sumofFactors(n) is always a non-negative integer.
# -------------------------------------------------------
@given(st.integers(min_value=1, max_value=100_000))
def test_sumofFactors_non_negative_integer(n):
    res = sumofFactors(n)
    assert isinstance(res, int)
    assert res >= 0


# -------------------------------------------------------
# Property 2: For any odd n, the sum of even factors should be zero.
# -------------------------------------------------------
@given(st.integers(min_value=1, max_value=100_000).filter(lambda x: x % 2 == 1))
def test_sumofFactors_odd_numbers_zero(n):
    assert sumofFactors(n) == 0


# -------------------------------------------------------
# Property 3: For even n, sumofFactors(n) must be at least n 
# (because n is an even factor of itself).
# -------------------------------------------------------
@given(st.integers(min_value=2, max_value=100_000).filter(lambda x: x % 2 == 0))
def test_sumofFactors_includes_self(n):
    assert sumofFactors(n) >= n


# -------------------------------------------------------
# Property 4: The output of sumofFactors(n) must always be even (or zero).
# -------------------------------------------------------
@given(st.integers(min_value=1, max_value=100_000))
def test_sumofFactors_result_even_or_zero(n):
    res = sumofFactors(n)
    assert res % 2 == 0


# -------------------------------------------------------
# Property 5: sumofFactors should be monotonic with respect to divisibility.
# If a divides b and both are even, then sumofFactors(a) <= sumofFactors(b).
# -------------------------------------------------------
@given(
    st.integers(min_value=2, max_value=1000).filter(lambda x: x % 2 == 0),
    st.integers(min_value=1, max_value=100)
)
def test_sumofFactors_monotonic_with_divisibility(a, k):
    b = a * k
    assert sumofFactors(a) <= sumofFactors(b)
