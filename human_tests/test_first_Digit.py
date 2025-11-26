import sys
import os
from hypothesis import given, strategies as st
import math
import pytest

# Ensure target_functions directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from first_Digit_buggy import first_Digit

# def first_Digit(n):
#     fact = 1
#     for i in range(2, n + 1):
#         fact = fact * i
#         while (fact % 10 == 0):
#             fact = int(fact / 10)
#     while (fact >= 10):
#         fact = int(fact / 10)
#     return math.floor(fact)


class TestFirstDigit:
    """Hypothesis-based property tests for first_Digit function"""
    
    @given(st.integers(min_value=1, max_value=100))
    def test_result_is_single_digit(self, n):
        """The result should always be a single digit (1-9)"""
        result = first_Digit(n)
        assert 1 <= result <= 9, f"Expected single digit, got {result}"
    
    @given(st.integers(min_value=1, max_value=100))
    def test_result_is_integer(self, n):
        """The result should always be an integer"""
        result = first_Digit(n)
        assert isinstance(result, int), f"Expected integer, got {type(result)}"
    
    @given(st.integers(min_value=1, max_value=100))
    def test_matches_mathematical_factorial(self, n):
        """Result should match the first digit of math.factorial(n)"""
        result = first_Digit(n)
        expected = int(str(math.factorial(n))[0])
        assert result == expected, f"For {n}!, expected {expected}, got {result}"
    
    @given(st.integers(min_value=1, max_value=20))
    def test_small_factorials_exhaustive(self, n):
        """Verify against known factorial values for small n"""
        result = first_Digit(n)
        factorial_str = str(math.factorial(n))
        expected = int(factorial_str[0])
        assert result == expected
    
    @given(st.integers(min_value=2, max_value=50))
    def test_consecutive_numbers(self, n):
        """Test that consecutive factorials can have different first digits"""
        result_n = first_Digit(n)
        result_n_plus_1 = first_Digit(n + 1)
        # Both should be valid digits
        assert 1 <= result_n <= 9
        assert 1 <= result_n_plus_1 <= 9
    
    def test_known_values(self):
        """Test against known factorial first digits"""
        known_cases = {
            1: 1,   # 1! = 1
            2: 2,   # 2! = 2
            3: 6,   # 3! = 6
            4: 2,   # 4! = 24
            5: 1,   # 5! = 120
            6: 7,   # 6! = 720
            7: 5,   # 7! = 5040
            8: 4,   # 8! = 40320
            9: 3,   # 9! = 362880
            10: 3,  # 10! = 3628800
            20: 2,  # 20! = 2432902008176640000
            25: 1,  # 25! starts with 1
        }
        for n, expected in known_cases.items():
            assert first_Digit(n) == expected, f"Failed for {n}!"
    
    @given(st.integers(min_value=1, max_value=100))
    def test_function_deterministic(self, n):
        """Function should return same result for same input"""
        result1 = first_Digit(n)
        result2 = first_Digit(n)
        assert result1 == result2, "Function should be deterministic"
    
    @given(st.integers(min_value=1, max_value=15))
    def test_result_type_consistency(self, n):
        """Result should be consistently of type int"""
        result = first_Digit(n)
        assert type(result) == int, f"Expected int type, got {type(result)}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])