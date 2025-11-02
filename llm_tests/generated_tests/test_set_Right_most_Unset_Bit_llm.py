import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from set_Right_most_Unset_Bit_buggy import set_Right_most_Unset_Bit

@pytest.mark.parametrize("n, expected", [
    (0, 1),        # 0 -> 1 (no bits set)
    (1, 1),        # 11 -> 1
    (2, 3),        # 10 -> 11
    (3, 3),        # 11 -> 11 (all bits set)
    (4, 5),        # 100 -> 101
    (5, 7),        # 101 -> 111
    (6, 7),        # 110 -> 111
    (7, 7),        # 111 -> 111 (all bits set)
    (8, 9),        # 1000 -> 1001
    (10, 11),      # 1010 -> 1011 (example)
    (15, 15),      # 1111 -> 1111 (all bits set)
    (18, 19),      # 10010 -> 10011
])
def test_set_right_most_unset_bit(n, expected):
    assert set_Right_most_Unset_Bit(n) == expected


def test_large_number_pattern():
    # 1023 (1111111111) all bits set -> unchanged
    assert set_Right_most_Unset_Bit(1023) == 1023

    # 1022 (1111111110) rightmost unset bit at LSB -> set it -> 1023
    assert set_Right_most_Unset_Bit(1022) == 1023
