import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from get_median_buggy import get_median

@pytest.mark.parametrize("arr1, arr2, n, expected", [
    # 1. Simple 1-element arrays
    ([1], [2], 1, 1.5),

    # 2. Identical single-element arrays
    ([5], [5], 1, 5.0),

    # 3. Small interleaved arrays (even combined length = 4)
    ([1, 3], [2, 4], 2, 2.5),

    # 4. Example from the spec (n = 5)
    ([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5, 16.0),

    # 5. Negative and positive numbers cancel out to zero median
    ([-5, -3, -1], [1, 3, 5], 3, 0.0),

    # 6. All elements of arr1 are smaller than all of arr2 (boundary)
    ([1, 2, 3, 4], [10, 11, 12, 13], 4, 7.0),

    # 7. Arrays with all equal elements (duplicates)
    ([1, 1, 1], [1, 1, 1], 3, 1.0),

    # 8. Overlapping blocks producing a non-integer median
    ([100, 200, 300, 400], [150, 250, 350, 450], 4, 275.0),

    # 9. Float inputs (ensure function handles numeric types producing float median)
    ([1.5, 2.5], [3.5, 4.5], 2, 3.0),

    # 10. Many duplicates and interleaving (middle are equal)
    ([1, 2, 2, 2, 3], [2, 2, 3, 4, 5], 5, 2.0),
])
def test_get_median_various(arr1, arr2, n, expected):
    result = get_median(arr1, arr2, n)
    assert result == pytest.approx(expected)
