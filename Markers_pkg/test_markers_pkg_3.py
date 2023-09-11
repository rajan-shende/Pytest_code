import pytest
import sys
# we're doing some basic code with xfail marker

@pytest.mark.xfail(reason = "Known issue")
def test_1():
    assert 1 == 2

@pytest.mark.xfail(reason = "known issue")
def test_2():
    assert 2 == 3

@pytest.mark.xfail  # this needs to be failed but passed so this is as XPASS in output
def test_3():
    assert 2 == 2

@pytest.mark.xfail
def test_4():
    assert "ADS" == True

@pytest.mark.xfail
def test_5():
    assert 0 == False

# xfail markers with some conditions


def square():
    return 2 ** 2


@pytest.mark.xfail(square() == 4, reason="This is xfail")
def test_6():
    print("THIS IS PASSED !!! BUT ACTUALLY FAILED")


@pytest.mark.xfail(sys.platform != 'win32', reason="This is failed because os is not windows")
def test_7():
    print("This is failed due to uncompatible platform")
    assert 1 != 1


@pytest.mark.xfail(raises=IndexError, reason="Index is unvalid hence this is failed")
def test_8():
    var1 = "RAJAN"
    print(var1[8])


@pytest.mark.xfail(raises=TypeError, reason="FAILS normally because of unvalid error raised")
def test_9():
    var2 = "RAJAN"
    print(var2[100])