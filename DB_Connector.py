import MySQLdb
import time


IP = '172.16.1.85'
PORT = 3306
LOGIN = 'tester'
PASSWORD = '1q2w3e4r'
REPEAT_INTERVAL = 100
MAX_TIMEOUT = 10000


def db_connection(PATH):
    db = MySQLdb.connect(host= IP, port=PORT, user=LOGIN, passwd=PASSWORD, db=PATH)
    return  db

def db_select(db, REQUEST):
    start_time = time.time()
    while time.time() - start_time < MAX_TIMEOUT:
        c = db.cursor()
        c.execute(REQUEST)
        db_resp = c.fetchone()
        if db_resp is not None:
            break
        time.sleep(REPEAT_INTERVAL)
    if db_resp is None:
        print('No response')
    else:
        return(db_resp)

def db_close_connection(db):
    db.close()

def get_data_from_db():
    db_real = db_connection("mt5_real")
    db_demo = db_connection("mt5_demo")

    R1 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market'")
    R2 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Market'")
    R3 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Instant'")
    R4 = db_select(db_real, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='Experts Timeout Instant'")
    R5 = db_select(db_demo, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Market'")
    R6 = db_select(db_demo, "SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='All Timeout Instant'")
    db_close_connection(db_real)
    db_close_connection(db_demo)

    return R1, R2, R3, R4, R5, R6