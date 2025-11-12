import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from find_max_val_buggy import find_max_val

@pytest.mark.parametrize("n, x, y, expected", [
    # Example from problem statement
    (15, 10, 5, 15),        # 15 % 10 == 5

    # Typical cases
    (8, 4, 3, 7),           # largest ≤8 with mod 4 == 3 is 7
    (7, 4, 3, 7),           # exact match n itself
    (9, 4, 3, 7),           # largest ≤9 with mod 4 == 3 is 7

    # No valid result (return -1)
    (2, 5, 3, -1),          # 3 > 2, no valid number
    (0, 5, 3, -1),          # 0 % 5 == 0, not 3 -> no valid
    (3, 7, 5, -1),          # 5 > 3, no valid number

    # y = 0 boundary cases
    (99, 10, 0, 90),        # 99 % 10 = 9 -> next lower multiple of 10 is 90
    (100, 10, 0, 100),      # exact multiple

    # x = 1 (always valid)
    (5, 1, 0, 5),           # all numbers %1 == 0

    # Large but fast test
    (100000, 97, 5, 99915), # computed via m = n - ((n - y) % x)
])
def test_find_max_val(n, x, y, expected):
    """
    find_max_val(n, x, y): should return the largest integer m such that
    0 <= m <= n and m % x == y, or -1 if no such m exists.
    """
    assert find_max_val(n, x, y) == expected

