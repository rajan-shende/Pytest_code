# The test files should be named with prefix test_
# This will help pytest while running pytest framework it will locate those files as a test files
# pytest will search in directories and subdirectories
# test methods should be prefixed with test_
# so that pytest while running can locate test methods in directories & Subdirectories
# we should not be adding multiple asserts in a single test method
# to run the tests Command : pytest testfolder_name
# Run tests using verbose mode Command : pytest -v testfolder_name
# To run specific test case in pycharm just click on that test and select run test case
# To run test cases while printing the required message we can use -s option
# cache stores the information about previous test run

def test_a1():
    assert 1 == (2 - 1)


def test_a2():
    assert 2 == 3, "Assertion failed intentionally"


def test_a3():
    assert 1 == 1



