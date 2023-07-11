import sys

import pytest


@pytest.mark.skip  ### to skip test and do not execute
def test_first():
    a = 10
    b = 20
    assert a == b


@pytest.mark.skipif(True, reason="simply skip")
def test_second():
    a = 10
    b = 10
    assert a == b


@pytest.mark.skipif(sys.version_info > (3, 7), reason=f"{sys.version_info} version is not supported ")
def test_third():
    a = 10
    b = 20
    result = a + b
    assert result == 30


@pytest.mark.xfail
def test_fourth():
    hi = 50
    bye = 100
    assert hi != bye
