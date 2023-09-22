import pytest
import requests


# Here writing a test with set of single parameter

@pytest.mark.parametrize("status_codes", [404, 200, 500])
def test_get(status_codes):
    response_1 = requests.get(url="https://google.com", params={})
    assert status_codes == response_1.status_code
    # assert abc1 == response_1.status_code


# Here writing a test case with multiple parameter like input & Output


@pytest.mark.parametrize("test_url, status_code", [("https://google.com", 200)])
def test_get_multi(test_url, status_code):
    response_1 = requests.get(test_url, params={})
    assert response_1.status_code == status_code


