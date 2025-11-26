import pytest
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../bug_portfolio")))

from check_Type_Of_Triangle_buggy import check_Type_Of_Triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # Classic right triangle
    (3, 4, 5, "Right-angled Triangle"),
    (5, 12, 13, "Right-angled Triangle"),
    (8, 15, 17, "Right-angled Triangle"),

    # Acute triangles
    (4, 5, 6, "Acute-angled Triangle"),
    (7, 8, 9, "Acute-angled Triangle"),
    (10, 10, 12, "Acute-angled Triangle"),

    # Obtuse triangles
    (2, 3, 4, "Obtuse-angled Triangle"),
    (6, 8, 10, "Right-angled Triangle"),   
    (5, 7, 10, "Obtuse-angled Triangle"),

    # Boundary-like valid triangle
    (1.5, 2.0, 2.4, "Acute-angled Triangle"),

    # Mixed order (ensure sorting / side selection bug exposed)
    (5, 3, 4, "Acute-angled Triangle"),     # permutation of (3,4,5)
])
def test_check_Type_Of_Triangle(a, b, c, expected):
    assert check_Type_Of_Triangle(a, b, c) == expected
