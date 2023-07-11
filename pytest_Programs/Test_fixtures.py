import pytest


@pytest.fixture()
def setup():
    print("get driver")
    print("maximize window")
    yield            # divide before and after activity
    print("print title")
    print("close window")


def test_1(setup):
    print("open facebook url")


def test_2(setup):
    print("open gmail url")
