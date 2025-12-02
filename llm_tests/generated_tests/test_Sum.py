import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from Sum_buggy import Sum


@pytest.mark.parametrize("n, expected", [
    (1, 0),              # no prime divisors
    (2, 2),              # smallest prime
    (3, 3),
    (4, 2),              # prime divisor 2
    (5, 5),
    (6, 5),              # 2 + 3
    (7, 7),
    (8, 2),              # only 2
    (9, 3),              # only 3
    (10, 7),             # 2 + 5
    (60, 10),            # example: 2 + 3 + 5 = 10
])
def test_sum_known(n, expected):
    assert Sum(n) == expected


@pytest.mark.parametrize("n", [
    11, 13, 17, 19, 23  # primes → sum should equal n itself
])
def test_prime_inputs(n):
    assert Sum(n) == n


@pytest.mark.parametrize("n", [
    97, 101, 149, 197   # large-ish primes
])
def test_large_primes(n):
    assert Sum(n) == n
