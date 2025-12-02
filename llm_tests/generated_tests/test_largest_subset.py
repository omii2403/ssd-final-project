import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from largest_subset_buggy import largest_subset

@pytest.mark.parametrize("a, n, expected", [
    # 1. Single element → subset size is 1
    ([5], 1, 1),

    # 2. All identical elements
    ([2, 2, 2], 3, 3),

    # 3. Simple divisible chain
    ([1, 2, 4, 8], 4, 4),

    # 4. No number divides another except trivial self
    ([3, 5, 7, 11], 4, 1),

    # 5. Example from spec
    ([1, 3, 6, 13, 17, 18], 6, 4),

    # 6. Mixed divisible and non-divisible
    ([2, 3, 4, 9, 27], 5, 3),  # (3, 9, 27)

    # 7. Includes 1 (divides everything)
    ([1, 10, 20, 40], 4, 4),

    # 8. Duplicates + divisibility mixing
    ([4, 4, 8, 16], 4, 4),

    # 9. Unsorted input
    ([18, 6, 3, 1], 4, 4),

    # 10. Some divisible, some isolated
    ([2, 4, 7, 14, 28, 9], 6, 3),  # chain: 2,4,14,28

    # 11. Large gaps but one small chain
    ([5, 10, 20, 21, 22, 23], 6, 3),

])
def test_largest_subset(a, n, expected):
    assert largest_subset(a, n) == expected
