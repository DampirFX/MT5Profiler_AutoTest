import pytest
from ConnectorMT5Profiler import Connection
from DB_Connector import get_data_from_db

default_list = ((1, 0, 3), (1, 0, 3), (1, 0, 3),(1, 0, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3), (1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 0, 3),(1, 1000, 3),(1, 2000, 3),(1, 2000, 3))
crisis_list = ((0, 1000, 3), (1, 1000, 3), (1, 1000, 3), (1, 1000, 3), (1, 2000, 3), (1, 4000, 3), (1, 4000, 3), (0, 1000, 3), (1, 1000, 3), (1, 1000, 3), (1, 1000, 3), (1, 2000, 3), (1, 4000, 3), (1, 4000, 3))



class Test_ChangeProfile_False_url():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Default_for_autotest",
                "platforms": ["MT5_MARKET_REAL"]
            }
        }
        return Connection().Change_Profile_false_url(data)

    def test_false_url_status(self,setup):
        assert "status" in setup.keys()

    def test_false_url_status_code(self,setup):
        assert setup["status"] == 3

    def test_false_url_description(self,setup):
        assert "description" in setup.keys()

    def test_false_url_description_value(self,setup):
        assert setup["description"] == 'invalid uri'

class Test_ChangeProfile_WithOut_Body():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {}
        return Connection().Change_Profile_true_url(data)

    def test_request_without_body_status(self, setup):
        assert "status" in setup.keys()

    def test_request_without_body_status_code(self, setup):
        assert setup["status"] == 4

    def test_request_without_body_description(self, setup):
        assert "description" in setup.keys()

    def test_request_without_body_description_value(self, setup):
        assert setup["description"] == "can't read 'tradingProfile' param"

class Test_ChangeProfile_WithOut_name():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {"platforms": ["MT5_MARKET_REAL"]}
        }
        return Connection().Change_Profile_true_url(data)

    def test_request_without_name_status(self,setup):
        assert "status" in setup.keys()

    def test_request_without_name_status_code(self,setup):
        assert setup["status"] == 4

    def test_request_without_name_description(self, setup):
        assert "description" in setup.keys()

    def test_request_without_name_description_value(self, setup):
        assert setup["description"] == "can't read 'name' param"

class Test_ChangeProfile_WithOut_platform():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {"name": "Crisis_for_autotest"}
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_without_platform_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_without_platform_status_code(self, setup):
        assert setup[0]["status"] == 0

    def test_request_without_platform_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_without_platform_description_value(self, setup):
        assert setup[0]["description"] == 'Done'

    def test_request_without_platform_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_without_platform_check_data_in_db(self, setup):
        assert setup[1] == crisis_list

    def test_request_without_platform_result_value(self,setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                    {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}]


class Test_No_Value_for_Name():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "",
                "platforms": ["MT5_INSTANT_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data)

    def test_request_without_value_for_name_status(self,setup):
        assert "status" in setup.keys()

    def test_request_without_value_for_name_status_code(self,setup):
        assert setup["status"] == 5

    def test_request_without_value_for_name_description(self, setup):
        assert "description" in setup.keys()

    def test_request_without_value_for_name_description_value(self, setup):
        assert setup["description"] == "can't find profile ''"

class Test_Value_To_Name_Not_Str():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": 123456,
                "platforms": ["MT5_INSTANT_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data)

    def test_request_value_to_name_not_str_status(self, setup):
        assert "status" in setup.keys()

    def test_request_value_to_name_not_str_status_code(self, setup):
        assert setup["status"] == 5

    def test_request_value_to_name_not_str_description(self, setup):
        assert "description" in setup.keys()

    def test_request_value_to_name_not_str_description_value(self, setup):
        assert setup["description"] == "element 'name' not string"

class Test_Correct_Value_To_Name():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Default_for_autotest",
                "platforms": ["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_correct_value_to_name_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_correct_value_to_name_status_code(self, setup):
        assert setup[0]["status"] == 0

    def test_correct_value_to_name_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_correct_value_to_name_description_value(self, setup):
        assert setup[0]["description"] == 'Done'

    def test_request_correct_value_to_name_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_correct_value_to_name_check_data_in_db(self, setup):
        assert setup[1] == default_list

    def test_request_correct_value_to_name_result_value(self, setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                      {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}]


class Test_Not_Found_Profile_For_Name_Value():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "for test",
                "platforms": ["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data)

    def test_request_not_found_profile_for_name_value_status(self, setup):
        assert "status" in setup.keys()

    def test_request_not_found_profile_for_name_value_status_code(self, setup):
        assert setup["status"] == 5

    def test_request_not_found_profile_for_name_value_description(self, setup):
        assert "description" in setup.keys()

    def test_request_not_found_profile_for_name_value_description_value(self, setup):
        assert setup["description"] == "can't find profile 'for test'"

class Test_No_Value_To_Platforms():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Crisis_for_autotest",
                "platforms": []
            }
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_no_value_to_platforms_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_no_value_to_platforms_status_code(self, setup):
        assert setup[0]["status"] == 0

    def test_request_no_value_to_platforms_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_no_value_to_platforms_description_value(self, setup):
        assert setup[0]["description"] == 'Done'

    def test_request_no_value_to_platforms_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_no_value_to_platforms_check_data_in_db(self, setup):
        assert setup[1] == crisis_list

    def test_request_no_value_to_platforms_result_value(self, setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                      {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}]


class Test_Value_To_Platforms_Not_Str():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Default_for_autotest",
                "platforms": [123456]
            }
        }
        return Connection().Change_Profile_true_url(data)

    def test_request_value_to_platforms_not_str_status(self, setup):
        assert "status" in setup.keys()

    def test_request_value_to_platforms_not_str_status_code(self, setup):
        assert setup["status"] == 5

    def test_request_value_to_platforms_not_str_description(self, setup):
        assert "description" in setup.keys()

    def test_request_value_to_platforms_not_str_description_value(self, setup):
        assert setup["description"] == 'platform element not string'

class Test_Correct_Value_To_Platforms_One_Server():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Default_for_autotest",
                "platforms": ["MT5_MARKET_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_correct_value_to_platforms_one_server_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_correct_value_to_platforms_one_server_status_code(self, setup):
        assert setup[0]["status"] == 0

    def test_request_correct_value_to_platforms_one_server_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_correct_value_to_platforms_one_server_description_value(self, setup):
        assert setup[0]["description"] == 'Done'

    def test_request_correct_value_to_platforms_one_server_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_correct_value_to_platforms_one_server_check_data_in_db(self, setup):
        assert setup[1] == default_list

    def test_request_correct_value_to_platforms_one_server_result_value(self, setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'status': 0, 'platform': 'MT5_MARKET_REAL'}]


class Test_Correct_Value_To_Platforms_Two_Servers():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Default_for_autotest",
                "platforms": ["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_correct_value_to_platforms_two_servers_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_correct_value_to_platforms_two_servers_status_code(self, setup):
        assert setup[0]["status"] == 0

    def test_request_correct_value_to_platforms_two_servers_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_correct_value_to_platforms_two_servers_description_value(self, setup):
        assert setup[0]["description"] == 'Done'

    def test_request_correct_value_to_platforms_two_servers_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_correct_value_to_platforms_two_servers_check_data_in_db(self, setup):
        assert setup[1] == default_list

    def test_request_correct_value_to_platforms_two_servers_result_value(self, setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                      {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}]


class Test_Value_To_Platforms_Two_Servers_One_Not_In_Config():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "For_AutoTest",
                "platforms": ["MT5_MARKET_REAL", "MT5_FOR_TEST"]
            }
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_value_to_platforms_two_servers_one_not_in_config_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_value_to_platforms_two_servers_one_not_in_config_status_code(self, setup):
        assert setup[0]["status"] == 7

    def test_request_value_to_platforms_two_servers_one_not_in_config_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_value_to_platforms_two_servers_one_not_in_config_description_value(self, setup):
        assert setup[0]["description"] == 'One or more updates are failed'

    def test_request_value_to_platforms_two_servers_one_not_in_config_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_value_to_platforms_two_servers_one_not_in_config_check_data_in_db(self, setup):
        assert setup[1] == default_list

    def test_request_value_to_platforms_two_servers_one_not_in_config_result_value(self, setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                        {'description': 'No information in config', 'platform': 'MT5_FOR_TEST', 'status': 2}]


class Test_Not_Found_Platform_In_Profile():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile":
                {
                 "name": "Default_for_autotest",
                "platforms": ["MT5_TEST"]
                }
            }
        return Connection().Change_Profile_true_url(data)

    def test_request_not_found_platform_in_profile_status(self, setup):
        assert "status" in setup.keys()

    def test_request_not_found_platform_in_profile_status_code(self, setup):
        assert setup["status"] == 7

    def test_request_not_found_platform_in_profile_description(self, setup):
        assert "description" in setup.keys()

    def test_request_not_found_platform_in_profile_description_value(self, setup):
        assert setup["description"] == 'One or more updates are failed'

    def test_request_not_found_platform_in_profile_result(self, setup):
        assert "Result" in setup.keys()

    def test_request_not_found_platform_in_profile_result_value(self, setup):
        assert setup["Result"] == [{'description': 'No information in config', 'platform': 'MT5_TEST', 'status': 2}]

#############################################################################
#Проверка кодов ответа
#############################################################################
class Test_response_code():
    class Test_response_code_2_and_7():
        @pytest.fixture(scope='class')
        def setup(self):
            data = {
                "tradingProfile":
                    {
                        "name": "Default_for_autotest",
                        "platforms": ["MT5_TEST"]
                    }
            }
            return Connection().Change_Profile_true_url(data)

        def test_request_not_found_platform_in_profile_status(self, setup):
            assert "status" in setup.keys()

        def test_request_not_found_platform_in_profile_status_code(self, setup):
            assert setup["status"] == 7

        def test_request_not_found_platform_in_profile_description(self, setup):
            assert "description" in setup.keys()

        def test_request_not_found_platform_in_profile_description_value(self, setup):
            assert setup["description"] == 'One or more updates are failed'

        def test_request_not_found_platform_in_profile_result(self, setup):
            assert "Result" in setup.keys()

        def test_request_not_found_platform_in_profile_result_value(self, setup):
            assert setup["Result"] == [{'description': 'No information in config', 'platform': 'MT5_TEST', 'status': 2}]

    class Test_Response_code_3():
        @pytest.fixture(scope='class')
        def setup(self):
            data = {
                "tradingProfile": {
                    "name": "Default_for_autotest",
                    "platforms": ["MT5_MARKET_REAL"]
                }
            }
            return Connection().Change_Profile_false_url(data)

        def test_false_url_status(self, setup):
            assert "status" in setup.keys()

        def test_false_url_status_code(self, setup):
            assert setup["status"] == 3

        def test_false_url_description(self, setup):
            assert "description" in setup.keys()

        def test_false_url_description_value(self, setup):
            assert setup["description"] == 'invalid uri'

    class Test_response_code_4():
        @pytest.fixture(scope='class')
        def setup(self):
            data = {
                "tradingProfile": {"platforms": ["MT5_MARKET_REAL"]}
            }
            return Connection().Change_Profile_true_url(data)

        def test_request_without_name_status(self, setup):
            assert "status" in setup.keys()

        def test_request_without_name_status_code(self, setup):
            assert setup["status"] == 4

        def test_request_without_name_description(self, setup):
            assert "description" in setup.keys()

        def test_request_without_name_description_value(self, setup):
            assert setup["description"] == "can't read 'name' param"

    class Test_response_code_5():
        @pytest.fixture(scope='class')
        def setup(self):
            data = {
                "tradingProfile": {
                    "name": 123456,
                    "platforms": ["MT5_INSTANT_REAL"]
                }
            }
            return Connection().Change_Profile_true_url(data)

        def test_request_value_to_name_not_str_status(self, setup):
            assert "status" in setup.keys()

        def test_request_value_to_name_not_str_status_code(self, setup):
            assert setup["status"] == 5

        def test_request_value_to_name_not_str_description(self, setup):
            assert "description" in setup.keys()

        def test_request_value_to_name_not_str_description_value(self, setup):
            assert setup["description"] == "element 'name' not string"

    class Test_response_code_6_and_7():
        @pytest.fixture(scope='class')
        def setup(self):
            data = {
                "tradingProfile": {
                    "name": "For_AutoTest",
                    "platforms": ["MT5_TEST"]
                }
            }
            return Connection().Change_Profile_true_url(data)

        def test_request_no_connection_with_server_status(self, setup):
            assert "status" in setup.keys()

        def test_request_no_connection_with_server_status_code(self, setup):
            assert setup["status"] == 7

        def test_request_no_connection_with_server_description(self, setup):
            assert "description" in setup.keys()

        def test_request_no_connection_with_server_description_value(self, setup):
            assert setup["description"] == 'One or more updates are failed'

        def test_request_no_connection_with_server_result(self, setup):
            assert "Result" in setup.keys()

        def test_request_no_connection_with_server_result_value(self, setup):
            assert setup["Result"] == [{'description': 'No connection','platform': 'MT5_TEST','status': 6}]


# #############################################################################
# #Check invalid json
# #############################################################################
#
class Test_No_Valid_Json_1():
    @pytest.fixture(scope='class')
    def setup(self):
        data = '{"tradingProfile":{"name":"Default_for_autotest","platforms":["MT5_MARKET_REAL"]}}'
        return Connection().Change_Profile_true_url(data)

    def test_request_no_valid_json_1_status(self, setup):
        assert "status" in setup.keys()

    def test_request_no_valid_json_1_status_code(self, setup):
        assert setup["status"] == 1

    def test_request_no_valid_json_1_description(self, setup):
        assert "description" in setup.keys()

    def test_request_no_valid_json_1_description_value(self, setup):
        assert setup["description"] == 'in Json::Value::find(key, end, found): requires objectValue ''or nullValue'

    class Test_No_Valid_Json_2():
        @pytest.fixture(scope='class')
        def setup(self):
            data = "{\"tradingProfile:{\"name\":\"Default_for_autotest\",\"platforms\":[\"MT5_MARKET_REAL\"]}}"
            return Connection().Change_Profile_wrong_json(data)

        def test_request_no_valid_json_2_status(self, setup):
            assert "status" in setup.keys()

        def test_request_no_valid_json_2_status_code(self, setup):
            assert setup["status"] == 5

        def test_request_no_valid_json_2_description(self, setup):
            assert "description" in setup.keys()

        def test_request_no_valid_json_2_description_value(self, setup):
            assert setup["description"] == 'invalid json'

class Test_Default_Mode():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {
            "tradingProfile": {
                "name": "Default",
                "platforms": ["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        return Connection().Change_Profile_true_url(data), get_data_from_db()

    def test_request_correct_value_to_platforms_two_servers_status(self, setup):
        assert "status" in setup[0].keys()

    def test_request_correct_value_to_platforms_two_servers_status_code(self, setup):
        assert setup[0]["status"] == 0

    def test_request_correct_value_to_platforms_two_servers_description(self, setup):
        assert "description" in setup[0].keys()

    def test_request_correct_value_to_platforms_two_servers_description_value(self, setup):
        assert setup[0]["description"] == 'Done'

    def test_request_correct_value_to_platforms_two_servers_result(self, setup):
        assert "Result" in setup[0].keys()

    def test_request_correct_value_to_platforms_two_servers_check_data_in_db(self, setup):
        assert setup[1] == default_list

    def test_request_correct_value_to_platforms_two_servers_result_value(self, setup):
        assert setup[0]["Result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                      {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0}]