import string
import pytest
from hypothesis import given, strategies as st, assume
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from pass_validity_buggy import pass_validity


class TestPassValidity:
    """Hypothesis-based property tests for pass_validity function"""
    
    @given(st.text(min_size=0, max_size=20))
    def test_result_is_boolean(self, p):
        """Result should always be a boolean"""
        result = pass_validity(p)
        assert isinstance(result, bool)
    
    @given(st.text(min_size=0, max_size=5))
    def test_too_short_returns_false(self, p):
        """Password shorter than 6 characters should return False"""
        assume(len(p) < 6)
        result = pass_validity(p)
        assert result == False
    
    @given(st.text(min_size=13, max_size=50))
    def test_too_long_returns_false(self, p):
        """Password longer than 12 characters should return False"""
        assume(len(p) > 12)
        result = pass_validity(p)
        assert result == False
    
    @given(st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Nd')), min_size=6, max_size=12))
    def test_no_lowercase_returns_false(self, p):
        """Password without lowercase should return False"""
        assume(not any(c.islower() for c in p))
        result = pass_validity(p)
        assert result == False
    
    @given(st.text(alphabet=st.characters(whitelist_categories=('Ll', 'Nd')), min_size=6, max_size=12))
    def test_no_uppercase_returns_false(self, p):
        """Password without uppercase should return False"""
        assume(not any(c.isupper() for c in p))
        result = pass_validity(p)
        assert result == False
    
    @given(st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll')), min_size=6, max_size=12))
    def test_no_digit_returns_false(self, p):
        """Password without digit should return False"""
        assume(not any(c.isdigit() for c in p))
        result = pass_validity(p)
        assert result == False
    
    @given(
        st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=3),
        st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=3),
        st.text(alphabet='0123456789', min_size=1, max_size=3)
    )
    def test_no_special_char_returns_false(self, lower, upper, digit):
        """Password without special character ($#@) should return False"""
        p = lower + upper + digit
        assume(6 <= len(p) <= 12)
        assume(not any(c in '$#@' for c in p))
        result = pass_validity(p)
        assert result == False
    
    @given(
        st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=2),
        st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=2),
        st.text(alphabet='0123456789', min_size=1, max_size=2),
        st.text(alphabet='$#@', min_size=1, max_size=2)
    )
    def test_with_whitespace_returns_false(self, lower, upper, digit, special):
        """Password with whitespace should return False"""
        p = lower + upper + digit + special + ' '
        assume(6 <= len(p) <= 12)
        result = pass_validity(p)
        assert result == False
    
    @given(
        st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=3),
        st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=3),
        st.text(alphabet='0123456789', min_size=1, max_size=3),
        st.text(alphabet='$#@', min_size=1, max_size=3)
    )
    def test_valid_password_returns_true(self, lower, upper, digit, special):
        """Valid password with all requirements should return True"""
        p = lower + upper + digit + special
        assume(6 <= len(p) <= 12)
        assume(not any(c.isspace() for c in p))
        result = pass_validity(p)
        assert result == True
    
    @given(st.text(min_size=0, max_size=20))
    def test_deterministic(self, p):
        """Function should return same result for same input"""
        result1 = pass_validity(p)
        result2 = pass_validity(p)
        assert result1 == result2
    
    @given(st.text(min_size=6, max_size=12))
    def test_all_requirements_checked(self, p):
        """Verify all requirements are properly checked"""
        result = pass_validity(p)
        
        has_lower = any(c in string.ascii_lowercase for c in p)
        has_upper = any(c in string.ascii_uppercase for c in p)

        
        has_digit = any(c in "0123456789" for c in p)

        has_special = any(c in '$#@' for c in p)
        has_space = any(c.isspace() for c in p)
        valid_length = 6 <= len(p) <= 12

        if result == True:
            assert has_lower and has_upper and has_digit and has_special and not has_space and valid_length
        else:
            assert not (has_lower and has_upper and has_digit and has_special and not has_space and valid_length)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])