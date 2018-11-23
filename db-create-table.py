#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test')


cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")


sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql);

print ("Database version : %s " % sql)

# disconnect from server
db.close()