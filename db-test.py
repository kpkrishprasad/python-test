#!/usr/bin/python

import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')

try:
    cursor = cnx.cursor()
    cursor.execute("""
      select * from students
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)
finally:
    cnx.close()
