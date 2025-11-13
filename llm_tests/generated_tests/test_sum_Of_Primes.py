import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from sum_Of_Primes_buggy import sum_Of_Primes

@pytest.mark.parametrize("n, expected", [
    (1, 0),             # No primes ≤ 1
    (2, 2),             # Only 2
    (3, 5),             # 2 + 3 = 5
    (5, 10),            # 2 + 3 + 5 = 10
    (10, 17),           # 2 + 3 + 5 + 7 = 17
    (20, 77),           # primes ≤20
    (30, 129),          # primes ≤30
    (37, 197),          # primes ≤37
    (50, 328),          # primes ≤50
    (100, 1060),        # primes ≤100
    (101, 1161),        # 101 is prime
    (150, 2276),        # corrected
    (200, 4227),        # corrected
    (250, 5830),        # corrected
    (300, 8275),        # corrected
    (500, 21536),       # verified
    (1000, 76127),      # verified large case
])
def test_sum_Of_Primes(n, expected):
    assert sum_Of_Primes(n) == expected
