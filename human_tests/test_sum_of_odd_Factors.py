import os
import sys
from hypothesis import given, strategies as st

# Allow importing buggy implementation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from sum_of_odd_Factors_buggy import sum_of_odd_Factors


  
# Helper: canonical slow reference implementation (ground truth)
  
def spec(n):
    return sum(d for d in range(1, n + 1) if d % 2 == 1 and n % d == 0)


  
# 1. Specification Agreement (fundamental correctness property)
  
@given(st.integers(min_value=1, max_value=5000))
def test_matches_spec(n):
    assert sum_of_odd_Factors(n) == spec(n)


  
# 2. Invariance under multiplying by powers of two
#    Odd factors do not change when n is multiplied by 2^k
  
@given(
    st.integers(min_value=1, max_value=2000),
    st.integers(min_value=0, max_value=10)
)
def test_invariance_under_powers_of_two(n, k):
    assert sum_of_odd_Factors(n) == sum_of_odd_Factors(n * (2 ** k))


  
# 3. Removing existing powers of two should not change result
  
@given(
    st.integers(min_value=1, max_value=2000),
    st.integers(min_value=0, max_value=10)
)
def test_idempotence_under_stripping_twos(n, k):
    value = n * (2 ** k)
    assert sum_of_odd_Factors(value) == sum_of_odd_Factors(n)


  
# 4. Result must always be odd (sum of odd divisors)
  
@given(st.integers(min_value=1, max_value=5000))
def test_result_is_odd(n):
    assert sum_of_odd_Factors(n) % 2 == 1


  
# 5. For odd n: result must be >= n (because n itself is included)
  
@given(st.integers(min_value=1, max_value=5000))
def test_for_odd_n_output_ge_n(n):
    if n % 2 == 1:
        assert sum_of_odd_Factors(n) >= n


  
# 6. If n is odd prime, result must be 1 + n
  
@given(st.integers(min_value=3, max_value=3000))
def test_for_odd_prime(n):
    # primality check for odd numbers
    if n % 2 == 1 and all(n % d for d in range(3, int(n**0.5) + 1, 2)):
        assert sum_of_odd_Factors(n) == 1 + n


  
# 7. Sum of odd factors of n must be <= n + sum(all proper odd divisors)
#    Simple upper bound property (sanity rule)
  
@given(st.integers(min_value=1, max_value=3000))
def test_upper_bound(n):
    s = sum_of_odd_Factors(n)
    # Upper bound: cannot exceed sum of all odd numbers <= n
    max_possible = sum(i for i in range(1, n + 1, 2))
    assert s <= max_possible


  
# 8. If a divides b → odd-factor-sum(b) >= odd-factor-sum(a)
  
@given(
    st.integers(min_value=1, max_value=2000),
    st.integers(min_value=1, max_value=20)
)
def test_divisor_monotonicity(a, k):
    b = a * k
    assert sum_of_odd_Factors(b) >= sum_of_odd_Factors(a)


  
# 9. Multiplicative property for coprime odd numbers:
#    sum_odd_factors(a * b) = sum_odd_factors(a) * sum_odd_factors(b)
  
@given(
    st.integers(min_value=1, max_value=500),
    st.integers(min_value=1, max_value=500)
)
def test_multiplicativity_for_coprime_odds(a, b):
    if a % 2 == 1 and b % 2 == 1:
        # check coprime
        from math import gcd
        if gcd(a, b) == 1:
            assert sum_of_odd_Factors(a * b) == sum_of_odd_Factors(a) * sum_of_odd_Factors(b)


  
# 10. For perfect squares of odd numbers:
#     odd factors should include sqrt(n)
  
@given(st.integers(min_value=1, max_value=1000))
def test_perfect_square_inclusion(k):
    n = (2*k + 1) ** 2  # odd perfect square
    sf = sum_of_odd_Factors(n)
    # Factor must include the odd square root
    root = 2*k + 1
    assert sf >= root
