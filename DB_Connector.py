import MySQLdb
import time


IP = '172.16.1.238'
PORT = 3306
LOGIN = 'root'
PASSWORD = '123'
PATH = 'mt5_dev_1'
REPEAT_INTERVAL = 100
MAX_TIMEOUT = 10000
def db_connection(REQUEST):
    db = MySQLdb.connect(host= IP, port=PORT, user=LOGIN, passwd=PASSWORD, db=PATH)
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
    db.close()