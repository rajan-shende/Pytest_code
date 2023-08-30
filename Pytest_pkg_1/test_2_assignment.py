def test_1():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


# By default pytest captures standard-output while running tests.
# Only if a test fails, the captured output is shown.
# Meaning, if the test is a pass, the print stmts are not logged to console.
# We can use -s option, toprint to stdout or to console in all cases.