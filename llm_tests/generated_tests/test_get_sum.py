import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from get_sum_buggy import get_sum

@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0.0),
        (2, 1.0),
        (3, 1.0),
        (6, 6.0),
        (10, 8.0),
        (12, 16.0),
        (28, 28.0),
        (36, 55.0),
        (49, 8.0),
        (97, 1.0),
        (121, 12.0),
    ],
)
def test_small_and_typical_values(n, expected):
    assert get_sum(n) == pytest.approx(expected)

def test_large_composite_number_100000():
    assert get_sum(100000) == pytest.approx(146078.0)

def test_large_prime_number_99991():
    assert get_sum(99991) == pytest.approx(1.0)

@pytest.mark.parametrize("n", [1, 2, 6, 10, 28, 36, 49, 121, 100000])
def test_proper_divisor_sum_logic(n):
    result = get_sum(n)
    if n == 1:
        assert result == pytest.approx(0.0)
    else:
        assert result < n
