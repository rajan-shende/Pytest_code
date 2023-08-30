import pytest


def test_a1():
    with pytest.raises(Exception):  # instead giving generic exception we can give the particular exception as well
        assert (1/0)

def test_a2():
    with pytest.raises(ZeroDivisionError):
        assert 1/0

def test_a3():
    with pytest.raises(Exception) as excinfo:
        assert (1, 3) == (1, 2)
    print(str(excinfo))

def test_a4():
    raise ValueError("VALUE ERROR RAISED !! IN FUNCTION 1")

def test_a5():
    with pytest.raises(ValueError) as execinfo:  # Here we are asserting for exception values
        test_a4()
        assert (execinfo.value) == "VALUE ERROR RAISED !! IN FUNCTION 1"