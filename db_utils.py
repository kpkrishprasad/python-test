import mysql.connector

DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "test"

class Student:
    def __init__(self, first_name = None, last_name = None, age = None, city = None, weight = None, height = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.weight = weight
        self.height = height


def db_connection():
    return mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)

def get_all_students():
    try:
        cnx = db_connection()
        cursor = cnx.cursor()
        cursor.execute("""
          select first_name, last_name, age, city, weight, height from students
        """)
        results = cursor.fetchall()
        students = []
        for row in results:
            students.append(Student(
                first_name=row[0],
                last_name=row[1],
                age=row[2],
                city = row[3],
                weight=row[4],
                height=row[5]
            ))
        return students
    finally:
        cnx.close()

if __name__ == "__main__":
     students = get_all_students()
     for student in students:
         print(student.first_name, student.last_name)


