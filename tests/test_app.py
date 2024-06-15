from app import add, subtract

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(3, 4) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    