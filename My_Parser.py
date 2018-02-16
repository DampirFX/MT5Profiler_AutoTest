import json


def parsers(s):
    #print('Response\n' + s)
    parsed_string = json.loads(s)
    if len(parsed_string) == 3:
        DescResult = parsed_string["description"]
        StatusResult = parsed_string["status"]
        parsed_string_platforms = parsed_string["result"]                 #Ответ по серверам
        i = 0
        AllPlatforms = []
        while i < len(parsed_string_platforms):
            name = parsed_string_platforms[i]
            AllPlatforms.append(name)
            i = i + 1
            return DescResult,StatusResult, AllPlatforms
        else:
            i = 0
            AllPlatforms = []
            while i < len(parsed_string_platforms):            #складываем в массив набор параметров каждого сервера
                name = parsed_string_platforms[i]
                AllPlatforms.append(name)
                i = i + 1
            return DescResult,StatusResult,AllPlatforms
    else:
        DescResult = parsed_string["description"]
        StatusResult = parsed_string["status"]
    return DescResult, StatusResult


#Памятка по доступу к параметру
#Основные результаты ответа
#FinishResult[0] == 'Done'          - Description
#FinishResult[1] == 0               - Status
#Работа с серверами из Result
#FinishResult[0]                 - первый сервер
#FinishResult[n-1]               - n ый сервер
#FinishResult[0]["description"]  - Description первого сервера
#FinishResult[0]["platform"]       - Server первого сервера
#FinishResult[0]["status"]       - Status первого сервера