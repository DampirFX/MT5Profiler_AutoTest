import json


def parsers(s):
    #print('Response\n' + s)
    parsed_string = json.loads(s)
    if len(parsed_string) == 3:
        DescResult = parsed_string["Description"]
        StatusResult = parsed_string["Status"]
        parsed_string_servers = parsed_string["Result"]                 #Ответ по серверам
        if len(parsed_string_servers) > 1:                              # Если есть не найденные аккаунты
            AllServers = []
            i = 0
            while i < len(parsed_string_servers["Servers"]):            #складываем в массив набор параметров каждого сервера
                name = parsed_string_servers["Servers"][i]
                AllServers.append(name)
                i = i + 1
            return DescResult,StatusResult,AllServers,(parsed_string_servers["UnknownLogins"])
        else:
            i = 0
            AllServers = []
            while i < len(parsed_string_servers["Servers"]):            #складываем в массив набор параметров каждого сервера
                name = parsed_string_servers["Servers"][i]
                AllServers.append(name)
                i = i + 1
            return DescResult,StatusResult,AllServers
    else:
        DescResult = parsed_string["Description"]
        StatusResult = parsed_string["Status"]
    return DescResult, StatusResult


#Памятка по доступу к параметру
#Основные результаты ответа
#FinishResult[0] == 'Done'          - Description
#FinishResult[1] == 0               - Status
#FinishResult[3] ==                 - если есть доп параметры
#Работа с серверами из Result
#FinishResult[2][0]                 - первый сервер
#FinishResult[2][n-1]               - n ый сервер
#FinishResult[2][0]["Description"]  - Description первого сервера
#FinishResult[2][0]["Logins"]       - Logins первого сервера
#FinishResult[2][0]["Server"]       - Server первого сервера
#FinishResult[2][0]["Status"]       - Status первого сервера