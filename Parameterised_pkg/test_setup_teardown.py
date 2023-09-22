import requests
import pytest
# as return is the last funtion in every function ; the code after return won't executes.
# If yeild is used it returns the object along with that the code after yeild statement is also executed. Main purpose of useing yeild is for the cleaning up the tasks like DB Connections

# Example

@pytest.fixture()
def setup_01():
    print("setup 01 initialised !")
    mydict = {"google": "https://www.google.com",
              "wiki": "https://www.wikipedia.org"
              }
    yield mydict
    print("\nCleaning tasks initiated")
    print(str(mydict.pop('google'))+"item popped from dictionary")


@pytest.fixture()
def setup_02():
    print("setup 02 initialised !")
    codes_list = [200, 400, 501]
    yield codes_list
    print("Cleaning tasks initiated")
    print(str(codes_list.pop())+"Code popped from list")


def test_01(setup_01, setup_02):
    response_1 = requests.get(url=setup_01["google"], params={})
    assert response_1.status_code in setup_02