import pytest
import sys
pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason="skipped because of non-linux pla")

# We can skip the entire pytest module based on skipif for some condition ; we can write that condition in top
# This is unconditional skip of the tests we use only skip()

@pytest.mark.skip()
def test_1():
    assert 2 == 2

@pytest.mark.skip(reason = "This test will be skipped because will fail on execution")
def test_2():
    assert 3 == 3


def square():
    return 2 ** 2

@pytest.mark.skipif(square() == 4, reason="square of 4 so skipped")
def test_3():
    assert 1 == True
