from ChangeProfile_Request import *
import allure


#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
def wrong_request():
    allure.description("Check wrong request")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT5_REAL", "MT5_DEMO"]
                        }
            }
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
        "tradingProfile":{"platforms":["MT5_REAL", "MT5_DEMO"]}
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def request_without_platforms():
    allure.description("No parameter platforms on request")
    data = {
        "tradingProfile":{"name":"Default"}
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
#Проверка параметра Name
#############################################################################
def no_value_to_name():
    allure.description("No value to name")
    data = {
        "tradingProfile":{
            "name":"",
            "platforms":["MT5_REAL", "MT5_DEMO"]
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
            "platforms":["MT5_REAL", "MT5_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_name():
    allure.description("Correct value to name")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT5_REAL", "MT5_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def not_found_profile_for_name_value():
    allure.description("Not found profile for name value")
    data = {
        "tradingProfile":{
            "name":"for test",
            "platforms":["MT5_REAL", "MT5_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
#Проверка параметра platforms
#############################################################################
def no_value_to_platforms():
    allure.description("No value to platforms")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":[]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def value_to_platforms_not_str():
    allure.description("Value to platforms not str")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":[123456]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_platforms_one_server():
    allure.description("Correct value to platform")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT5_REAL"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_platforms_two_servers():
    allure.description("Correct value to platforms")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT5_REAL","MT5_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def value_to_platforms_two_servers_one_not_in_config():
    allure.description("Two server one not in the config")
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT5_DEMO","MT5_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def not_found_platform_in_profile():
    allure.description("Not found platform in the profile")
    data = {
        "tradingProfile":{
            "name":"Default",
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