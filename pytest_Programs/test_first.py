def test_first():
    a = 10
    b = 20
    assert a == b   ##### assert  is like comparison if result is true then test case is passed


def test_second():
    a = 10
    b = 10
    assert a == b


def test_third():
    a = 10
    b = 20
    result = a + b
    assert result == 30

