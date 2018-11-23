#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test')


cursor = db.cursor()

try:
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac', 'Mohan', 20, 'M', 2000)
            """

    cursor.execute(sql)
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Krish', 'Prasad', 14, 'M', 2004)
            """

    cursor.execute(sql)
    db.commit()
except:
   db.rollback()

# disconnect from server
db.close()