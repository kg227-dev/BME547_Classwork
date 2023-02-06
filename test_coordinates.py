import pytest

@pytest.mark.parametrize("p1, p2, expected_m, expected_b", [((1,2), (3,6), 2, 0), ((0,0),(1,1),1,0)])
def test_get_line(p1,p2,expected_m, expected_b):
    from coordinates import get_line
    m,b = get_line(p1,p2)
    return m == expected_m and b == expected_b

@pytest.mark.parametrize("m, b, x, expected", [(3, 4, 5, 19), (-2, -1, 2,-5)])
def test_get_y(m,b,x, expected):
    from coordinates import get_y
    y = get_y(m,b,x)
    assert y == expected


