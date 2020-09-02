import pytest


@pytest.mark.parametrize("x, point1, point2, expected", [
    (0.5, (0, 0), (1, 1), 0.5),
    (2, (4,-3),(0,-4), -3.5)
    ])
def test_compute_y(x, point1, point2, expected):
    from activity_9_2 import compute_y
    result = compute_y(x, point1, point2)
    assert result == expected
