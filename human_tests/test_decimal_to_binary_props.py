from hypothesis import given, strategies as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from decimal_to_binary_buggy import decimal_To_Binary

@given(st.integers(min_value=0, max_value=10**6))
def test_binary_roundtrip(n):
    # property: converting the function output's decimal digits interpreted as base-2
    # should recover the original n
    b = decimal_To_Binary(n)
    # representation must be string of only 0/1 digits
    s = str(b)
    assert all(ch in '01' for ch in s)
    # interpreting s as base-2 should equal n
    assert int(s, 2) == n

@given(st.integers(min_value=0, max_value=10**6))
def test_monotonic_increase(n):
    # property: for non-negative n, as n increases, binary length is non-decreasing
    b = decimal_To_Binary(n)
    # length of binary digits equals floor(log2(n))+1 (for n>0)
    if n == 0:
        assert str(b) == '0'
    else:
        assert len(str(b)) == len(bin(n)[2:])
