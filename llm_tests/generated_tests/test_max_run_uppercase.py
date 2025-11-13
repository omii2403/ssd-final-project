import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from max_run_uppercase_buggy import max_run_uppercase

@pytest.mark.parametrize("s, expected", [
    # Basic cases
    ("A", 1),
    ("a", 0),
    ("AA", 2),
    ("aa", 0),

    # Mixed cases
    ("aA", 1),
    ("Aa", 1),
    ("aAaA", 1),

    # Given example
    ("aaAAABBBccDDDDDeE", 6),   # longest run = "DDDDD"

    # Multiple uppercase segments
    ("ABCdefGHIJk", 4),         # ABC=3, GHIJ=4
    ("abCDEfgHI", 3),           # CDE=3, HI=2

    # Entire uppercase
    ("ABCDEFG", 7),

    # No uppercase
    ("abcdefgh", 0),

    # Alternating letters
    ("AaAaAaAa", 1),

    # Ends with uppercase run
    ("abcXYZ", 3),
])
def test_max_run_uppercase(s, expected):
    assert max_run_uppercase(s) == expected
