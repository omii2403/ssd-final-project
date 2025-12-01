import os
import sys
import math
import colorsys
from hypothesis import given, strategies as st

# Ensure bug_portfolio directory is visible for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bug_portfolio')))

from rgb_to_hsv_correct import rgb_to_hsv


# Strategy: all valid 8-bit RGB triples
rgb_strategy = st.tuples(
    st.integers(min_value=0, max_value=255),
    st.integers(min_value=0, max_value=255),
    st.integers(min_value=0, max_value=255),
)


@given(rgb_strategy)
def test_rgb_to_hsv_ranges(rgb):
    """Basic range properties for HSV output."""
    r, g, b = rgb
    h, s, v = rgb_to_hsv(r, g, b)

    assert 0.0 <= s <= 100.0
    assert 0.0 <= v <= 100.0
    # Allow tiny tolerance for hue, but it should be effectively in [0, 360)
    assert -1.0 <= h < 361.0


@given(rgb_strategy)
def test_rgb_to_hsv_grayscale_property(rgb):
    """For grayscale inputs (r == g == b), saturation must be 0 and hue 0."""
    r, g, b = rgb
    h, s, v = rgb_to_hsv(r, g, b)

    if r == g == b:
        assert math.isclose(s, 0.0, abs_tol=1e-6)
        assert math.isclose(h % 360.0, 0.0, abs_tol=1e-6)


@given(rgb_strategy)
def test_rgb_to_hsv_matches_colorsys_value_and_saturation(rgb):
    """S and V should match Python's colorsys implementation (within tolerance)."""
    r, g, b = rgb
    h, s, v = rgb_to_hsv(r, g, b)

    rr, gg, bb = r / 255.0, g / 255.0, b / 255.0
    ref_h, ref_s, ref_v = colorsys.rgb_to_hsv(rr, gg, bb)

    ref_s *= 100.0
    ref_v *= 100.0

    assert math.isclose(s, ref_s, rel_tol=1e-6, abs_tol=1e-6)
    assert math.isclose(v, ref_v, rel_tol=1e-6, abs_tol=1e-6)


@given(rgb_strategy)
def test_rgb_to_hsv_matches_colorsys_hue_when_colored(rgb):
    """Hue should match colorsys for non-gray colors (where saturation > 0)."""
    r, g, b = rgb
    h, s, v = rgb_to_hsv(r, g, b)

    rr, gg, bb = r / 255.0, g / 255.0, b / 255.0
    ref_h, ref_s, ref_v = colorsys.rgb_to_hsv(rr, gg, bb)

    ref_h *= 360.0

    # Only compare hue when there is meaningful color (not nearly gray)
    if ref_s > 1e-6:
        h_norm = h % 360.0
        ref_h_norm = ref_h % 360.0
        assert math.isclose(h_norm, ref_h_norm, rel_tol=1e-3, abs_tol=1e-3)


@given(rgb_strategy)
def test_rgb_to_hsv_black_and_white_extremes(rgb):
    """Special behavior for pure black and pure white."""
    r, g, b = rgb
    h, s, v = rgb_to_hsv(r, g, b)

    if (r, g, b) == (0, 0, 0):
        # Pure black: value 0, saturation 0, hue irrelevant but we keep it at 0
        assert math.isclose(v, 0.0, abs_tol=1e-6)
        assert math.isclose(s, 0.0, abs_tol=1e-6)
        assert math.isclose(h % 360.0, 0.0, abs_tol=1e-6)

    if (r, g, b) == (255, 255, 255):
        # Pure white: value 100, saturation 0, hue 0 by convention
        assert math.isclose(v, 100.0, abs_tol=1e-6)
        assert math.isclose(s, 0.0, abs_tol=1e-6)
        assert math.isclose(h % 360.0, 0.0, abs_tol=1e-6)
