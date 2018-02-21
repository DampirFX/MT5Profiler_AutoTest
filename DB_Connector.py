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