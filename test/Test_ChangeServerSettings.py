import pytest
from src.mt5_web_api_connector import MT5Connector
from src.ConnectorMT5Profiler import Connection_To_MT5Profiler

class Test_ChangeServerSettings_Trade_Disabled():
    @pytest.fixture(scope='class')
    def setup(self):
        symbol = 'EURUSD'
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_DISABLED"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data),MT5Connector().get_symbol_settings(symbol)

    def test_changeserversettings_trade_disabled_status(self,setup):
        print("Service Response : ", setup[0])
        assert "status" in setup[0].keys()

    def test_changeserversettings_trade_disabled_status_code(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["status"] == 0

    def test_changeserversettings_trade_disabled_description(self,setup):
        print("Service Response : ", setup[0])
        assert "description" in setup[0].keys()

    def test_changeserversettings_trade_disabled_description_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["description"] == 'Done'

    def test_changeserversettings_trade_disabled_result(self,setup):
        print("Service Response : ", setup[0])
        assert "result" in setup[0].keys()

    def test_changeserversettings_trade_disabled_result_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

    def test_changeserversettings_trade_disabled_server_value(self,setup):
        print("Service Response : ", setup[1])
        assert setup[1]["TradeMode"] == '0'

class Test_ChangeServerSettings_Trade_Longonly():
    @pytest.fixture(scope='class')
    def setup(self):
        symbol = 'EURUSD'
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_LONGONLY"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data),MT5Connector().get_symbol_settings(symbol)

    def test_changeserversettings_trade_longonly_status(self,setup):
        print("Service Response : ", setup[0])
        assert "status" in setup[0].keys()

    def test_changeserversettings_trade_longonly_status_code(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["status"] == 0

    def test_changeserversettings_trade_longonly_description(self,setup):
        print("Service Response : ", setup[0])
        assert "description" in setup[0].keys()

    def test_changeserversettings_trade_longonly_description_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["description"] == 'Done'

    def test_changeserversettings_trade_longonly_result(self,setup):
        print("Service Response : ", setup[0])
        assert "result" in setup[0].keys()

    def test_changeserversettings_trade_longonly_result_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

    def test_changeserversettings_trade_longonly_server_value(self,setup):
        print("Service Response : ", setup[1])
        assert setup[1]["TradeMode"] == '1'

class Test_ChangeServerSettings_Trade_Shortonly():
    @pytest.fixture(scope='class')
    def setup(self):
        symbol = 'EURUSD'
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_SHORTONLY"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data),MT5Connector().get_symbol_settings(symbol)

    def test_changeserversettings_trade_shortonly_status(self,setup):
        print("Service Response : ", setup[0])
        assert "status" in setup[0].keys()

    def test_changeserversettings_trade_shortonly_status_code(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["status"] == 0

    def test_changeserversettings_trade_shortonly_description(self,setup):
        print("Service Response : ", setup[0])
        assert "description" in setup[0].keys()

    def test_changeserversettings_trade_shortonly_description_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["description"] == 'Done'

    def test_changeserversettings_trade_shortonly_result(self,setup):
        print("Service Response : ", setup[0])
        assert "result" in setup[0].keys()

    def test_changeserversettings_trade_shortonly_result_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

    def test_changeserversettings_trade_shortonly_server_value(self,setup):
        print("Service Response : ", setup[1])
        assert setup[1]["TradeMode"] == '2'

class Test_ChangeServerSettings_Trade_Closeonly():
    @pytest.fixture(scope='class')
    def setup(self):
        symbol = 'EURUSD'
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_CLOSEONLY"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data),MT5Connector().get_symbol_settings(symbol)

    def test_changeserversettings_trade_closeonly_status(self,setup):
        print("Service Response : ", setup[0])
        assert "status" in setup[0].keys()

    def test_changeserversettings_trade_closeonly_status_code(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["status"] == 0

    def test_changeserversettings_trade_closeonly_description(self,setup):
        print("Service Response : ", setup[0])
        assert "description" in setup[0].keys()

    def test_changeserversettings_trade_closeonly_description_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["description"] == 'Done'

    def test_changeserversettings_trade_closeonly_result(self,setup):
        print("Service Response : ", setup[0])
        assert "result" in setup[0].keys()

    def test_changeserversettings_trade_closeonly_result_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

    def test_changeserversettings_trade_closeonly_server_value(self,setup):
        print("Service Response : ", setup[1])
        assert setup[1]["TradeMode"] == '3'

class Test_ChangeServerSettings_Trade_Full():
    @pytest.fixture(scope='class')
    def setup(self):
        symbol = 'EURUSD'
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data),MT5Connector().get_symbol_settings(symbol)

    def test_changeserversettings_trade_full_status(self,setup):
        print("Service Response : ", setup[0])
        assert "status" in setup[0].keys()

    def test_changeserversettings_trade_full_status_code(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["status"] == 0

    def test_changeserversettings_trade_full_description(self,setup):
        print("Service Response : ", setup[0])
        assert "description" in setup[0].keys()

    def test_changeserversettings_trade_full_description_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["description"] == 'Done'

    def test_changeserversettings_trade_full_result(self,setup):
        print("Service Response : ", setup[0])
        assert "result" in setup[0].keys()

    def test_changeserversettings_trade_full_result_value(self,setup):
        print("Service Response : ", setup[0])
        assert setup[0]["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

    def test_changeserversettings_trade_full_server_value(self,setup):
        print("Service Response : ", setup[1])
        assert setup[1]["TradeMode"] == '4'

class Test_ChangeServerSettings_Platform_No_In_Settings():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_TEST"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_platform_no_in_settings_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_platform_no_in_settings_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 7

    def test_changeserversettings_platform_no_in_settings_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_platform_no_in_settings_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Partially success'

    def test_changeserversettings_platform_no_in_settings_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_platform_no_in_settings_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Server not found', 'platform': 'MT5_TEST', 'status': 2}]

class Test_ChangeServerSettings_Platform_Not_Str():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":[5],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_platform_not_str_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_platform_not_str_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 1

    def test_changeserversettings_platform_not_str_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_platform_not_str_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == "element 'platforms' not string" #'in Json::Value::asCString(): requires stringValue'

class Test_ChangeServerSettings_Platform_No_In_Request():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_platform_no_in_request_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_platform_no_in_request_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_platform_no_in_request_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_platform_no_in_request_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_platform_no_in_request_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_platform_no_in_request_result_value(self,setup):
        print("Service Response : ", setup)
        assert (setup["result"] == [{'description': 'Done', 'platform': 'MT5_DEMO', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_INSTANT_DEMO', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_MARKET_DEMO', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]
            or

            setup["result"] == [{'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0},
                                {'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                {'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}])


class Test_ChangeServerSettings_Two_Platform_In_Request():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL","MT5_MARKET_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_two_platform_in_request_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_two_platform_in_request_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_two_platform_in_request_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_two_platform_in_request_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_two_platform_in_request_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_two_platform_in_request_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

class Test_ChangeServerSettings_Two_Platform_In_Request_One_Not_In_Setting():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL","MT5_TEST"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_two_platform_in_request_one_not_in_settings_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_two_platform_in_request_one_not_in_settings_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 7

    def test_changeserversettings_two_platform_in_request_one_not_in_settings_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_two_platform_in_request_one_not_in_settings_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Partially success'

    def test_changeserversettings_two_platform_in_request_one_not_in_settings_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_two_platform_in_request_one_not_in_settings_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0},
                                   {'description': 'Server not found', 'platform': 'MT5_TEST', 'status': 2}]

class Test_ChangeServerSettings_No_Symbols_In_Request():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_no_symbols_in_request_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_no_symbols_in_request_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_no_symbols_in_request_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_no_symbols_in_request_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_no_symbols_in_request_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_no_symbols_in_request_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

class Test_ChangeServerSettings_No_Symbol_In_Request():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_no_symbol_in_request_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_no_symbol_in_request_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 4

    def test_changeserversettings_no_symbol_in_request_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_no_symbol_in_request_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == "Request hasn't one or more mandatory parameter"

class Test_ChangeServerSettings_No_Symbol_On_Server():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "AutoTest","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_no_symbol_on_server_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_no_symbol_on_server_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 8

    def test_changeserversettings_no_symbol_on_server_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_no_symbol_on_server_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == "Symbol 'AutoTest' not found"

class Test_ChangeServerSettings_Symbol_Not_Str():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": 5,"tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_symbol_not_str_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_symbol_not_str_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 5

    def test_changeserversettings_symbol_not_str_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_symbol_not_str_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == "element 'symbols' not string"

class Test_ChangeServerSettings_Two_Symbols():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"},{"symbol": "AUDCAD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_two_symbols_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_two_symbols_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_two_symbols_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_two_symbols_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_two_symbols_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_two_symbols_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

class Test_ChangeServerSettings_Two_Symbols_One_Not_Found():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"},{"symbol": "AutoTest","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_two_symbols_one_not_found_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_two_symbols_one_not_found_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 7

    def test_changeserversettings_two_symbols_one_not_found_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_two_symbols_one_not_found_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Partially success'

    def test_changeserversettings_two_symbols_one_not_found_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_two_symbols_one_not_found_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

class Test_ChangeServerSettings_Two_Symbols():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_FULL"},{"symbol": "AUDCAD","tradeMode": "TRADE_FULL"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_two_symbols_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_two_symbols_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_two_symbols_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_two_symbols_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_two_symbols_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_two_symbols_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

class Test_ChangeServerSettings_No_TradeMode_In_Request():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_no_trademode_in_request_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_no_trademode_in_request_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_no_trademode_in_request_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_no_trademode_in_request_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_no_trademode_in_request_result(self,setup):
        print("Service Response : ", setup)
        assert "result" in setup.keys()

    def test_changeserversettings_no_trademode_in_request_result_value(self,setup):
        print("Service Response : ", setup)
        assert setup["result"] == [{'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]

class Test_ChangeServerSettings_TradeMode_Not_Str():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": 5}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_trademode_not_str_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_trademode_not_str_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 5

    def test_changeserversettings_trademode_not_str_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_trademode_not_str_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == "element 'tradeMode' not string"

class Test_ChangeServerSettings_Wrong_Value_For_TradeMode():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {"platforms":["MT5_REAL"],"symbols": [{"symbol": "EURUSD","tradeMode": "TRADE_TEST"}]}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_wrong_value_for_trademode_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_wrong_value_for_trademode_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 5

    def test_changeserversettings_wrong_value_for_trademode_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_wrong_value_for_trademode_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == "element 'tradeMode' not containe proper content"

class Test_ChangeServerSettings_Empty_Body():
    @pytest.fixture(scope='class')
    def setup(self):
        data = {}
        return Connection_To_MT5Profiler().Change_Server_Settings(data)

    def test_changeserversettings_empty_body_status(self,setup):
        print("Service Response : ", setup)
        assert "status" in setup.keys()

    def test_changeserversettings_empty_body_status_code(self,setup):
        print("Service Response : ", setup)
        assert setup["status"] == 0

    def test_changeserversettings_empty_body_description(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_empty_body_description_value(self,setup):
        print("Service Response : ", setup)
        assert setup["description"] == 'Done'

    def test_changeserversettings_empty_body_result(self,setup):
        print("Service Response : ", setup)
        assert "description" in setup.keys()

    def test_changeserversettings_empty_body_result_value(self,setup):
        print("Service Response : ", setup)
        assert (setup["result"] == [{'description': 'Done', 'platform': 'MT5_DEMO', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_INSTANT_DEMO', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_MARKET_DEMO', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                   {'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}]
            or

            setup["result"] == [{'description': 'Done', 'platform': 'MT5_INSTANT_REAL', 'status': 0},
                                {'description': 'Done', 'platform': 'MT5_MARKET_REAL', 'status': 0},
                                {'description': 'Done', 'platform': 'MT5_REAL', 'status': 0}])