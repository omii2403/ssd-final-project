import os, sys
from hypothesis import given, strategies as st

# Ensure target_functions directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from set_Right_most_Unset_Bit_buggy import set_Right_most_Unset_Bit

# Property 1: Result should be >= n (setting a bit cannot decrease the number)
@given(st.integers(min_value=0, max_value=10**6))
def test_non_decreasing(n):
    result = set_Right_most_Unset_Bit(n)
    assert result >= n


# Property 2: If n == 0, result must be 1 (bug-revealing case)
@given(st.just(0))
def test_zero_case(n):
    result = set_Right_most_Unset_Bit(n)
    assert result == 1


# Property 3: If all bits up to the highest 1 are set (e.g., 1, 3, 7, 15, ...), result == n
# because there’s no unset bit to set.
@given(st.integers(min_value=1, max_value=10**6))
def test_all_bits_set_no_change(n):
    # Create number with all lower bits set: e.g., 7 (111) or 15 (1111)
    all_bits_set = (1 << n.bit_length()) - 1
    result = set_Right_most_Unset_Bit(all_bits_set)
    assert result == all_bits_set


# Property 4: Setting the rightmost 0 bit of n should flip exactly one bit from 0 to 1
@given(st.integers(min_value=0, max_value=10**6))
def test_exactly_one_bit_flipped(n):
    result = set_Right_most_Unset_Bit(n)
    # XOR highlights changed bits; for valid case, exactly one bit should flip
    diff_bits = bin(n ^ result).count('1')
    # Exception: if no unset bit exists (i.e., result == n)
    if result != n:
        assert diff_bits == 1


# Property 5: For even n, the result must be n + 1
# Because the rightmost bit (0) is unset and will be set to 1.
@given(st.integers(min_value=0, max_value=10**6).filter(lambda x: x % 2 == 0))
def test_even_numbers_increase_by_one(n):
    result = set_Right_most_Unset_Bit(n)
    assert result == n + 1
