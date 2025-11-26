import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../bug_portfolio')))

from rgb_to_hsv_buggy import rgb_to_hsv


def almost_equal(a, b, tol=1e-2):
    return abs(a - b) <= tol

@pytest.mark.parametrize("r,g,b,expected", [
    # Primary colors
    (255, 0, 0, (0, 100, 100)),         # Red
    (0, 255, 0, (120, 100, 100)),       # Green
    (0, 0, 255, (240, 100, 100)),       # Blue

    # Secondary colors
    (255, 255, 0, (60, 100, 100)),      # Yellow
    (0, 255, 255, (180, 100, 100)),     # Cyan
    (255, 0, 255, (300, 100, 100)),     # Magenta

    # Grayscale colors (saturation must be 0, hue = 0)
    (0, 0, 0, (0, 0, 0)),               # Black
    (128, 128, 128, (0, 0, 50.2)),      # Mid-gray
    (255, 255, 255, (0, 0, 100)),       # White

    # Low-saturation color (almost gray)
    (250, 240, 245, (330, 4, 98)),      # Slightly pink-white

    # Unequal RGB for non-trivial hue
    (192, 128, 64, (30, 66.7, 75.3)),   # Brownish color
    (128, 0, 64, (330, 100, 50.2)),     # Dark magenta
])
def test_rgb_to_hsv(r, g, b, expected):
    h, s, v = rgb_to_hsv(r, g, b)
    eh, es, ev = expected
    # Hue wrap-around check
    assert 0 <= h < 360, f"Hue {h} out of range"
    # Saturation/value range
    assert 0 <= s <= 100, f"Saturation {s} out of range"
    assert 0 <= v <= 100, f"Value {v} out of range"

    # Approximate comparison (floating point tolerance)
    assert almost_equal(h, eh, 1), f"Hue mismatch: got {h}, expected {eh}"
    assert almost_equal(s, es, 1), f"Saturation mismatch: got {s}, expected {es}"
    assert almost_equal(v, ev, 1), f"Value mismatch: got {v}, expected {ev}"

def test_grayscale_behavior():
    # For all grayscale inputs, s must be 0 and h = 0
    for val in [0, 64, 128, 192, 255]:
        h, s, v = rgb_to_hsv(val, val, val)
        assert s == 0, f"Saturation not 0 for grayscale {val}"
        assert h == 0, f"Hue not 0 for grayscale {val}"
        assert almost_equal(v, val / 255 * 100, 0.5)

def test_boundary_values():
    # Ensure edge cases are handled correctly
    assert rgb_to_hsv(255, 255, 254)[1] < 1, "Near-white should have low saturation"
    assert rgb_to_hsv(1, 0, 0)[2] > 0, "Very dark red should have nonzero V"
    assert rgb_to_hsv(0, 0, 1)[0] == 240, "Very dark blue hue mismatch"
