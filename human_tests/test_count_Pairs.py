import sys
import os
import pytest
from hypothesis import given, assume, strategies as st

# Adjust import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from count_Pairs_buggy import count_Pairs


class TestCountPairs:
    """Hypothesis-based property tests for count_Pairs function"""

    @given(st.lists(st.integers(), min_size=0, max_size=300))
    def test_result_is_int(self, arr):
        """Function must always return an integer"""
        result = count_Pairs(arr, len(arr))
        assert isinstance(result, int)

    @given(st.lists(st.integers(), min_size=0, max_size=300))
    def test_zero_for_empty_or_single_element(self, arr):
        """Empty or 1-element list must have 0 pairs"""
        assume(len(arr) <= 1)
        assert count_Pairs(arr, len(arr)) == 0

    @given(st.lists(st.integers(), min_size=0, max_size=200))
    def test_manual_bruteforce_pair_count(self, arr):
        """Check pair count by brute-force computation"""
        n = len(arr)
        expected = 0

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    expected += 1

        result = count_Pairs(arr, n)
        assert result == expected

    @given(
        st.lists(st.integers(min_value=0, max_value=10), min_size=5, max_size=80)
    )
    def test_small_value_range_stress(self, arr):
        """High-duplicate lists should match brute-force count"""
        n = len(arr)
        expected = 0

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    expected += 1

        assert count_Pairs(arr, n) == expected

    @given(st.lists(st.integers(), min_size=2, max_size=200))
    def test_manual_verification(self, arr):
        """Cross-verify with mathematical combination formula"""
        n = len(arr)
        freq = {}

        # Count occurrences
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        # Expected = sum of nC2 for each value
        expected = 0
        for count in freq.values():
            if count >= 2:
                expected += count * (count - 1) // 2

        result = count_Pairs(arr, n)
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
