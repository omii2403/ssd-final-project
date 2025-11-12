import pytest
import math  # MISSING IMPORT - THIS WAS THE ISSUE
import sys, os
from hypothesis import given, strategies as st, assume, settings
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from bell_Number_buggy import bell_Number

# Property 1: Known Bell number values
def test_bell_known_values():
    """
    Test against well-known Bell numbers from OEIS A000110
    """
    assert bell_Number(0) == 1
    assert bell_Number(1) == 1
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15
    assert bell_Number(5) == 52
    assert bell_Number(6) == 203
    assert bell_Number(7) == 877


# Property 2: Bell numbers are strictly increasing for n > 0
@given(st.integers(min_value=1, max_value=15))
def test_bell_strictly_increasing(n):
    """
    B(n+1) > B(n) for all n >= 0
    """
    current = bell_Number(n)
    next_val = bell_Number(n + 1)
    assert next_val > current, \
        f"Bell numbers must increase: B({n}) = {current}, B({n+1}) = {next_val}"


# Property 3: Bell number growth rate (Dobinski's lower bound)
@given(st.integers(min_value=1, max_value=12))
def test_bell_lower_bound(n):
    """
    B(n) >= 2^(n-1) for n >= 1
    This is a known lower bound for Bell numbers
    """
    result = bell_Number(n)
    lower_bound = 2 ** (n - 1)
    assert result >= lower_bound, \
        f"B({n}) = {result} should be >= 2^({n}-1) = {lower_bound}"


# Property 4: First element equals last element of previous row
@given(st.integers(min_value=1, max_value=15))
def test_bell_triangle_property(n):
    """
    In the Bell triangle, bell[i][0] = bell[i-1][i-1]
    We can verify this by computing the triangle manually
    """
    bell = [[0 for i in range(n+2)] for j in range(n+2)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    
    # The nth Bell number should equal bell[n][0]
    assert bell[n][0] == bell_Number(n), \
        f"Triangle construction mismatch at n={n}"


# Property 5: Sum formula - Bell numbers via Stirling numbers
@given(st.integers(min_value=0, max_value=10))
@settings(max_examples=20)
def test_bell_stirling_sum(n):
    """
    B(n) = sum of Stirling numbers of the second kind S(n,k) for k=0 to n
    We'll use a simplified check: B(n) >= n for n >= 1
    """
    result = bell_Number(n)
    if n >= 1:
        assert result >= n, f"B({n}) = {result} should be >= {n}"


# Property 6: Non-negativity and integer type
@given(st.integers(min_value=0, max_value=20))
def test_bell_positive_integer(n):
    """
    All Bell numbers must be positive integers
    """
    result = bell_Number(n)
    assert result > 0, f"B({n}) must be positive, got {result}"
    assert isinstance(result, int), f"B({n}) must be integer, got {type(result)}"


# Property 7: Base case
def test_bell_base_case():
    """
    B(0) = 1 (there is exactly one way to partition the empty set)
    """
    assert bell_Number(0) == 1


# Property 8: Small values manual verification
def test_bell_small_values():
    """
    Manual verification of small Bell numbers
    B(2) = 2: {{1,2}} or {{1},{2}}
    B(3) = 5: five ways to partition {1,2,3}
    """
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5


# Property 9: Recurrence relation check
@given(st.integers(min_value=2, max_value=12))
def test_bell_triangle_recurrence(n):
    """
    Each element in Bell triangle: bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    Verify the computation is consistent
    """
    # Build triangle manually
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    
    # Result should match
    result = bell_Number(n)
    expected = bell[n][0]
    assert result == expected, f"B({n}) recurrence check failed: got {result}, expected {expected}"


# Property 10: Monotonic growth with specific ratio
@given(st.integers(min_value=2, max_value=10))
def test_bell_growth_ratio(n):
    """
    Bell numbers grow rapidly: B(n+1) > B(n)
    """
    b_n = bell_Number(n)
    b_n_plus_1 = bell_Number(n + 1)
    assert b_n_plus_1 > b_n, \
        f"Growth check: B({n+1}) = {b_n_plus_1} must be > B({n}) = {b_n}"
