import pytest
from Cases import *

default_list = ((1, 0, 3), (1, 0, 3), (1, 0, 3),(1, 0, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3), (1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3))
crisis_list =  ((1, 0, 3), (1, 0, 3), (1, 0, 3), (1, 1000, 3),(1, 2000, 3),(1, 2000, 3),(1, 2000, 3),(1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3),(1, 2000, 3))
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
        assert wrong_request() == {'description': 'invalid uri', 'status': 3}

    def test_no_body_request(resource_setup):
        assert no_body_request() == {'description': "can't read 'tradingProfile' param", 'status': 4}

    def test_request_without_name_and_platform(resource_setup):
        assert request_without_name_and_platform() == {'description': "can't read 'name' param", 'status': 4}

    def test_request_without_name(resource_setup):
        assert request_without_name() == {'description': "can't read 'name' param", 'status': 4}

    def test_request_without_platforms(resource_setup):
        finres = request_without_platforms()
        assert finres[0] == {'Result': [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                        {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}],
                             'description': 'Done', 'status': 0}

        assert finres[1] == crisis_list

    def test_no_value_to_name(resource_setup):
        assert no_value_to_name() == {'description': "can't find profile ''", 'status': 5}

    def test_value_to_name_not_str(resource_setup):
        assert value_to_name_not_str() == {'description': "element 'name' not string", 'status': 5}

    def test_correct_value_to_name(resource_setup):
        finres = correct_value_to_name()
        assert finres[0] == {'description': 'Done', 'Result': [{'description': 'Done', 'status': 0, 'platform': 'MT5_MARKET_REAL'},
                                                                             {'description': 'Done', 'status': 0, 'platform': 'MT5_INSTANT_REAL'}], 'status': 0}

        assert finres[1] == default_list

    def test_not_found_profile_for_name_value(resource_setup):
        assert not_found_profile_for_name_value() == {'description': "can't find profile 'for test'", 'status': 5}

    def test_no_value_to_platforms(resource_setup):
        finres = no_value_to_platforms()
        assert finres[0] == {'Result': [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                        {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}],
                             'description': 'Done', 'status': 0}

        assert finres[1] == crisis_list

    def test_value_to_platforms_not_str(resource_setup):
        assert value_to_platforms_not_str() == {'description': 'platform element not string', 'status': 5}

    def test_correct_value_to_platforms_one_server(resource_setup):
        finres = correct_value_to_platforms_one_server()
        assert finres[0] == {'description': 'Done', 'Result': [{'description': 'Done', 'status': 0, 'platform': 'MT5_MARKET_REAL'}], 'status': 0}

        assert finres[1] == default_list

    def test_correct_value_to_platforms_two_servers(resource_setup):
        finres = correct_value_to_platforms_two_servers()
        assert finres[0] == {'Result': [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                        {'description': 'Done', 'platform': 'MT5_INSTANT_REAL','status': 0}],
                             'description': 'Done', 'status': 0}

        assert finres[1] == default_list

    def test_value_to_platforms_two_servers_one_not_in_config(resource_setup):
        finres = value_to_platforms_two_servers_one_not_in_config()
        assert finres[0] == {'Result': [{'description': "IMTAdminAPI::RouteGet('All Timeout Market', ""route) failed, error(MTAPIRES): 13('Not found')",
                                         'platform': 'MT5_MARKET_REAL', 'status': 1},
                                        {'description': 'No information in config', 'platform': 'MT5_FOR_TEST',
                                         'status': 2}],
                             'description': 'One or more updates are failed', 'status': 7}

        assert finres[1] == default_list

    def test_not_found_platform_in_profile(resource_setup):
        assert not_found_platform_in_profile() == {'Result': [{'description': 'No information in config', 'platform': 'MT5_TEST', 'status': 2}],
                                                   'description': 'One or more updates are failed', 'status': 7}
#############################################################################
#Проверка кодов ответа
#############################################################################
    class Test_response_code():
        def test_not_found_platform_in_profile(resource_setup):
            assert not_found_platform_in_profile() == {'Result': [{'description': 'No information in config','platform': 'MT5_TEST','status': 2}],
                                                        'description': 'One or more updates are failed','status': 7}

        def test_wrong_request(resource_setup):
            assert wrong_request() == {'description': 'invalid uri', 'status': 3}

        def test_no_body_request(resource_setup):
            assert no_body_request() == {'description': "can't read 'tradingProfile' param", 'status': 4}

        def test_request_without_name_and_platform(resource_setup):
            assert request_without_name_and_platform() == {'description': "can't read 'name' param", 'status': 4}

        def test_request_without_name(resource_setup):
            assert request_without_name() == {'description': "can't read 'name' param", 'status': 4}

        def test_value_to_name_not_str(resource_setup):
            assert value_to_name_not_str() == {'description': "element 'name' not string", 'status': 5}

        def test_no_value_to_name(resource_setup):
            assert no_value_to_name() == {'description': "can't find profile ''", 'status': 5}

        def test_not_found_profile_for_name_value(resource_setup):
            assert not_found_profile_for_name_value() == {'description': "can't find profile 'for test'", 'status': 5}

        def test_no_valid_json_2(resource_setup):
            assert no_valid_json_2() == {'description': 'invalid json', 'status': 5}

        def test_value_to_platforms_not_str(resource_setup):
            assert value_to_platforms_not_str() == {'description': 'platform element not string', 'status': 5}

        def test_no_connection_with_server(resource_setup):
            assert no_connection_with_server() == {'Result': [{'description': 'No connection','platform': 'MT5_TEST','status': 6}],
                                                   'description': 'One or more updates are failed','status': 7}

        def test_not_found_platform_in_profile(resource_setup):
            assert not_found_platform_in_profile() == {'Result': [{'description': 'No information in config', 'platform': 'MT5_TEST', 'status': 2}],
                                                       'description': 'One or more updates are failed', 'status': 7}

        def test_value_to_platforms_two_servers_one_not_in_config(resource_setup):
            finres = value_to_platforms_two_servers_one_not_in_config()
            assert finres[0] == {'Result': [{'description': "IMTAdminAPI::RouteGet('All Timeout Market', ""route) failed, error(MTAPIRES): 13('Not found')",
                                             'platform': 'MT5_MARKET_REAL', 'status': 1},
                                            {'description': 'No information in config', 'platform': 'MT5_FOR_TEST',
                                             'status': 2}],
                                 'description': 'One or more updates are failed', 'status': 7}

            assert finres[1] == default_list

#############################################################################
#Проверка запроса Reload
#############################################################################

class Test_ReloadProfiles():
    def test_true_reload(self):
        assert true_reload() == {'description': 'Done', 'status': 0}

    def test_false_reload(self):
        assert false_reload() == {'description': 'invalid uri', 'status': 3}

#############################################################################
#Check invalid json
#############################################################################

class Test_valid_json():
    def test_no_valid_json_1(resource_setup):
        assert no_valid_json_1() == {'description': 'in Json::Value::find(key, end, found): requires objectValue ''or nullValue','status': 1}

    def test_no_valid_json_2(resource_setup):
        assert no_valid_json_2() == {'description': 'invalid json', 'status': 5}

#############################################################################
#Check data in db
#############################################################################

class Test_Data_in_DB():
        def test_check_db_first(resource_setup):
            finres = check_db_first()
            assert finres[0] == {'Result': [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                            {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}],
                                 'description': 'Done', 'status': 0}

            assert finres[1] == ((1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 2000, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3),(1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 2000, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3))

        def test_check_db_second(resource_setup):
            finres = check_db_second()
            assert finres[0] == {'Result': [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                            {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}],
                                 'description': 'Done', 'status': 0}

            assert finres[1] == ((1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 4000, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3),(1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 4000, 3),(1, 1000, 3), (1, 2000, 3),(1, 2000, 3))

def test_default_mode(resource_setup):
    finres = default_mode()
    assert finres[0] == {'Result': [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                    {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}],
                         'description': 'Done', 'status': 0}

    assert finres[1] == default_list