# We should have a single assert in each of the tests recommended
# We can have multiple asserts in a test as well
def test_a1():
    assert 3 > 2
    assert 4 <= 2
# we can add more logical operators in assert
# possible logical operators can be added in assert are :
# >=, <=, ==, != etc.

def test_a2():
    assert 1
    assert True
    assert 12.3
#    assert False
    assert 2
    assert "RAJAN"
#    assert 9/5 == divmod(9, 5)
    assert  4 in divmod(9, 5)
    assert "ap" in "pineapple"
    assert "app" not in "pineapple"

# Checking a sublist in a list
# Example
def test_a3():
#    assert [1, 2] in [1, 2, 3]
    assert [1, 2] in [[1, 2], [1, 3]]
    assert 1 in [1, 2, 3]