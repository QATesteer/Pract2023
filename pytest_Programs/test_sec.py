def test_first():
    a = 10
    b = 20
    assert a == b


def test_second():
    a = 10
    b = 10
    assert a == b


def test_third():
    a = 10
    b = 20
    result = a + b
    assert result == 30

def test_fourth():
    hi = 50
    bye = 100
    assert hi != bye