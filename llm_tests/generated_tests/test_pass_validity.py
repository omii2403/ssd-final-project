import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from pass_validity_buggy import pass_validity


@pytest.mark.parametrize("p, expected", [
    # Valid passwords
    ("Password@10", True),
    ("Aa1$aa", True),           # minimum length 6
    ("Aa1$aaaaaaa", True),      # within 6–12 length
    ("Ab9#XYz", True),
    ("Xy2@Qw3", True),

    # Length violations
    ("Aa1$aa1$aa1$aa", False),  # > 12 chars
    ("A1$a", False),            # < 6 chars

    # Missing required character types
    ("AAAAAA1$", False),        # no lowercase
    ("aaaaaa1$", False),        # no uppercase
    ("Aa$$$$aa", False),        # no digit
    ("Aa123456", False),        # no special char

    # Special char allowed cases
    ("Aa1#aa", True),
    ("Aa1@bb", True),
    ("Aa1$cc", True),

    # Whitespace invalid
    ("Aa1$ a", False),
    (" A1$aa", False),
    ("Aa1$aa\n", False),

    # Only ASCII special set allowed
    ("Aa1!aa", False),          # '!' not allowed
    ("Aa1%aa", False),          # '%' not allowed

    # Edge logical combinations
    ("ZZzz11$", True),
    ("Zz1@ 1", False),          # contains space
])
def test_pass_validity(p, expected):
    assert pass_validity(p) == expected
