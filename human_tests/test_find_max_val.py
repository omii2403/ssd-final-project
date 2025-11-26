import pytest
from hypothesis import given, strategies as st, assume
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from find_max_val_buggy import find_max_val


class TestFindMaxVal:
    """Hypothesis-based property tests for find_max_val function"""
    
    @given(
        st.integers(min_value=0, max_value=10000),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_result_in_valid_range(self, n, x, y):
        """Result should be in range [0, n] or -1"""
        assume(y < x)
        result = find_max_val(n, x, y)
        assert result == -1 or (0 <= result <= n)
    
    @given(
        st.integers(min_value=0, max_value=10000),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_modulo_property(self, n, x, y):
        """If result is not -1, then result % x should equal y"""
        assume(y < x)
        result = find_max_val(n, x, y)
        if result != -1:
            assert result % x == y
    
    @given(
        st.integers(min_value=0, max_value=10000),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_maximality(self, n, x, y):
        """If result k exists, no larger valid k should exist"""
        assume(y < x)
        result = find_max_val(n, x, y)
        if result != -1:
            # Check no larger value works
            for k in range(result + 1, n + 1):
                if k % x == y:
                    assert False, f"Found larger valid k={k} but function returned {result}"
    
    @given(
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_valid_solution_exists_when_y_in_range(self, x, y):
        """When n >= y and y < x, should find at least y as solution"""
        assume(y < x)
        n = y  # n is at least y
        result = find_max_val(n, x, y)
        assert result >= 0, f"Expected valid result when n={n}, x={x}, y={y}"
    
    @given(
        st.integers(min_value=0, max_value=10000),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_returns_minus_one_when_no_solution(self, n, x, y):
        """Should return -1 only when no valid k exists"""
        assume(y < x)
        result = find_max_val(n, x, y)
        if result == -1:
            # Verify no k in [0, n] satisfies k % x == y
            for k in range(n + 1):
                assert k % x != y, f"Found valid k={k} but function returned -1"
    
    @given(
        st.integers(min_value=0, max_value=10000),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_deterministic(self, n, x, y):
        """Function should return same result for same input"""
        assume(y < x)
        result1 = find_max_val(n, x, y)
        result2 = find_max_val(n, x, y)
        assert result1 == result2
    
    @given(
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=0, max_value=99)
    )
    def test_when_n_less_than_y(self, x, y):
        """When n < y, should return -1"""
        assume(y < x)
        assume(y > 0)
        n = y - 1
        result = find_max_val(n, x, y)
        assert result == -1
    
    @given(st.integers(min_value=1, max_value=100))
    def test_y_equals_zero(self, x):
        """When y=0, largest k should be the largest multiple of x <= n"""
        n = x * 10
        result = find_max_val(n, x, 0)
        assert result % x == 0
        assert result <= n
        assert result >= n - x + 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])