import pymysql
import time


IP = 'rds.mt.qa-env.com'
PORT = 3306
LOGIN = 'tester'
PASSWORD = '1q2w3e4r'
REPEAT_INTERVAL = 100
MAX_TIMEOUT = 10000


def db_connection(PATH):
    db = pymysql.connect(host= IP, port=PORT, user=LOGIN, passwd=PASSWORD, db=PATH)
    return db

def db_select(db, REQUEST):
    start_time = time.time()
    while time.time() - start_time < MAX_TIMEOUT:
        c = db.cursor()
        c.execute(REQUEST)
        db_resp = c.fetchone()
        if db_resp is not 'None':
            break
        time.sleep(REPEAT_INTERVAL)
    if db_resp is 'None':
        print('No response')
    else:
        return(db_resp)

def db_close_connection(db):
    db.close()

def get_data_from_db():
    db_real = db_connection("mt5_real")
    R1 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Forex Timeout Market'")
    R2 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='RU Timeout Market'")
    R3 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Energy Timeout Market'")
    R4 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 1'")
    R5 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 1'")
    R6 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 2'")
    R7 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 2'")

    R8 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Forex Timeout Market'")
    R9 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='RU Timeout Market'")
    R10 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Energy Timeout Market'")
    R11 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 1'")
    R12 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 1'")
    R13 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market 2'")
    R14 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market 2'")
    db_close_connection(db_real)

    return R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14