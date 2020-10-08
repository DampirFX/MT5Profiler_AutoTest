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