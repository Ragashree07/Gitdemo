import pytest
@pytest.mark.usefixtures("dataload")
class Test_load:
    def test_loaddata(self,dataload):
        print(dataload)
        print(dataload[0])