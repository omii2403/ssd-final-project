import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from sum_of_odd_Factors_buggy import sum_of_odd_Factors


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),      # smallest positive integer
        (2, 1),      # smallest even number, only odd factor is 1
        (18, 13),    # odd factors {1, 3, 9}
        (21, 32),    # example from spec: odd factors {1, 3, 7, 21}
        (27, 40),    # odd square: 3^3, odd factors {1, 3, 9, 27}
        (45, 78),    # multiple odd primes and powers
        (64, 1),     # power of two, only odd factor is 1
        (72, 13),    # mix of even and odd, odd factors {1, 3, 9}
        (97, 98),    # odd prime, factors {1, 97}
        (105, 192),  # product of three odd primes
    ],
)
def test_sum_of_odd_Factors_various(n, expected):
    assert sum_of_odd_Factors(n) == expected
