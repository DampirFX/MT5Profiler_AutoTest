from ConnectorMT5Profiler import Connection
import allure
from DB_Connector import *
import time


#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
def wrong_request():
    allure.description("Check wrong request")

    FinishResult = falseurl(data)
    return FinishResult
#############################################################################
def no_body_request():
    allure.description("No body on request")
    data = {}
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def request_without_name_and_platform():
    allure.description("No parameters name and platform on request")
    data = {"tradingProfile":{}}
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def request_without_name():
    allure.description("No parameter name on request")
    data = {
        "tradingProfile":{"platforms":["MT5_MARKET_REAL"]}
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def request_without_platforms():
    allure.description("No parameter platforms on request")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{"name":"Crisis_for_autotest"}
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data

#############################################################################
#Проверка параметра Name
#############################################################################
def no_value_to_name():
    allure.description("No value to name")
    data = {
        "tradingProfile":{
            "name":"",
            "platforms":["MT5_INSTANT_REAL"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def value_to_name_not_str():
    allure.description("Value to name not str")
    data = {
        "tradingProfile":{
            "name":123456,
            "platforms":["MT5_INSTANT_REAL"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_name():
    allure.description("Correct value to name")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{
                "name":"Default_for_autotest",
                "platforms":["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()

    return FinishResult, db_data
#############################################################################
def not_found_profile_for_name_value():
    allure.description("Not found profile for name value")
    data = {
        "tradingProfile":{
            "name":"for test",
            "platforms":["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Проверка параметра platforms
#############################################################################
def no_value_to_platforms():
    allure.description("No value to platforms")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{
                "name":"Crisis_for_autotest",
                "platforms":[]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data
#############################################################################
def value_to_platforms_not_str():
    allure.description("Value to platforms not str")
    data = {
        "tradingProfile":{
            "name":"Default_for_autotest",
            "platforms":[123456]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_platforms_one_server():
    allure.description("Correct value to platform")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{
                "name":"Default_for_autotest",
                "platforms":["MT5_MARKET_REAL"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)
    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data
#############################################################################
def correct_value_to_platforms_two_servers():
    allure.description("Correct value to platforms")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{
                "name":"Default_for_autotest",
                "platforms":["MT5_MARKET_REAL","MT5_INSTANT_REAL"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data
#############################################################################
def value_to_platforms_two_servers_one_not_in_config():
    allure.description("Two server one not in the config")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{
                "name":"For_AutoTest",
                "platforms":["MT5_MARKET_REAL","MT5_FOR_TEST"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data
#############################################################################
def not_found_platform_in_profile():
    allure.description("Not found platform in the profile")
    data = {
        "tradingProfile":{
            "name":"Default_for_autotest",
            "platforms":["MT5_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Проверка кодов ответа
#############################################################################
def no_connection_with_server():
    allure.description("No connection with server")
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT5_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Check valid json
#############################################################################
def no_valid_json_1():
    allure.description("No valid json 1")
    data = '{"tradingProfile":{"name":"Default_for_autotest","platforms":["MT5_MARKET_REAL"]}}'
    FinishResult = trueurl(data)
    return FinishResult

def no_valid_json_2():
    allure.description("No valid json 2")
    data = "{\"tradingProfile:{\"name\":\"Default_for_autotest\",\"platforms\":[\"MT5_MARKET_REAL\"]}}"
    FinishResult = trueurl_without_json(data)
    return FinishResult
#############################################################################
#Check DB (work service with MT5Server)
#############################################################################
def check_db_first():                                                                                                     #Описать тест задать несколько файлов с конфигурацией для проверок
    allure.description('Check data in the DB')
    with allure.step('Request'):
        data = {
            "tradingProfile":{
                "name":"For_AutoTest_1",
                "platforms":["MT5_MARKET_REAL",  "MT5_INSTANT_REAL"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data

#############################################################################
def check_db_second():
    allure.description('Check data in the DB')
    with allure.step('Request'):
        data = {
            "tradingProfile":{
                "name":"For_AutoTest_2",
                "platforms":["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data

#############################################################################
#Set default mode
#############################################################################
def default_mode():
    allure.description("Set default mode")
    with allure.step("Sending a request"):
        data = {
            "tradingProfile":{
                "name":"Default_for_autotest",
                "platforms":["MT5_MARKET_REAL", "MT5_INSTANT_REAL"]
            }
        }
        FinishResult = trueurl(data)
    time.sleep(5)

    with allure.step('Check data in the DB'):
        db_data = get_data_from_db()
    return FinishResult, db_data