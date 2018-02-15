import pytest
from Cases import *


@pytest.fixture()
def resource_setup(request):
    print("\nStart test")
    print(request.scope)
    print(request.function.__name__)
    #print(request.cls)
    print(request.module.__name__)
    #print(request.fspath)
    f = open(filename + '.log', 'a+')
    f.write(datetime.now().strftime("%H:%M:%S") + '   ' + request.function.__name__ + '\n')
    def resource_teardown():
        print("Finish test")
    request.addfinalizer(resource_teardown)

def test_wrong_request():
    assert wrong_request() == 'result - OK'