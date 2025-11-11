import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from get_max_gold_buggy import get_max_gold

def test_single_cell():
    assert get_max_gold([[7]], 1, 1) == 7

def test_single_row():
    # Only move right
    assert get_max_gold([[1, 2, 3, 4]], 1, 4) == 10

def test_single_column():
    # No movement possible except starting cell
    gold = [[5], [2], [9]]
    assert get_max_gold(gold, 3, 1) == 9

def test_example_given():
    gold = [
        [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]
    ]
    assert get_max_gold(gold, 4, 4) == 16

def test_all_zeroes():
    gold = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert get_max_gold(gold, 3, 3) == 0

def test_path_with_right_up_and_right_down():
    gold = [
        [10, 1, 1],
        [1, 10, 1],
        [1, 1, 10]
    ]
    # Best path is starting at row 0 -> (0,0)->(1,1)->(2,2) = 10+10+10
    assert get_max_gold(gold, 3, 3) == 30

def test_two_rows_mix():
    gold = [
        [1, 100, 1],
        [100, 1, 100]
    ]
    # Best path: start at row 1 -> (1,0)->(0,1)->(1,2) = 100+100+100 = 300
    assert get_max_gold(gold, 2, 3) == 300

def test_large_values():
    gold = [
        [100, 200, 300],
        [300, 200, 100],
        [200, 300, 100]
    ]
    # Best path: start at row 1 -> (1,0)->(0,1)->(0,2) = 300+200+300 = 800
    assert get_max_gold(gold, 3, 3) == 800

def test_boundary_all_equal():
    gold = [[5]*5 for _ in range(5)]
    # Any path leads to 5 * 5 columns = 25
    assert get_max_gold(gold, 5, 5) == 25
