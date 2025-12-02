import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from armstrong_number_buggy import armstrong_number

@pytest.mark.parametrize("number, expected", [
    # 1. Smallest Armstrong number (single-digit)
    (1, True),

    # 2. All single digits are Armstrong numbers
    (7, True),

    # 3. Classic Armstrong number example
    (153, True),

    # 4. Another known Armstrong number
    (370, True),

    # 5. 3-digit Armstrong number
    (371, True),

    # 6. Non-Armstrong small number
    (10, False),

    # 7. Given example of non-Armstrong
    (123, False),

    # 8. Boundary: near an Armstrong number but not equal
    (152, False),

    # 9. Large non-Armstrong number
    (999, False),

    # 10. Edge: two-digit number (none are Armstrong except single-digit)
    (57, False),

    # 11. Another 4-digit non-Armstrong
    (9475, False),
])
def test_armstrong_number_cases(number, expected):
    assert armstrong_number(number) == expected
