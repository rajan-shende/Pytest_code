# The init.py help us in the test discovery.
# __init__.py also helps to execution of tests with same names in different modules
# Raising exception : If we want to test a condition where ;
# if condition is not met it can arise an error like Internal server error n all
# for that we are using the pytest "raises"
# Also this helps to pass the test in case exception is raised
# Also if the test is suppose to raise exception and it does not in that case the test fails

class Employee:
    org = "MARS & CO"

class TestClass1:
    # Here we can call the methods / we can create some instances like instance of webdriver in case of selenium

    def test_a1(self):
        emp = Employee()
        emp_2 = Employee()
        assert type(1) == int
        assert type(1.0) == float
        assert type(emp) == Employee
        assert "apple" == "APPLE".lower()

    def test_a2(self):
        assert 2 in (1, 2)



