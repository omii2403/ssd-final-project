import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from get_Number_buggy import get_Number
def manual_expected(n, k):
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    arr = odds + evens
    return arr[k - 1]

@pytest.mark.parametrize("n,k", [
    (1, 1),          # smallest n
    (2, 1),          # first odd
    (2, 2),          # first even
    (3, 3),          # last element odd block boundary
    (8, 5),          # given example: expected = 2
    (9, 5),          # odd size odd-block
    (10, 6),         # mid even block
    (15, 1),         # first element
    (15, 8),         # boundary: last odd element (since odds = 8 values)
    (15, 9),         # first even after odd block
    (20, 20),        # final element in a larger sequence
    (7, 4),          # exact boundary at end of odd block (4th element is 7)
])
def test_get_Number(n, k):
    assert get_Number(n, k) == manual_expected(n, k)
