import mathlib as ml

def test_all():
    """Roughly testing everything"""

    assert ml.add(6, 2) == 8
    assert ml.sub(6, 2) == 4
    assert ml.mul(6, 2) == 12
    assert ml.div(6, 2) == 4

def test_add():
    """Addition test"""

    for i in range(1000):
        for j in range(1000):
            assert ml.add(i, j) == (i + j)

