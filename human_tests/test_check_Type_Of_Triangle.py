import sys
import os
import pytest
from hypothesis import given, assume, strategies as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from check_Type_Of_Triangle_buggy import check_Type_Of_Triangle
class TestCheckTypeOfTriangle:
    """Hypothesis-based property tests for check_Type_Of_Triangle function"""
    
    @given(
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000)
    )
    def test_result_is_string(self, a, b, c):
        """Result should always be a string"""
        assume(a + b > c and b + c > a and a + c > b)  # Valid triangle
        result = check_Type_Of_Triangle(a, b, c)
        assert isinstance(result, str)
    
    @given(
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000)
    )
    def test_result_is_valid_type(self, a, b, c):
        """Result should be one of three triangle types"""
        assume(a + b > c and b + c > a and a + c > b)  # Valid triangle
        result = check_Type_Of_Triangle(a, b, c)
        assert result in ["Right-angled Triangle", "Obtuse-angled Triangle", "Acute-angled Triangle"]
    
    @given(
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000)
    )
    def test_deterministic(self, a, b, c):
        """Function should return same result for same input"""
        assume(a + b > c and b + c > a and a + c > b)  # Valid triangle
        result1 = check_Type_Of_Triangle(a, b, c)
        result2 = check_Type_Of_Triangle(a, b, c)
        assert result1 == result2
    
    @given(
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000)
    )
    def test_order_independence(self, a, b, c):
        """Result should be same regardless of side order"""
        assume(a + b > c and b + c > a and a + c > b)  # Valid triangle
        result_abc = check_Type_Of_Triangle(a, b, c)
        result_bca = check_Type_Of_Triangle(b, c, a)
        result_cab = check_Type_Of_Triangle(c, a, b)
        assert result_abc == result_bca == result_cab
    
    @given(st.integers(min_value=1, max_value=500))
    def test_pythagorean_triple_is_right(self, n):
        """Pythagorean triples should be right-angled"""
        # Generate pythagorean triple: 3-4-5, 5-12-13, etc.
        a, b, c = 3 * n, 4 * n, 5 * n
        result = check_Type_Of_Triangle(a, b, c)
        assert result == "Right-angled Triangle"
    
    @given(st.integers(min_value=1, max_value=100))
    def test_equilateral_is_acute(self, side):
        """Equilateral triangles should be acute-angled"""
        result = check_Type_Of_Triangle(side, side, side)
        assert result == "Acute-angled Triangle"
    
    @given(st.integers(min_value=1, max_value=500))
    def test_verify_right_angle_condition(self, n):
        """Verify right angle: a² + b² = c²"""
        a, b = 3 * n, 4 * n
        c = int((a**2 + b**2)**0.5)
        assume(a**2 + b**2 == c**2)  # Perfect right triangle
        result = check_Type_Of_Triangle(a, b, c)
        assert result == "Right-angled Triangle"
    
    @given(
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=1, max_value=100)
    )
    def test_obtuse_condition(self, a, b):
        """Triangle where c² > a² + b² should be obtuse"""
        assume(a > 0 and b > 0)
        c = int((a**2 + b**2)**0.5) + 5  # Make c larger
        assume(a + b > c and b + c > a and a + c > b)  # Valid triangle
        assume(c**2 > a**2 + b**2)  # Obtuse condition
        result = check_Type_Of_Triangle(a, b, c)
        assert result == "Obtuse-angled Triangle"
    
    @given(
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000),
        st.integers(min_value=1, max_value=1000)
    )
    def test_manual_verification(self, a, b, c):
        """Manually verify triangle type classification"""
        assume(a + b > c and b + c > a and a + c > b)  # Valid triangle
        
        result = check_Type_Of_Triangle(a, b, c)
        
        sqa, sqb, sqc = a**2, b**2, c**2
        
        # Check right angle
        is_right = (sqa == sqb + sqc) or (sqb == sqa + sqc) or (sqc == sqa + sqb)
        
        # Check obtuse angle
        is_obtuse = (sqa > sqb + sqc) or (sqb > sqa + sqc) or (sqc > sqa + sqb)
        
        # Check acute angle
        is_acute = (sqa < sqb + sqc) and (sqb < sqa + sqc) and (sqc < sqa + sqb)
        
        if is_right:
            assert result == "Right-angled Triangle"
        elif is_obtuse:
            assert result == "Obtuse-angled Triangle"
        elif is_acute:
            assert result == "Acute-angled Triangle"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])