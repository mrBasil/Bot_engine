import fdb

from data.config import DB_IP, DB_PATH, DB_PORT, DB_USER, DB_PASSWORD

async def getCon():
     return fdb.connect(dsn=DB_IP+":"+DB_PATH, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)










