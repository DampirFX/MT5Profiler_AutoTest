import pymysql
import time
import json

# IP = 'rds.mt.qa-env.com'
# PORT = 3306
# LOGIN = 'tester'
# PASSWORD = '1q2w3e4r'
# REPEAT_INTERVAL = 100
# MAX_TIMEOUT = 10000

class Connection_To_DB(object):
    def __init__(self):
        with open('src/credentials.json', "r") as read_file:
            self.data_set = json.load(read_file)

    def db_connection(self):
        db = pymysql.connect(host= self.data_set["IP_DB"], port=self.data_set["PORT_DB"], user=self.data_set["LOGIN_DB"], passwd=self.data_set["PASSWORD_DB"], db=self.data_set["PATH_DB"])
        return db

    def db_select(self,db, REQUEST):
        start_time = time.time()
        while time.time() - start_time < self.data_set["MAX_TIMEOUT_DB"]:
            c = db.cursor()
            c.execute(REQUEST)
            db_resp = c.fetchone()
            if db_resp is not 'None':
                break
            time.sleep(self.data_set["REPEAT_INTERVAL_DB"])
        if db_resp is 'None':
            print('No response')
        else:
            return(db_resp)

    def db_close_connection(self,db):
        db.close()

    def get_data_from_db(self):
        db_real = Connection_To_DB().db_connection()
        R1 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Forex Timeout Market'")
        R2 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='RU Timeout Market'")
        R3 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Energy Timeout Market'")
        R4 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 1'")
        R5 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 1'")
        R6 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 2'")
        R7 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 2'")
        R8 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Forex Timeout Market'")
        R9 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='RU Timeout Market'")
        R10 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Energy Timeout Market'")
        R11 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 1'")
        R12 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 1'")
        R13 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 2'")
        R14 = Connection_To_DB().db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 2'")
        Connection_To_DB().db_close_connection(db_real)

        return R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14

    # def cill_connection():
    #     mass = (99360, 99475, 99581, 99656, 99792, 99892, 100067, 100167, 100412, 100601, 100706, 100846, 100965, 101338, 101541, 101714, 101965, 102117, 102312, 102445, 102537, 102743, 103097, 103342, 103410, 104379, 104468, 104775, 105052, 105248, 105353, 105781, 106108, 106466, 106541, 106690, 106839)
    #     db = db_connection("fxqatservice")
    #     for i in mass:
    #         print(i)
    #         db_select(db,'kill connection ' + str(i))
    #     db_close_connection(db)
    #
    # cill_connection()