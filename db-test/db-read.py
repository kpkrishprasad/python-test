#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test')

cursor = db.cursor()

try:
    query = "SELECT * FROM EMPLOYEE WHERE AGE < 25"

    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))

except:
    print("Error: Unable to fetch data.")


# disconnect from server
db.close()
