import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from max_chain_length_buggy import Pair, max_chain_length


def sort_pairs(arr):
    """Ensure pairs are sorted by second element (standard approach)."""
    return sorted(arr, key=lambda p: p.b)


def test_single_pair():
    arr = [Pair(1, 2)]
    assert max_chain_length(arr, len(arr)) == 1


def test_non_overlapping_pairs():
    arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 3


def test_overlapping_pairs():
    arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 3


def test_fully_overlapping_pairs():
    arr = [Pair(1, 10), Pair(2, 9), Pair(3, 8)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 1


def test_touching_pairs_not_chain():
    arr = [Pair(1, 2), Pair(2, 3)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 1


def test_disordered_pairs():
    arr = [Pair(27, 40), Pair(5, 24), Pair(15, 25), Pair(50, 60)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 3


def test_large_gap_pairs():
    arr = [Pair(1, 5), Pair(10, 15), Pair(20, 25)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 3

def test_identical_pairs():
    arr = [Pair(1, 3), Pair(1, 3), Pair(1, 3)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 1


def test_wide_range_pairs():
    arr = [Pair(1, 100), Pair(101, 200), Pair(201, 300)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 3


def test_partial_overlap():
    arr = [Pair(1, 10), Pair(9, 20), Pair(21, 30)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 2


def test_random_mixed_case():
    arr = [Pair(10, 20), Pair(1, 2), Pair(5, 8), Pair(21, 25), Pair(30, 35)]
    arr = sort_pairs(arr)
    assert max_chain_length(arr, len(arr)) == 5
