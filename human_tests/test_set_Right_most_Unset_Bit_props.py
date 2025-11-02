import sys
import os
import pytest
import random
from hypothesis import given, strategies as st

# Add path to target_functions so we can import implementation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from set_Right_most_Unset_Bit_buggy import set_Right_most_Unset_Bit


# Property 1: Output should never be smaller than input
# (Because setting an unset bit can only increase or keep the number same)
def test_output_not_smaller():
    for _ in range(1000):
        n = random.randint(0, 100000)
        result = set_Right_most_Unset_Bit(n)
        assert result >= n


# Property 2: If all bits of n are already 1, output == n
def test_all_bits_set_property():
    # Construct numbers like 1, 3, 7, 15, 31, ... (all bits set)
    for i in range(1, 20):
        n = (1 << i) - 1
        result = set_Right_most_Unset_Bit(n)
        assert result == n, f"Failed for n={n}, got {result}"

# Property 3: The binary representation of result differs by exactly one bit
# (The rightmost 0 bit becomes 1)
def test_bit_difference():
    for _ in range(1000):
        n = random.randint(0, 100000)
        result = set_Right_most_Unset_Bit(n)
        # XOR gives positions where bits differ
        diff = n ^ result
        # Either no difference (if all bits set) or exactly one bit flipped
        assert diff == 0 or (diff & (diff - 1)) == 0


# Property 4: Edge cases - 0 and large number
def test_edge_cases():
    assert set_Right_most_Unset_Bit(0) == 1  # 0 → 1
    n = 2**20
    result = set_Right_most_Unset_Bit(n)
    assert result >= n

# Property 5: Only one new bit is set if not all bits are set
@given(st.integers(min_value=0, max_value=10**6))
def test_one_bit_set(n):
    result = set_Right_most_Unset_Bit(n)
    diff = result ^ n  # XOR to find changed bits
    if n & (n + 1) != 0:  # not all bits set
        assert diff & (diff - 1) == 0  # exactly one bit difference
    else:
        assert result == n  # if all bits set, output unchanged
