import sqlite3
from bean.kline_bean import kline
from consts.constants import *

def createTable():
    conn = sqlite3.connect('okex.db')
    print ("Opened database successfully")


        # timestamp = 0
        # low = 0.0
        # high = 0.0
        # open = 0.0
        # close = 0.0
        # volume = 0.0
        # currency_volume = 0.0
        
    c = conn.cursor()
    c.execute('''CREATE TABLE KLINE
        (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
        TYPE         INTEGER         NOT NULL,
        MD5          TEXT            NOT NULL UNIQUE ,
        TIMESTAMP    INTEGER         NOT NULL,
        LOW          REAL,
        HIGH         REAL,
        OPEN         REAL,
        CLOSE        REAL,
        VOLUME       REAL,
        CURRENCY_VOLUME  REAL);''')

    print ("Table created successfully")
    conn.commit()
    conn.close()
    pass


def insert(*args):
    conn = sqlite3.connect('okex.db')
    c = conn.cursor()
    print ("Opened database successfully")

    print(args[0])

    c.execute("INSERT INTO KLINE (ID, TYPE, MD5, TIMESTAMP, LOW, HIGH, OPEN, CLOSE, VOLUME, CURRENCY_VOLUME) \
        VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? )", (kline_type_1min, args[0], args[1], args[2],
        args[3], args[4], args[5], args[6], args[7]))
    
    conn.commit()
    print ("Kline created successfully")
    conn.close()
    
    pass