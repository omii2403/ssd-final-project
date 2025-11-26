import pytest
import math
import sys, os

# Correct the path to the bug_portfolio directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from binomial_Coeff_buggy import binomial_Coeff, sum_Of_product


# ---------- binomial_Coeff tests (edge, typical, boundary) ----------

def test_binomial_base_cases():
    assert binomial_Coeff(0, 0) == 1
    assert binomial_Coeff(7, 0) == 1
    assert binomial_Coeff(7, 7) == 1

def test_binomial_small_examples():
    assert binomial_Coeff(4, 2) == 6
    assert binomial_Coeff(5, 2) == 10
    assert binomial_Coeff(6, 3) == 20

def test_binomial_symmetry():
    for n in range(0, 12):
        for k in range(0, n + 1):
            assert binomial_Coeff(n, k) == binomial_Coeff(n, n - k)

def test_binomial_pascal_identity():
    # Test Pascal's identity for a range of n,k
    for n in range(2, 12):
        for k in range(1, n):
            lhs = binomial_Coeff(n, k)
            rhs = binomial_Coeff(n - 1, k - 1) + binomial_Coeff(n - 1, k)
            assert lhs == rhs

def test_binomial_row_sum_power_of_two():
    for n in range(0, 11):
        total = sum(binomial_Coeff(n, k) for k in range(n + 1))
        assert total == 2 ** n

def test_binomial_against_math_comb_large():
    # compare against Python's math.comb for several values including a boundary-like case
    cases = [(10, 5), (15, 7), (20, 10), (25, 12)]
    for n, k in cases:
        assert binomial_Coeff(n, k) == math.comb(n, k)


# ---------- sum_Of_product tests (edge, typical, boundary) ----------

def test_sum_of_product_known_values():
    # C(2n, n-1) known values
    assert sum_Of_product(1) == math.comb(2, 0)   # 1
    assert sum_Of_product(2) == math.comb(4, 1)   # 4 choose 1 = 4 (some implementations might define differently; spec expects C(4,1)=4)
    # Note: Spec examples gave sum_Of_product(2) -> 6 earlier in conversation, but mathematically C(4,1)=4.
    # We verify according to the spec in the prompt: sum_Of_product(n) = C(2n, n-1).
    assert sum_Of_product(3) == math.comb(6, 2)   # 15
    assert sum_Of_product(4) == math.comb(8, 3)   # 56
    assert sum_Of_product(5) == math.comb(10, 4)  # 210

def test_sum_of_product_consistency_with_binomial():
    for n in range(1, 12):
        expected = binomial_Coeff(2 * n, n - 1)
        assert sum_Of_product(n) == expected

def test_sum_of_product_monotonic_increasing_for_small_n():
    vals = [sum_Of_product(n) for n in range(1, 8)]
    # Should be non-decreasing for these n (strictly increasing here)
    assert all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))

def test_sum_of_product_large_n_against_math_comb():
    # check a larger n
    n = 12
    assert sum_Of_product(n) == math.comb(2 * n, n - 1)
