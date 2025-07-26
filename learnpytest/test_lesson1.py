import pytest


@pytest.mark.usefixtures("setup")
class Testcountry:
    def test_state1(self):
        print("I am from Kerala")
    def test_state2(self):
        print("I am from Andhra")
    def test_state3(self):
        print("I am from Assam")
    def test_state4(self):
        print("I am from Bihar")