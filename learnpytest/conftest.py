import pytest


@pytest.fixture(scope="class")
def setup():
    print("India is my country")
    yield
    print("These are the people of India")

@pytest.fixture()
def dataload():
    print("It loads the data")
    return ["raga", "shree", "ragashreegandhi"]

@pytest.fixture(params=[("chrome","raga"),("firefox","shree")])
def parameter(request):
    return request.param