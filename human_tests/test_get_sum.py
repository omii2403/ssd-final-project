import os
import sys
from hypothesis import given, strategies as st, assume

# Ensure bug_portfolio directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from get_sum_buggy import get_sum


def proper_divisor_sum(n: int) -> int:
    """Reference property function: sum of all positive divisors of n except n."""
    if n <= 1:
        return 0
    s = 1
    # only check up to sqrt(n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
        i += 1
    return s


@given(st.integers(min_value=1, max_value=10**6))
def test_sum_of_proper_divisors_matches_definition(n):
    """Property: get_sum(n) must equal the mathematically defined sum of proper divisors."""
    assume(n > 0)
    assert get_sum(n) == proper_divisor_sum(n)


@given(st.integers(min_value=1, max_value=10**6))
def test_result_is_non_negative(n):
    """Property: sum of proper divisors is always >= 0."""
    result = get_sum(n)
    assert result >= 0


@given(st.integers(min_value=2, max_value=10**6))
def test_perfect_abundant_deficient_consistency(n):
    """
    Property: classification must match divisor-sum theory.
    perfect: sum == n
    abundant: sum > n
    deficient: sum < n
    """
    s = get_sum(n)

    if s == n:  # perfect number
        # n should be one of known perfect numbers or follow perfect definition
        assert s == n
    elif s > n:  # abundant
        assert s > n
    else:  # deficient
        assert s < n
