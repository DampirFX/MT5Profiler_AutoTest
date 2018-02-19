from Cases import *
from DB_Connector import *


#print(check_db())
result=db_connection("SELECT mode, ActionValueUInt,ActionType FROM mt5_routing where name='CFD Timeout'")
print(result)
if result == [0,3000,3]:
    print('OK')
else:
    print('false')
