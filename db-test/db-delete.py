#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test')

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > %d" % (19)

try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()
