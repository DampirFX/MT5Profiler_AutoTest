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
        assert no_body_request() == {'Description': "can't read 'tradingProfile' param", 'Status': 4}
    def test_request_without_name_and_platform(resource_setup):
        assert request_without_name_and_platform() == {'Description': "can't read 'name' param", 'Status': 4}
    def test_request_without_name(resource_setup):
        assert request_without_name() == {'Description': "can't read 'name' param", 'Status': 4}
    def test_request_without_platforms(resource_setup):
        assert request_without_platforms() == {'Description': 'Done', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_REAL'}, {'Description': 'Done', 'Status': 0, 'platform': 'MT5_DEMO'}], 'Status': 0}
    def test_no_value_to_name(resource_setup):
        assert no_value_to_name() == {'Description': "can't find profile ''", 'Status': 5}
    def test_value_to_name_not_str(resource_setup):
        assert value_to_name_not_str() == {'Description': "can't read 'name' param", 'Status': 4}
    def test_correct_value_to_name(resource_setup):
        assert correct_value_to_name() == {'Description': 'Done', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_REAL'}, {'Description': 'Done', 'Status': 0, 'platform': 'MT5_DEMO'}], 'Status': 0}
    def test_not_found_profile_for_name_value(resource_setup):
        assert not_found_profile_for_name_value() == {'Description': "can't find profile 'for test'", 'Status': 5}
    def test_no_value_to_platforms(resource_setup):
        assert no_value_to_platforms() == {'Description': 'Done', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_REAL'}, {'Description': 'Done', 'Status': 0, 'platform': 'MT5_DEMO'}], 'Status': 0}
    def test_value_to_platforms_not_str(resource_setup):
        assert value_to_platforms_not_str() == {'Description': 'platform element not string', 'Status': 5}
    def test_correct_value_to_platforms_one_server(resource_setup):
        assert correct_value_to_platforms_one_server() == {'Description': 'Done', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_REAL'}], 'Status': 0}
    def test_correct_value_to_platforms_two_servers(resource_setup):
        assert correct_value_to_platforms_two_servers() == {'Description': 'Done', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_REAL'}, {'Description': 'Done', 'Status': 0, 'platform': 'MT5_DEMO'}], 'Status': 0}
    def test_value_to_platforms_two_servers_one_not_in_config(resource_setup):
        value_to_platforms_two_servers_one_not_in_config() == {'Description': 'One or more updates are failed', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_DEMO'}, {'Description': 'No connection', 'Status': 6, 'platform': 'MT5_TEST'}], 'Status': 7}
    def test_not_found_platform_in_profile(resource_setup):
        assert not_found_platform_in_profile() == {'Description': 'One or more updates are failed', 'Result': [{'Description': 'No information in config', 'Status': 2, 'platform': 'MT5_TEST'}], 'Status': 7}
#############################################################################
#Проверка кодов ответа
#############################################################################
    class Test_response_code():
        def test_not_found_platform_in_profile(resource_setup):
            assert not_found_platform_in_profile() == {'Description': 'One or more updates are failed', 'Result': [{'Description': 'No information in config', 'Status': 2, 'platform': 'MT5_TEST'}], 'Status': 7}
        def test_wrong_request(resource_setup):
            assert wrong_request() == {'Description': 'invalid uri', 'Status': 3}
        def test_no_body_request(resource_setup):
            assert no_body_request() == {'Description': "can't read 'tradingProfile' param", 'Status': 4}
        def test_request_without_name_and_platform(resource_setup):
            assert request_without_name_and_platform() == {'Description': "can't read 'name' param", 'Status': 4}
        def test_request_without_name(resource_setup):
            assert request_without_name() == {'Description': "can't read 'name' param", 'Status': 4}
        def test_value_to_name_not_str(resource_setup):
            assert value_to_name_not_str() == {'Description': "can't read 'name' param", 'Status': 4}
        def test_no_value_to_name(resource_setup):
            assert no_value_to_name() == {'Description': "can't find profile ''", 'Status': 5}
        def test_not_found_profile_for_name_value(resource_setup):
            assert not_found_profile_for_name_value() == {'Description': "can't find profile 'for test'", 'Status': 5}
        def test_value_to_platforms_not_str(resource_setup):
            assert value_to_platforms_not_str() == {'Description': 'platform element not string', 'Status': 5}
        def test_no_connection_with_server(resource_setup):
            assert no_connection_with_server() == {'Description': 'One or more updates are failed', 'Result': [{'Description': 'No connection', 'Status': 6, 'platform': 'MT5_TEST'}], 'Status': 7}
        def test_not_found_platform_in_profile(resource_setup):
            assert not_found_platform_in_profile() == {'Description': 'One or more updates are failed', 'Result': [{'Description': 'No information in config', 'Status': 2, 'platform': 'MT5_TEST'}], 'Status': 7}
        def test_value_to_platforms_two_servers_one_not_in_config(resource_setup):
            value_to_platforms_two_servers_one_not_in_config() == {'Description': 'One or more updates are failed', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT5_DEMO'}, {'Description': 'No connection', 'Status': 6, 'platform': 'MT5_TEST'}], 'Status': 7}
#############################################################################
#Проверка запроса Reload
#############################################################################
#class Test_Reload():
#    def test_reload(self):
#        assert reload() == 'dasrfsdfds'
#############################################################################
class Test_Data_in_DB():
    def test_check_db(resource_setup):
        mode,value,type = check_db()
        assert mode == 1
        assert value == 2000
        assert type == 3