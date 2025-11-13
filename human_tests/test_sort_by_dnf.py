import pytest
from hypothesis import given, strategies as st, assume
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from sort_by_dnf_buggy import sort_by_dnf


class TestSortByDnf:
    """Hypothesis-based property tests for sort_by_dnf function"""
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_result_is_sorted(self, arr):
        """Result should be sorted in ascending order"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        assert result == sorted(result)
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_same_length(self, arr):
        """Result should have same length as input"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        assert len(result) == len(arr)
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_preserves_elements(self, arr):
        """Result should contain same elements as input"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        assert sorted(result) == sorted(arr)
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_count_preservation(self, arr):
        """Count of 0s, 1s, and 2s should be preserved"""
        n = len(arr)
        arr_copy = arr.copy()
        
        count_0_before = arr.count(0)
        count_1_before = arr.count(1)
        count_2_before = arr.count(2)
        
        result = sort_by_dnf(arr_copy, n)
        
        count_0_after = result.count(0)
        count_1_after = result.count(1)
        count_2_after = result.count(2)
        
        assert count_0_before == count_0_after
        assert count_1_before == count_1_after
        assert count_2_before == count_2_after
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_matches_builtin_sort(self, arr):
        """Result should match Python's built-in sort"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        expected = sorted(arr)
        assert result == expected
    
    @given(st.integers(min_value=1, max_value=100))
    def test_all_zeros_stays_same(self, size):
        """Array of all zeros should remain all zeros"""
        arr = [0] * size
        result = sort_by_dnf(arr, size)
        assert result == [0] * size
    
    @given(st.integers(min_value=1, max_value=100))
    def test_all_ones_stays_same(self, size):
        """Array of all ones should remain all ones"""
        arr = [1] * size
        result = sort_by_dnf(arr, size)
        assert result == [1] * size
    
    @given(st.integers(min_value=1, max_value=100))
    def test_all_twos_stays_same(self, size):
        """Array of all twos should remain all twos"""
        arr = [2] * size
        result = sort_by_dnf(arr, size)
        assert result == [2] * size
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=1, max_size=100))
    def test_already_sorted_stays_sorted(self, arr):
        """Already sorted array should remain sorted"""
        arr_sorted = sorted(arr)
        n = len(arr_sorted)
        result = sort_by_dnf(arr_sorted.copy(), n)
        assert result == arr_sorted
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=1, max_size=100))
    def test_reverse_sorted_gets_sorted(self, arr):
        """Reverse sorted array should be sorted correctly"""
        arr_reverse = sorted(arr, reverse=True)
        n = len(arr_reverse)
        result = sort_by_dnf(arr_reverse.copy(), n)
        assert result == sorted(arr_reverse)
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_zeros_come_first(self, arr):
        """All zeros should come before ones and twos"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        
        count_0 = result.count(0)
        if count_0 > 0:
            # All first count_0 elements should be 0
            assert all(result[i] == 0 for i in range(count_0))
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_twos_come_last(self, arr):
        """All twos should come after zeros and ones"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        
        count_2 = result.count(2)
        if count_2 > 0:
            # All last count_2 elements should be 2
            assert all(result[i] == 2 for i in range(len(result) - count_2, len(result)))
    
    def test_known_values(self):
        """Test against known values"""
        known_cases = [
            ([], 0, []),
            ([0], 1, [0]),
            ([1], 1, [1]),
            ([2], 1, [2]),
            ([2, 0, 1], 3, [0, 1, 2]),
            ([1, 0, 2], 3, [0, 1, 2]),
            ([2, 2, 0, 1, 1, 0], 6, [0, 0, 1, 1, 2, 2]),
            ([0, 1, 2, 0, 1, 2], 6, [0, 0, 1, 1, 2, 2]),
            ([2, 1, 0], 3, [0, 1, 2]),
            ([0, 0, 0, 1, 1, 2, 2, 2], 8, [0, 0, 0, 1, 1, 2, 2, 2]),
        ]
        for arr, n, expected in known_cases:
            result = sort_by_dnf(arr.copy(), n)
            assert result == expected, f"Failed for {arr}"
    
    @given(st.lists(st.integers(min_value=0, max_value=2), min_size=0, max_size=100))
    def test_contains_only_valid_values(self, arr):
        """Result should only contain 0, 1, or 2"""
        n = len(arr)
        arr_copy = arr.copy()
        result = sort_by_dnf(arr_copy, n)
        assert all(x in [0, 1, 2] for x in result)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])