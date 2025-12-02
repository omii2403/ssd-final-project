import sys
import os
from hypothesis import given, strategies as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from Sum_buggy import Sum

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


# 1. Basic correctness using inline prime-divisor logic
@given(n=st.integers(min_value=1, max_value=5000))
def test_basic_correctness(n):
    expected = 0
    for d in range(2, n + 1):
        if n % d == 0 and is_prime(d):
            expected += d
    assert Sum(n) == expected


# 2. If n is prime → Sum(n) = n
@given(n=st.integers(min_value=2, max_value=5000))
def test_prime_value(n):
    if is_prime(n):
        assert Sum(n) == n


# 3. Perfect squares → only the base prime counted once
@given(p=st.integers(min_value=2, max_value=200))
def test_perfect_square(p):
    n = p * p
    if is_prime(p):
        assert Sum(n) == p


# 4. If n = p*q (two primes), sum should be p + q
@given(
    p=st.integers(min_value=2, max_value=200),
    q=st.integers(min_value=2, max_value=200)
)
def test_product_of_two_primes(p, q):
    if is_prime(p) and is_prime(q):
        n = p * q
        if n <= 5000:
            if p == q:
                assert Sum(n) == p
            else:
                assert Sum(n) == p + q


# 5. Sum(n) must never exceed n
@given(n=st.integers(min_value=1, max_value=5000))
def test_sum_never_exceeds_n(n):
    assert Sum(n) <= n


# 6. Sum(n) must always be ≥ 0
@given(n=st.integers(min_value=1, max_value=5000))
def test_non_negative(n):
    assert Sum(n) >= 0


# 7. n = 1 → output must be 0
def test_n_one():
    assert Sum(1) == 0


# 8. For even n > 2, 2 must be included in prime divisors
@given(n=st.integers(min_value=2, max_value=5000))
def test_even_number_contains_two(n):
    if n % 2 == 0:
        assert Sum(n) >= 2


# 9. For odd n with no prime divisors except itself (n prime)
@given(n=st.integers(min_value=3, max_value=5000))
def test_odd_prime_case(n):
    if is_prime(n):
        assert Sum(n) == n


# 10. Composite odd n without 2 should NOT include 2 in result
@given(n=st.integers(min_value=3, max_value=5000))
def test_no_two_for_odd(n):
    if n % 2 == 1:
        assert Sum(n) != 2  # odd numbers cannot have 2 as a divisor


# 11. If n has only one prime factor p (like p^k), Sum(n) = p
@given(
    p=st.integers(min_value=2, max_value=200),
    k=st.integers(min_value=2, max_value=5)
)
def test_prime_power(p, k):
    if is_prime(p):
        n = p ** k
        if n <= 5000:
            assert Sum(n) == p


# 12. Sum(n) for any n must equal the sum of distinct primes dividing it
@given(n=st.integers(min_value=1, max_value=5000))
def test_distinct_prime_divisor_property(n):
    distinct_sum = 0
    for d in range(2, n + 1):
        if n % d == 0 and is_prime(d):
            distinct_sum += d
    assert Sum(n) == distinct_sum
