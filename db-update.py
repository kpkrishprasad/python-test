#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test')

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE AGE < 15"

try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()
