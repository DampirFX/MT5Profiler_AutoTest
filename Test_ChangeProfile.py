import pytest
from Cases import *


@pytest.fixture(autouse=True)
def resource_setup(request):
    print("\nStart test")
    print(request.scope)
    print(request.cls)
    print('Description: ' +request.function.__name__)
    def resource_teardown():
        print("Finish test")
    request.addfinalizer(resource_teardown)
#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
class Test_ChangeProfile():
    def test_wrong_request(resource_setup):
        assert wrong_request() == {'Description': 'invalid uri', 'Status': 3}
    def test_no_body_request(resource_setup):
        assert no_body_request() == ''
    def test_request_without_name_and_platform(resource_setup):
        assert request_without_name_and_platform() == ''
    def test_request_without_name(resource_setup):
        assert request_without_name() == ''
    def test_request_without_platforms(resource_setup):
        assert request_without_platforms == ''
    def test_no_value_to_name(resource_setup):
        assert no_value_to_name() == ''
    def test_value_to_name_not_str(resource_setup):
        assert value_to_name_not_str() == ''
    def test_correct_value_to_name(resource_setup):
        assert correct_value_to_name() == ''
    def test_not_found_profile_for_name_value(resource_setup):
        assert not_found_profile_for_name_value() == ''
    def test_no_value_to_platforms(resource_setup):
        assert no_value_to_platforms() == ''
    def test_value_to_platforms_not_str(resource_setup):
        assert value_to_platforms_not_str() == ''
    def test_correct_value_to_platforms(resource_setup):
        assert correct_value_to_platforms() == ''
    def test_not_found_platform_in_profile(resource_setup):
        assert not_found_platform_in_profile() == ''

#############################################################################
#Проверка запроса Reload
#############################################################################
#class Test_Reload():
#    def test_reload(self):
#        assert reload() == 'dasrfsdfds'