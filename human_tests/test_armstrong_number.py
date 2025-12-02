import pytest
import os, sys
from hypothesis import given, strategies as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from armstrong_number_buggy import armstrong_number


# 1. All single–digit positive integers are Armstrong numbers
@given(n=st.integers(min_value=1, max_value=9))
def test_single_digit_numbers(n):
    assert armstrong_number(n) is True


# 2. Known Armstrong numbers must return True
@pytest.mark.parametrize("n", [153, 370, 371, 407, 9474])
def test_known_armstrong_numbers(n):
    assert armstrong_number(n) is True


# 3. Known non-Armstrong numbers must return False
@pytest.mark.parametrize("n", [10, 11, 12, 123, 200, 500, 999, 9475])
def test_known_non_armstrong_numbers(n):
    assert armstrong_number(n) is False


# 4. If all digits are the same (e.g., 222, 4444), only “1…1” can be Armstrong
@given(
    digit=st.integers(min_value=2, max_value=9),      # avoid 0 and 1
    length=st.integers(min_value=2, max_value=6)
)
def test_repeated_digit_numbers(digit, length):
    n = int(str(digit) * length)
    assert armstrong_number(n) is False


# 5. Powers of 10 except 1 return False (e.g., 10, 100, 1000)
@given(exp=st.integers(min_value=1, max_value=8))
def test_powers_of_ten(exp):
    n = 10 ** exp
    assert armstrong_number(n) is False


# 6. If number ends with 0 and is multi-digit → cannot be Armstrong
@given(
    n=st.integers(min_value=10, max_value=200000).filter(lambda x: str(x)[-1] == "0")
)
def test_numbers_ending_with_zero(n):
    assert armstrong_number(n) is False


# 7. All two-digit numbers are NOT Armstrong
@given(n=st.integers(min_value=10, max_value=99))
def test_two_digit_numbers(n):
    assert armstrong_number(n) is False


# 8. For 3-digit numbers, only {153, 370, 371, 407} are Armstrong
@given(n=st.integers(min_value=100, max_value=999))
def test_three_digit_numbers(n):
    if n in (153, 370, 371, 407):
        assert armstrong_number(n) is True
    else:
        assert armstrong_number(n) is False


# 9. For 4-digit numbers, only 9474 is Armstrong
@given(n=st.integers(min_value=1000, max_value=9999))
def test_four_digit_numbers(n):
    if n == 9474:
        assert armstrong_number(n) is True
    else:
        assert armstrong_number(n) is False


# 10. Numbers with strictly increasing digits (e.g., 1234) are never Armstrong
@given(
    d1=st.integers(1, 6),
    d2=st.integers(2, 7),
    d3=st.integers(3, 8),
    d4=st.integers(4, 9)
)
def test_strictly_increasing_digits(d1, d2, d3, d4):
    if d1 < d2 < d3 < d4:  # ensure strictly increasing
        n = int(f"{d1}{d2}{d3}{d4}")
        assert armstrong_number(n) is False


# 11. Random large number above known Armstrong limit → always False
@given(n=st.integers(min_value=10000, max_value=200000))
def test_large_numbers(n):
    # All known Armstrong numbers below 200k end at 9474
    assert armstrong_number(n) is False
