from flask import Flask
import db_utils

app = Flask(__name__)


@app.route("/")
def hello():
    students = db_utils.get_all_students()
    output = ""
    for student in students:
        output += student.first_name + "," + student.last_name + "," + student.city
    return output

@app.route("/ping")
def ping():
    return "pong"

@app.route("/table")
def table():
    return """
        <html>
        <body>
        <table border="1" bgcolor="lightblue" cellpadding="10" align="center" f>
            <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Age</th>
            </tr>
            <tr>
                <td>Jill</td>
                <td>Smith</td>
                <td>50</td>
            </tr>
            <tr>
                <td>Eve</td>
                <td>Jackson</td>
                <td>94</td>
            </tr>
        </table>
        </body>
        </html>
    """

@app.route("/students")
def students():
    header = """
     <html>
         <body>
    """

    footer = """
         </body>
         </html>
    """

    table_headers  = """
         <table border="1" bgcolor="lightblue" cellpadding="10" align="center" f>
             <tr>
                 <th>Firstname</th>
                 <th>Lastname</th>
                 <th>Age</th>
                 <th>City</th>
                 <th>Weight</th>
                 <th>Height</th>
             </tr>
    """

    table_footers = """
         </table>
    """

    table_rows = ""
    students = db_utils.get_all_students()
    for student in students:
        table_rows +=  "<tr>" \
            + "<td>" + student.first_name + "</td>" \
            + "<td>" + student.last_name + "</td>" \
            + "<td>" + str(student.age) + "</td>" \
            + "<td>" + student.city + "</td>" \
            + "<td>" + str(student.weight) + "</td>" \
            + "<td>" + str(student.height) + "</td>" \
            + "</tr>"

    return header + table_headers + table_rows + table_footers + footer




if __name__ == "__main__":
    app.run(host='0.0.0.0')

