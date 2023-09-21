import requests
import pytest
# Test fixtures are used for doing some task / s before the session starts
# also after session ends. like cleaning DB Connection or setup DB Connection etc.
# One can return data from fixture as well
# It is not mandatory that the fixture must return something.
# Fixture basics part 1
# Fixtures can be called in 2 different ways. 1. is using directly in a function 2. calling a fixture using markers
# Fixture basics part 2 we are calling fixture by using directly inside a function but we cannot use the returned value inside other test


@pytest.fixture()
def setup_url():
    print(" Initializing test fixture ")
    url_dict = {"google1": "https://www.google.com", "yahoo1": "https://www.yahoo.com"}
    return url_dict


def test_url(setup_url):
    response_1 = requests.get(url=setup_url["google1"], params={})
    response_2 = requests.get(url=setup_url["yahoo1"], params={})

    print("status_code for google is "+str(response_1.status_code))
    print("status_code for yahoo is " + str(response_2.status_code))

# Fixture basics part 2
# we are calling fixture by using the markers

@pytest.mark.usefixtures("setup_url")
def test_url_2():
    print("test_url_2")
    assert 1 == 1






