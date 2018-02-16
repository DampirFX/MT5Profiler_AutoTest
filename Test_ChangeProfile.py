import pytest
from Cases import *


@pytest.fixture(autouse=True)
def resource_setup(request):
    print("\nStart test")
    print(request.scope)
    print(request.cls)
    print('Description: ' +request.function.__name__)
    #print(request.module.__name__)
    #print(request.fspath)
    def resource_teardown():
        print("Finish test")
    request.addfinalizer(resource_teardown)

def test_wrong_request(resource_setup):
    assert wrong_request() == {'Description': 'invalid uri', 'Status': 3}