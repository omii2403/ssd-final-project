import pytest
from hypothesis import given, strategies as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from generate_matrix_buggy import generate_matrix


class TestGenerateMatrix:
    """Hypothesis-based property tests for generate_matrix"""

    @given(st.integers(min_value=-50, max_value=0))
    def test_non_positive_n_returns_empty(self, n):
        """For n <= 0, the function must return an empty list."""
        assert generate_matrix(n) == []

    @given(st.integers(min_value=1, max_value=50))
    def test_matrix_shape(self, n):
        """Matrix must be n x n."""
        m = generate_matrix(n)
        assert len(m) == n
        assert all(len(row) == n for row in m)

    @given(st.integers(min_value=1, max_value=50))
    def test_contains_all_values_from_1_to_n2(self, n):
        """Matrix must contain exactly numbers 1 to n*n."""
        m = generate_matrix(n)
        flat = [x for row in m for x in row]
        assert sorted(flat) == list(range(1, n*n + 1))

    @given(st.integers(min_value=1, max_value=50))
    def test_each_value_unique(self, n):
        """All values must be unique."""
        m = generate_matrix(n)
        flat = [x for row in m for x in row]
        assert len(flat) == len(set(flat))

    @given(st.integers(min_value=1, max_value=50))
    def test_deterministic(self, n):
        """Calling generate_matrix twice with same n must give same result."""
        assert generate_matrix(n) == generate_matrix(n)

    @given(st.integers(min_value=1, max_value=30))
    def test_spiral_property_border_correct(self, n):
        """
        Basic spiral property:
        - Top-left must be 1.
        - Bottom-right must be n*n or near the end of spiral.
        """
        m = generate_matrix(n)
        assert m[0][0] == 1

        # bottom-right should be a high number (end of spiral)
        assert 1 <= m[-1][-1] <= n*n

    @given(st.integers(min_value=1, max_value=40))
    def test_values_in_valid_range(self, n):
        """All matrix values must lie between 1 and n*n."""
        m = generate_matrix(n)
        flat = [x for row in m for x in row]
        assert all(1 <= v <= n*n for v in flat)

    @given(st.integers(min_value=1, max_value=40))
    def test_no_row_all_zero(self, n):
        """Since initialization uses [row[:] for row in [[0]*n]*n], ensure no unfilled row remains."""
        m = generate_matrix(n)
        assert all(any(v != 0 for v in row) for row in m)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
