import pytest

pytestmark = [pytest.mark.sanity, pytest.mark.smoke]



@pytest.mark.sanity
def test_1():
    assert 1 == 1

@pytest.mark.sanity
def test_2():
    assert 1 == 1

@pytest.mark.regression
def test_3():
    assert 1 == 1


@pytest.mark.regression
def test_4():
    assert 1 == 1

@pytest.mark.smoke
def test_5():
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.smoke
def test_6():
    assert 1 == 1



