import pytest
import math
import sys
import os

# Correct the path to the bug_portfolio directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../bug_portfolio")))

from bell_Number_buggy import bell_Number




def test_base_case_zero():
    """Test B(0) = 1 - one way to partition empty set."""
    assert bell_Number(0) == 1


def test_base_case_one():
    """Test B(1) = 1 - one way to partition single element."""
    assert bell_Number(1) == 1


def test_example_2():
    """Test B(2) = 2 - partitions: {{1,2}}, {{1},{2}}."""
    assert bell_Number(2) == 2


def test_example_3():
    """Test B(3) = 5."""
    assert bell_Number(3) == 5


def test_example_4():
    """Test B(4) = 15."""
    assert bell_Number(4) == 15


def test_example_5():
    """Test B(5) = 52."""
    assert bell_Number(5) == 52


def test_example_6():
    """Test B(6) = 203."""
    assert bell_Number(6) == 203


def test_bell_7():
    """Test B(7) = 877."""
    assert bell_Number(7) == 877


def test_bell_8():
    """Test B(8) = 4140."""
    assert bell_Number(8) == 4140


def test_bell_9():
    """Test B(9) = 21147."""
    assert bell_Number(9) == 21147


def test_bell_10():
    """Test B(10) = 115975."""
    assert bell_Number(10) == 115975


def test_strictly_increasing():
    """Test that Bell numbers are strictly increasing for n >= 1."""
    for i in range(1, 8):
        assert bell_Number(i) < bell_Number(i + 1)
