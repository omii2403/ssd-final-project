import sys
import os
from hypothesis import given, strategies as st

# Ensure target_functions directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from get_max_gold_buggy import get_max_gold


# Helper strategy: generate valid gold mines (list of lists of non-negative ints)
@st.composite
def gold_mine_strategy(draw, max_m=5, max_n=5, max_val=20):
    m = draw(st.integers(min_value=1, max_value=max_m))
    n = draw(st.integers(min_value=1, max_value=max_n))
    gold = draw(st.lists(
        st.lists(st.integers(min_value=0, max_value=max_val), min_size=n, max_size=n),
        min_size=m,
        max_size=m
    ))
    return gold, m, n


# Property 1: Output is non-negative
@given(gold_mine_strategy())
def test_non_negative_result(data):
    gold, m, n = data
    result = get_max_gold(gold, m, n)
    assert result >= 0


# Property 2: For 1x1 grid, result == that cell’s value
@given(st.integers(min_value=0, max_value=100))
def test_single_cell(val):
    gold = [[val]]
    result = get_max_gold(gold, 1, 1)
    assert result == val


# Property 3: For 1-row mine, result == sum of all cells
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10))
def test_single_row_mine(row):
    gold = [row]
    result = get_max_gold(gold, 1, len(row))
    assert result == sum(row)


# Property 4: For 1-column mine, result == max cell in that column
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10))
def test_single_column_mine(col):
    gold = [[x] for x in col]
    result = get_max_gold(gold, len(col), 1)
    assert result == max(col)


# Property 5: Adding a new column (with non-negative gold) shouldn’t reduce result
@given(gold_mine_strategy())
def test_increasing_columns(data):
    gold, m, n = data
    extended_gold = [row + [0] for row in gold]  # Add zero-value column
    result1 = get_max_gold(gold, m, n)
    result2 = get_max_gold(extended_gold, m, n + 1)
    assert result2 >= result1
