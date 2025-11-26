import pytest
from hypothesis import given, strategies as st, assume
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from sum_Of_Primes_buggy import sum_Of_Primes


class TestSumOfPrimes:
    """Hypothesis-based property tests for sum_Of_Primes function"""
    
    @given(st.integers(min_value=2, max_value=1000))
    def test_result_is_non_negative(self, n):
        """Sum of primes should always be non-negative"""
        result = sum_Of_Primes(n)
        assert result >= 0
    
    @given(st.integers(min_value=2, max_value=1000))
    def test_result_is_integer(self, n):
        """Result should be an integer"""
        result = sum_Of_Primes(n)
        assert isinstance(result, int)
    
    @given(st.integers(min_value=2, max_value=1000))
    def test_monotonic_increasing(self, n):
        """Sum should be monotonically non-decreasing as n increases"""
        assume(n < 1000)
        result_n = sum_Of_Primes(n)
        result_n_plus_1 = sum_Of_Primes(n + 1)
        assert result_n_plus_1 >= result_n
    
    @given(st.integers(min_value=2, max_value=100))
    def test_sum_less_than_triangular(self, n):
        """Sum of primes up to n should be less than sum of all numbers 1 to n"""
        result = sum_Of_Primes(n)
        triangular = n * (n + 1) // 2
        assert result <= triangular
    
    @given(st.integers(min_value=3, max_value=1000))
    def test_adding_prime_increases_sum(self, n):
        """If n is prime, sum(n) should be greater than sum(n-1)"""
        result_n = sum_Of_Primes(n)
        result_n_minus_1 = sum_Of_Primes(n - 1)
        
        # Check if n is prime
        is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
        
        if is_prime:
            assert result_n == result_n_minus_1 + n
        else:
            assert result_n == result_n_minus_1
    
    @given(st.integers(min_value=2, max_value=500))
    def test_deterministic(self, n):
        """Function should return same result for same input"""
        result1 = sum_Of_Primes(n)
        result2 = sum_Of_Primes(n)
        assert result1 == result2
    
    
    @given(st.integers(min_value=2, max_value=1000))
    def test_result_at_least_two(self, n):
        """Sum should be at least 2 (the first prime) for n >= 2"""
        result = sum_Of_Primes(n)
        assert result >= 2
    
    @given(st.integers(min_value=2, max_value=200))
    def test_verify_by_manual_computation(self, n):
        """Verify result by manually computing sum of primes"""
        result = sum_Of_Primes(n)
        
        # Manually find primes and sum them
        manual_sum = 0
        for num in range(2, n + 1):
            is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
            if is_prime:
                manual_sum += num
        
        assert result == manual_sum


if __name__ == "__main__":
    pytest.main([__file__, "-v"])