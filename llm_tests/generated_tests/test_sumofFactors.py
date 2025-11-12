import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from sumofFactors_buggy import sumofFactors

@pytest.mark.parametrize("n, expected", [
    # Smallest possible input (only even factor is itself if even)
    (1, 0),            # No even factors
    (2, 2),            # Only even factor is 2
    (3, 0),            # Odd number, no even factors
    (4, 6),            # Even factors: 2, 4 -> sum = 6
    (6, 8),            # Even factors: 2, 6 -> sum = 8
    (8, 14),           # Even factors: 2, 4, 8 -> sum = 14
    (10, 12),          # Even factors: 2, 10 -> sum = 12
    (12, 24),          # Even factors: 2, 4, 6, 12 -> sum = 24
    (16, 30),          # Even factors: 2, 4, 8, 16 -> sum = 30
    (25, 0),           # Odd square number, no even factors
    (30, 48),          # Even factors: 2, 6, 10, 30 -> sum = 48
    (100, 186),        # Even factors: 2, 4, 10, 20, 50, 100 -> sum = 186
])
def test_sumofFactors(n, expected):
    assert sumofFactors(n) == expected
