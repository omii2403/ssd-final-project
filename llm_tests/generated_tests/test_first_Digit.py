import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from first_Digit_buggy import first_Digit

@pytest.mark.parametrize("n, expected", [
    (0, 1),       # 0! = 1 → first digit 1
    (1, 1),       # 1! = 1 → first digit 1
    (2, 2),       # 2! = 2 → first digit 2
    (3, 6),       # 3! = 6 → first digit 6
    (4, 2),       # 4! = 24 → first digit 2
    (5, 1),       # 5! = 120 → first digit 1
    (7, 5),       # 7! = 5040 → first digit 5
    (10, 3),      # 10! = 3628800 → first digit 3
    (20, 2),      # 20! = 2432902008176640000 → first digit 2
    (25, 1),      # 25! = 15511210043330985984000000 → first digit 1
    (50, 3),      # 50! starts with 3 (≈ 3.0414e64)
    (100, 9),     # 100! starts with 9 (≈ 9.3326e157)
])
def test_first_Digit(n, expected):
    assert first_Digit(n) == expected
