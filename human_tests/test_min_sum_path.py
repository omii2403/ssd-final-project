import os
import sys
from hypothesis import given, strategies as st

# Make buggy file importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from min_sum_path_buggy import min_sum_path


# -------------------------------------------------------------
# Ground truth spec (slow but correct)
# -------------------------------------------------------------
def spec(A):
    # Simple recursive DP using bottom-up fresh array
    dp = A[-1][:]
    for i in range(len(A) - 2, -1, -1):
        new_dp = [0] * (i + 1)
        for j in range(i + 1):
            new_dp[j] = A[i][j] + min(dp[j], dp[j + 1])
        dp = new_dp
    return dp[0]


# -------------------------------------------------------------
# 1. Agreement with spec
# -------------------------------------------------------------
@given(st.lists(st.lists(st.integers(min_value=-20, max_value=50), min_size=1), min_size=1, max_size=7))
def test_matches_spec(A):
    # Ensure triangle shape
    for i in range(len(A)):
        A[i] = A[i][:i+1]
        if len(A[i]) < i+1:
            A[i] = A[i] + [0] * (i + 1 - len(A[i]))
    assert min_sum_path(A) == spec(A)


# -------------------------------------------------------------
# 2. Single-row triangle → return its only element
# -------------------------------------------------------------
@given(st.integers(min_value=-100, max_value=100))
def test_single_row(x):
    assert min_sum_path([[x]]) == x


# -------------------------------------------------------------
# 3. If all numbers equal, result = depth * value
# -------------------------------------------------------------
@given(st.integers(min_value=-20, max_value=20), st.integers(min_value=1, max_value=8))
def test_uniform_triangle(val, depth):
    A = [[val] * (i + 1) for i in range(depth)]
    assert min_sum_path(A) == val * depth


# -------------------------------------------------------------
# 4. Negative numbers must be handled correctly
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=-10, max_value=10), min_size=1, max_size=8))
def test_negative_rows(row):
    A = [row[:1], row[:2], row[:3]]
    assert min_sum_path(A) == spec(A)


# -------------------------------------------------------------
# 5. Increasing all elements by constant k increases result by k*depth
# -------------------------------------------------------------
@given(
    st.integers(min_value=-5, max_value=5),
    st.integers(min_value=-50, max_value=50),
    st.integers(min_value=1, max_value=7)
)
def test_add_constant(k, base, depth):
    A = [[base + i + j for j in range(i + 1)] for i in range(depth)]
    A2 = [[x + k for x in row] for row in A]
    assert min_sum_path(A2) == min_sum_path(A) + k * depth


# -------------------------------------------------------------
# 6. Right-leaning triangle vs left-leaning
# -------------------------------------------------------------
def make_left(depth):
    return [[0] * (i + 1) for i in range(depth)]

def make_right(depth):
    return [[999] * i + [0] for i in range(depth)]

@given(st.integers(min_value=1, max_value=8))
def test_left_vs_right(depth):
    assert min_sum_path(make_left(depth)) == 0
    assert min_sum_path(make_right(depth)) == 0


# -------------------------------------------------------------
# 7. Path choices must be monotonic in columns
# -------------------------------------------------------------
@given(st.integers(min_value=1, max_value=6))
def test_triangle_width(depth):
    A = [[i] * (i + 1) for i in range(depth)]
    assert min_sum_path(A) == sum(range(depth))


# -------------------------------------------------------------
# 8. Large values must not overflow logic
# -------------------------------------------------------------
@given(st.lists(st.lists(st.integers(min_value=0, max_value=10**6), min_size=1), min_size=2, max_size=6))
def test_large_values(A):
    for i in range(len(A)):
        A[i] = A[i][:i+1]
        if len(A[i]) < i+1:
            A[i] += [0] * (i + 1 - len(A[i]))
    assert min_sum_path(A) == spec(A)


# -------------------------------------------------------------
# 9. If each row strictly decreases, leftmost path is optimal
# -------------------------------------------------------------
@given(st.integers(min_value=1, max_value=8))
def test_decreasing_rows(depth):
    A = [[depth - i + j for j in range(i + 1)] for i in range(depth)]
    assert min_sum_path(A) == spec(A)


# -------------------------------------------------------------
# 10. Random triangle must match spec
# -------------------------------------------------------------
@given(
    st.lists(
        st.lists(st.integers(min_value=-10, max_value=10), min_size=1),
        min_size=1, max_size=7
    )
)
def test_random_triangle(A):
    for i in range(len(A)):
        A[i] = A[i][:i+1]
        if len(A[i]) < i+1:
            A[i] += [0] * (i + 1 - len(A[i]))
    assert min_sum_path(A) == spec(A)
