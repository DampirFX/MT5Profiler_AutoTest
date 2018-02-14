from ChangeProfile_Request import *
from datetime import datetime


filename = datetime.now().strftime("%Y%m%d")
f = open(filename + '.log', 'a+')
###################################################################
#1
def wrong_request():
    test_name = (wrong_request.__name__)        #имя функции вставлять ручками без скобок
    #Проверка неверного запроса
    f = open(filename + '.log', 'a+')
    f.write(datetime.now().strftime("%H:%M:%S") + '   Test ' + test_name + '\n')
    print('\nTest ' + test_name)
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT5_REAL", "MT5_REAL2"]
                        }
            }

    FinishResult = trueurl(data)
    if FinishResult[0] == 'invalid uri':
        if FinishResult[1] == 3:
            result = 'result - OK'
            f.write(datetime.now().strftime("%H:%M:%S") + '   result - OK\n')
        else:
            result = 'result - Failed'
            f.write(datetime.now().strftime("%H:%M:%S") + '   result - Failed: wrong status\n')
    else:
        result = 'result - Failed'
        f.write(datetime.now().strftime("%H:%M:%S") + '   result - Failed: wrong response\n')
    return result
    f.write(datetime.now().strftime("%H:%M:%S")+'   ' + result)
###################################################################
f.close()