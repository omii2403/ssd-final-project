import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from decimal_to_binary_buggy import decimal_To_Binary

@pytest.mark.parametrize("N, expected", [
    (0, 0),            # smallest input
    (1, 1),            # simple case
    (2, 10),           # binary of 2 is '10'
    (3, 11),           # consecutive ones
    (4, 100),          # power of two
    (5, 101),          # example given
    (7, 111),          # all ones in binary
    (8, 1000),         # next power of two
    (15, 1111),        # four bits all set
    (16, 10000),       # boundary between bit lengths
    (31, 11111),       # five bits all set
    (255, 11111111),   # 8-bit all ones
])
def test_decimal_to_binary(N, expected):
    assert decimal_To_Binary(N) == expected


def test_large_number():
    # binary of 1023 is 10 consecutive 1s
    assert decimal_To_Binary(1023) == int("1" * 10)

def test_powers_of_two_pattern():
    # Verify pattern for powers of two: 2^k -> 1 followed by k zeros
    for k in range(0, 10):
        N = 2 ** k
        expected = int("1" + "0" * k)
        assert decimal_To_Binary(N) == expected
