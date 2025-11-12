from hypothesis import given, strategies as st, assume
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from get_max_occure import get_max_occuring_char  # main function

# -----------------------------
# Restrict input to ASCII range
# -----------------------------
text_strategy = st.text(min_size=1, alphabet=st.characters(max_codepoint=255))

@given(text_strategy)
def test_character_is_from_input(s):
    # Property: Returned character must exist in input
    result = get_max_occuring_char(s)
    assert result in s

@given(text_strategy)
def test_max_character_consistency(s):
    # Property: The returned character must have the maximum frequency
    result = get_max_occuring_char(s)
    counts = {c: s.count(c) for c in set(s)}
    max_count = max(counts.values())
    assert counts[result] == max_count

@given(text_strategy)
def test_same_result_for_permutations(s):
    # Property: Any permutation of the string should give the same result
    from random import shuffle

    counts = {c: s.count(c) for c in set(s)}
    # Skip if multiple characters share the same max frequency (ambiguous result)
    assume(list(counts.values()).count(max(counts.values())) == 1)

    chars = list(s)
    shuffle(chars)
    shuffled = ''.join(chars)

    assert get_max_occuring_char(s) == get_max_occuring_char(shuffled)
