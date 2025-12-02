import pytest
from hypothesis import given, strategies as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from get_Number_buggy import get_Number

# Helper for expected output
def manual_expected(n, k):
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    arr = odds + evens
    return arr[k - 1]


# 1. Basic correctness
@given(
    n=st.integers(min_value=1, max_value=20_000),
    k=st.integers(min_value=1, max_value=20_000)
)
def test_basic_correctness(n, k):
    k = min(k, n)
    assert get_Number(n, k) == manual_expected(n, k)


# 2. Odds must appear first — SAMPLE check
@given(n=st.integers(min_value=1, max_value=20_000))
def test_odds_order(n):
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    
    # Only sample first 20 odd positions to keep runtime low
    sample_positions = odds[:20]
    for idx, val in enumerate(sample_positions, start=1):
        assert get_Number(n, idx) == val


# 3. Evens after odds — SAMPLE check
@given(n=st.integers(min_value=1, max_value=20_000))
def test_evens_order(n):
    odds_count = len([i for i in range(1, n + 1) if i % 2 == 1])
    evens = [i for i in range(1, n + 1) if i % 2 == 0]

    # Only sample first 20 evens
    for i, val in enumerate(evens[:20], start=odds_count + 1):
        assert get_Number(n, i) == val


# 4. Output must be between 1 and n
@given(
    n=st.integers(min_value=1, max_value=50_000),
    k=st.integers(min_value=1, max_value=50_000)
)
def test_output_range(n, k):
    k = min(k, n)
    out = get_Number(n, k)
    assert 1 <= out <= n


# 5. Odd block produces odd numbers — sampling
@given(
    n=st.integers(min_value=1, max_value=30_000),
    idx=st.integers(min_value=1, max_value=200)   # sample first 200 positions
)
def test_odd_block_parity(n, idx):
    odds_count = len([i for i in range(1, n + 1) if i % 2 == 1])
    if idx <= odds_count:
        assert get_Number(n, idx) % 2 == 1


# 6. Even block produces even numbers — sampling
@given(
    n=st.integers(min_value=1, max_value=30_000),
    offset=st.integers(min_value=1, max_value=200)
)
def test_even_block_parity(n, offset):
    odds_count = len([i for i in range(1, n + 1) if i % 2 == 1])
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    
    if offset <= len(evens):
        idx = odds_count + offset
        assert get_Number(n, idx) % 2 == 0


# 7. Small n exhaustive correctness
@given(
    n=st.integers(min_value=1, max_value=40),
    k=st.integers(min_value=1, max_value=40)
)
def test_small_exhaustive(n, k):
    k = min(k, n)
    assert get_Number(n, k) == manual_expected(n, k)


# 8. Monotonic inside odd block — sampling
@given(n=st.integers(min_value=1, max_value=20_000))
def test_monotonic_odds(n):
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    sample = min(len(odds), 20)

    for i in range(1, sample):
        assert get_Number(n, i) < get_Number(n, i + 1)


# 9. Monotonic inside even block — sampling
@given(n=st.integers(min_value=1, max_value=20_000))
def test_monotonic_evens(n):
    odds_count = len([i for i in range(1, n + 1) if i % 2 == 1])
    evens = [i for i in range(1, n + 1) if i % 2 == 0]

    sample = min(len(evens), 20)

    for i in range(1, sample):
        k1 = odds_count + i
        k2 = odds_count + i + 1
        assert get_Number(n, k1) < get_Number(n, k2)


# 10. First element must always be 1
@given(n=st.integers(min_value=1, max_value=50_000))
def test_first_element_always_one(n):
    assert get_Number(n, 1) == 1


# 11. Last element corresponds to last even or last odd
@given(n=st.integers(min_value=1, max_value=50_000))
def test_last_element_correct(n):
    expected = n if n % 2 == 0 else n - 1
    if n == 1:
        expected = 1
    assert get_Number(n, n) == expected


# 12. Structure preservation — sampling only!
@given(n=st.integers(min_value=1, max_value=50_000))
def test_block_sizes(n):
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    evens = [i for i in range(1, n + 1) if i % 2 == 0]

    # Check first 20 odds
    for i, val in enumerate(odds[:20], start=1):
        assert get_Number(n, i) == val

    # Check first 20 evens
    for i, val in enumerate(evens[:20], start=len(odds) + 1):
        assert get_Number(n, i) == val
