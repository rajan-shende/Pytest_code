# Running tests with some naming
# -k option enables to pass the expression / substring of test name to execute the specific test/s
# Along with the test execution we can execute the specific modules as well which contains those tests
# command : pytest -v -k names
# command : pytest -v -k landing
# we can use and or operators as well
# command : pytest -v -k "lat or landing"

def test_landing():
    assert 1 == 1


def test_db():
    assert 2 == 2


def test_latest():
    assert 1 == 1
