from ChangeProfile_Request import *
import allure


###################################################################
def wrong_request():
    allure.description("Check wrong request")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT5_REAL", "MT5_REAL2"]
                        }
            }
    FinishResult = falseurl(data)
    return FinishResult
###################################################################