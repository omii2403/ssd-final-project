import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))
from Traingle_valid_correct import check_Validity

def test_valid_scalene_triangle():
    assert check_Validity(7, 10, 5) is True  # typical valid triangle

def test_valid_equilateral_triangle():
    assert check_Validity(5, 5, 5) is True  # all sides equal

def test_valid_isosceles_triangle():
    assert check_Validity(4, 4, 5) is True  # two equal sides

def test_invalid_zero_side():
    assert check_Validity(0, 5, 5) is False  # side cannot be zero

def test_invalid_negative_side():
    assert check_Validity(-1, 2, 3) is False  # side cannot be negative

def test_invalid_flat_triangle():
    assert check_Validity(1, 2, 3) is False  # equality case fails triangle inequality

def test_invalid_one_large_side():
    assert check_Validity(10, 2, 3) is False  # one side too large

def test_valid_boundary_case():
    assert check_Validity(2, 3, 4) is True  # minimal valid non-degenerate triangle

def test_large_valid_triangle():
    assert check_Validity(1000000, 1000001, 999999) is True  # large numbers, valid triangle

def test_large_invalid_triangle():
    assert check_Validity(1000000, 1, 1) is False  # large side invalid

def test_all_equal_but_zero():
    assert check_Validity(0, 0, 0) is False  # all zero invalid

def test_almost_flat_but_valid():
    assert check_Validity(2, 3, 4) is True  # sum of smaller sides > third side
