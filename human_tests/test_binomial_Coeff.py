import pytest
import math  # MISSING IMPORT - THIS WAS THE ISSUE
import sys, os
from hypothesis import given, strategies as st, assume
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from binomial_Coeff_buggy import binomial_Coeff, sum_Of_product


# Property 1: Binomial coefficient symmetry
@given(st.integers(min_value=0, max_value=20), st.integers(min_value=0, max_value=20))
def test_binomial_symmetry(n, k):
    """
    Pascal's Triangle symmetry: C(n, k) = C(n, n-k)
    """
    assume(0 <= k <= n)
    result1 = binomial_Coeff(n, k)
    result2 = binomial_Coeff(n, n - k)
    assert result1 == result2, \
        f"Symmetry failed: C({n},{k}) = {result1}, C({n},{n-k}) = {result2}"


# Property 2: Boundary conditions
@given(st.integers(min_value=0, max_value=30))
def test_binomial_boundary_nC0(n):
    """
    C(n, 0) must always equal 1 for any n >= 0
    """
    result = binomial_Coeff(n, 0)
    assert result == 1, f"C({n}, 0) should be 1, got {result}"


@given(st.integers(min_value=0, max_value=30))
def test_binomial_boundary_nCn(n):
    """
    C(n, n) must always equal 1 for any n >= 0
    """
    result = binomial_Coeff(n, n)
    assert result == 1, f"C({n}, {n}) should be 1, got {result}"


# Property 3: Pascal's identity
@given(st.integers(min_value=2, max_value=25), st.integers(min_value=1, max_value=20))
def test_pascals_identity(n, k):
    """
    Pascal's Identity: C(n, k) = C(n-1, k-1) + C(n-1, k)
    """
    assume(1 <= k <= n - 1)
    left = binomial_Coeff(n, k)
    right = binomial_Coeff(n - 1, k - 1) + binomial_Coeff(n - 1, k)
    assert left == right, \
        f"Pascal's identity failed: C({n},{k}) = {left}, but C({n-1},{k-1}) + C({n-1},{k}) = {right}"


# Property 4: Sum of row equals 2^n
@given(st.integers(min_value=0, max_value=15))
def test_binomial_row_sum(n):
    """
    Sum of all binomial coefficients in row n: ∑C(n,k) = 2^n
    """
    row_sum = sum(binomial_Coeff(n, k) for k in range(n + 1))
    expected = 2 ** n
    assert row_sum == expected, \
        f"Row {n} sum should be {expected}, got {row_sum}"


# Property 5: Oracle comparison with math.comb
@given(st.integers(min_value=0, max_value=30), st.integers(min_value=0, max_value=30))
def test_binomial_oracle(n, k):
    """
    Compare against Python's built-in math.comb for correctness
    """
    assume(0 <= k <= n)
    result = binomial_Coeff(n, k)
    expected = math.comb(n, k)
    assert result == expected, \
        f"C({n},{k}) = {result}, but math.comb gives {expected}"


# Property 6: Monotonicity in middle region
@given(st.integers(min_value=2, max_value=20))
def test_binomial_monotonic_increase(n):
    """
    For k < n/2, C(n, k) < C(n, k+1) (coefficients increase toward middle)
    """
    for k in range(min(n // 2, n)):
        if k + 1 <= n:
            current = binomial_Coeff(n, k)
            next_val = binomial_Coeff(n, k + 1)
            assert current <= next_val, \
                f"Monotonicity failed: C({n},{k}) = {current} should be <= C({n},{k+1}) = {next_val}"


# Property 7: Non-negativity
@given(st.integers(min_value=0, max_value=30), st.integers(min_value=0, max_value=30))
def test_binomial_non_negative(n, k):
    """
    All binomial coefficients must be positive integers
    """
    assume(0 <= k <= n)
    result = binomial_Coeff(n, k)
    assert result > 0, f"C({n},{k}) must be positive, got {result}"
    assert isinstance(result, int), f"C({n},{k}) must be integer, got {type(result)}"


# Property 8: sum_Of_product oracle test
@given(st.integers(min_value=1, max_value=15))
def test_sum_of_product_oracle(n):
    """
    sum_Of_product(n) should equal C(2n, n-1) using standard library
    """
    result = sum_Of_product(n)
    expected = math.comb(2 * n, n - 1)
    assert result == expected, \
        f"sum_Of_product({n}) = {result}, but C({2*n},{n-1}) = {expected}"


# Property 9: sum_Of_product increases with n
@given(st.integers(min_value=1, max_value=20))
def test_sum_of_product_increasing(n):
    """
    For n >= 1, sum_Of_product(n+1) > sum_Of_product(n)
    """
    current = sum_Of_product(n)
    if n < 20:
        next_val = sum_Of_product(n + 1)
        assert next_val > current, \
            f"sum_Of_product should increase: f({n}) = {current}, f({n+1}) = {next_val}"


# Property 10: Known test cases
def test_binomial_known_values():
    """
    Test against well-known binomial coefficient values
    """
    assert binomial_Coeff(5, 2) == 10
    assert binomial_Coeff(6, 3) == 20
    assert binomial_Coeff(4, 2) == 6
    assert binomial_Coeff(10, 5) == 252
    assert binomial_Coeff(0, 0) == 1
    assert binomial_Coeff(7, 0) == 1
    assert binomial_Coeff(7, 7) == 1


def test_sum_of_product_known_values():
    """
    Test sum_Of_product against known values
    """
    assert sum_Of_product(1) == 1   # C(2, 0) = 1
    assert sum_Of_product(2) == 4   # C(4, 1) = 4
    assert sum_Of_product(3) == 15  # C(6, 2) = 15
    assert sum_Of_product(4) == 56  # C(8, 3) = 56
    assert sum_Of_product(5) == 210 # C(10, 4) = 210
