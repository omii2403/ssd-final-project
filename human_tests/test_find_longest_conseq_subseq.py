import os
import sys
from hypothesis import given, strategies as st

# Allow import from bug_portfolio folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))
from find_longest_conseq_subseq_buggy import find_longest_conseq_subseq


# -------------------------------------------------------------
# Slow, correct reference implementation (ground truth)
# -------------------------------------------------------------
def spec(arr):
    arr = sorted(set(arr))
    longest = 1
    current = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current += 1
        else:
            current = 1
        longest = max(longest, current)
    return longest


# -------------------------------------------------------------
# 1. Basic specification agreement
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1, max_size=200))
def test_matches_spec(arr):
    assert find_longest_conseq_subseq(arr, len(arr)) == spec(arr)


# -------------------------------------------------------------
# 2. Reordering arr must not change result
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=-500, max_value=500), min_size=1, max_size=150))
def test_permutation_invariance(arr):
    import random
    arr2 = arr[:]
    random.shuffle(arr2)
    assert find_longest_conseq_subseq(arr, len(arr)) == \
           find_longest_conseq_subseq(arr2, len(arr2))


# -------------------------------------------------------------
# 3. Adding duplicates should not affect the result
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=-300, max_value=300), min_size=1, max_size=150))
def test_duplicate_invariance(arr):
    if len(arr) > 1:
        arr2 = arr + [arr[0]]
        assert find_longest_conseq_subseq(arr2, len(arr2)) == \
               find_longest_conseq_subseq(arr, len(arr))


# -------------------------------------------------------------
# 4. If array is strictly consecutive, answer = length
# -------------------------------------------------------------
@given(st.integers(min_value=1, max_value=50))
def test_strict_consecutive(k):
    arr = list(range(k))
    assert find_longest_conseq_subseq(arr, len(arr)) == k


# -------------------------------------------------------------
# 5. A single element always returns 1
# -------------------------------------------------------------
@given(st.integers(min_value=-10000, max_value=10000))
def test_single_element(n):
    assert find_longest_conseq_subseq([n], 1) == 1


# -------------------------------------------------------------
# 6. Fully non-consecutive list returns 1
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=0, max_value=500), min_size=1, max_size=50))
def test_all_far_apart(arr):
    arr = [x * 10 for x in arr]  # ensure large gaps
    assert find_longest_conseq_subseq(arr, len(arr)) == 1


# -------------------------------------------------------------
# 7. Adjacent gaps break sequences
# -------------------------------------------------------------
@given(st.integers(min_value=1, max_value=50))
def test_gap_breaks_sequence(k):
    arr = [1,2,3,4, k+10, k+20]
    assert find_longest_conseq_subseq(arr, len(arr)) == 4


# -------------------------------------------------------------
# 8. Negative numbers & positives work equally
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=-50, max_value=50), min_size=1, max_size=100))
def test_mixed_sign(arr):
    assert find_longest_conseq_subseq(arr, len(arr)) == spec(arr)


# -------------------------------------------------------------
# 9. Adding numbers far outside range cannot increase result
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=0, max_value=20), min_size=1, max_size=40))
def test_unrelated_values(arr):
    extended = arr + [9999, -9999]
    assert find_longest_conseq_subseq(extended, len(extended)) == spec(arr)


# -------------------------------------------------------------
# 10. Sorted repeated patterns should behave same as unsorted
# -------------------------------------------------------------
@given(st.lists(st.integers(min_value=0, max_value=10), min_size=5, max_size=50))
def test_pattern_repetition(arr):
    doubled = arr + arr
    assert find_longest_conseq_subseq(arr, len(arr)) == \
           find_longest_conseq_subseq(doubled, len(doubled))
