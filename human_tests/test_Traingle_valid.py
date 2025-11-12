from hypothesis import given, strategies as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from Traingle_valid_correct import check_Validity  # main function

# -----------------------------
# Basic Human Tests
# -----------------------------
def test_basic_cases():
    assert check_Validity(1, 2, 3) is False   # degenerate (1+2=3)
    assert check_Validity(2, 3, 5) is False   # degenerate (2+3=5)
    assert check_Validity(7, 10, 5) is True   # valid triangle

# -----------------------------
# Challenge Tests (Edge and Boundary)
# -----------------------------
def test_edge_cases():
    assert check_Validity(3, 4, 5) is True     # right triangle
    assert check_Validity(10, 1, 1) is False   # invalid (too long)
    assert check_Validity(5, 5, 9) is True     # valid isosceles
    assert check_Validity(5, 5, 10) is False   # degenerate
    assert check_Validity(0, 5, 5) is False    # zero side invalid
    assert check_Validity(-1, 4, 5) is False   # negative side invalid

# -----------------------------
# Hypothesis Property Tests
# -----------------------------
@given(st.integers(min_value=0, max_value=1000),
       st.integers(min_value=0, max_value=1000),
       st.integers(min_value=0, max_value=1000))
def test_triangle_inequality_property(a, b, c):
    # Property: True iff all triangle inequalities hold
    result = check_Validity(a, b, c)
    expected = (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a)
    assert result == expected


@given(st.integers(min_value=1, max_value=1000),
       st.integers(min_value=1, max_value=1000),
       st.integers(min_value=1, max_value=1000))
def test_symmetry_property(a, b, c):
    # Property: order of sides doesn’t affect validity
    results = {
        check_Validity(a, b, c),
        check_Validity(b, c, a),
        check_Validity(c, a, b)
    }
    assert len(results) == 1
