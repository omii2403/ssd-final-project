import pytest
from hypothesis import given, strategies as st, assume
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from max_run_uppercase_buggy import max_run_uppercase


class TestMaxRunUppercase:
    """Hypothesis-based property tests for max_run_uppercase function"""
    
    @given(st.text(min_size=0, max_size=1000))
    def test_result_is_non_negative(self, test_str):
        """Result should always be non-negative"""
        result = max_run_uppercase(test_str)
        assert result >= 0
    
    @given(st.text(min_size=0, max_size=1000))
    def test_result_is_integer(self, test_str):
        """Result should be an integer"""
        result = max_run_uppercase(test_str)
        assert isinstance(result, int)
    
    @given(st.text(min_size=0, max_size=1000))
    def test_result_not_exceeds_length(self, test_str):
        """Result should not exceed string length"""
        result = max_run_uppercase(test_str)
        assert result <= len(test_str)
    
    @given(st.text(alphabet=st.characters(whitelist_categories=('Lu',)), min_size=1, max_size=100))
    def test_all_uppercase_returns_length(self, test_str):
        """All uppercase string should return its length"""
        result = max_run_uppercase(test_str)
        assert result == len(test_str)
    
    @given(st.text(alphabet=st.characters(blacklist_categories=('Lu',)), min_size=1, max_size=100))
    def test_no_uppercase_returns_zero(self, test_str):
        """String with no uppercase should return 0"""
        result = max_run_uppercase(test_str)
        assert result == 0
    
    @given(st.text(min_size=0, max_size=1000))
    def test_deterministic(self, test_str):
        """Function should return same result for same input"""
        result1 = max_run_uppercase(test_str)
        result2 = max_run_uppercase(test_str)
        assert result1 == result2
    
    @given(st.text(min_size=1, max_size=500))
    def test_verify_by_manual_computation(self, test_str):
        """Verify result by manually finding max consecutive uppercase"""
        result = max_run_uppercase(test_str)
        
        # Manually compute max run
        max_run = 0
        current_run = 0
        for char in test_str:
            if char.isupper():
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 0
        
        assert result == max_run
    
    @given(
        st.text(alphabet=st.characters(blacklist_categories=('Lu',)), min_size=0, max_size=50),
        st.text(alphabet=st.characters(whitelist_categories=('Lu',)), min_size=1, max_size=50),
        st.text(alphabet=st.characters(blacklist_categories=('Lu',)), min_size=0, max_size=50)
    )
    def test_uppercase_run_in_middle(self, prefix, uppercase_run, suffix):
        """Test string with uppercase run in middle"""
        test_str = prefix + uppercase_run + suffix
        result = max_run_uppercase(test_str)
        assert result >= len(uppercase_run)
    
    @given(st.integers(min_value=1, max_value=100))
    def test_single_uppercase_at_end(self, n):
        """String ending with single uppercase should return 1 if no longer run"""
        test_str = 'a' * n + 'A'
        result = max_run_uppercase(test_str)
        assert result == 1
    
    @given(st.integers(min_value=1, max_value=100))
    def test_single_uppercase_at_start(self, n):
        """String starting with single uppercase"""
        test_str = 'A' + 'a' * n
        result = max_run_uppercase(test_str)
        assert result == 1
    
    def test_known_values(self):
        """Test against known values"""
        known_cases = {
            "": 0,
            "a": 0,
            "A": 1,
            "ABC": 3,
            "AbC": 1,
            "ABCabc": 3,
            "abcABC": 3,
            "aaBBccDD": 2,
            "AAaaBBBccDDDD": 4,
            "AAABBaaCCCC": 5,
            "aaaBBBBccDD": 4,
        }
        for test_str, expected in known_cases.items():
            assert max_run_uppercase(test_str) == expected, f"Failed for '{test_str}'"
    
    @given(st.integers(min_value=1, max_value=50), st.integers(min_value=1, max_value=50))
    def test_multiple_runs(self, run1_len, run2_len):
        """Test string with multiple uppercase runs"""
        test_str = 'A' * run1_len + 'a' + 'B' * run2_len
        result = max_run_uppercase(test_str)
        assert result == max(run1_len, run2_len)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])