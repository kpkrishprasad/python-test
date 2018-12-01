from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello From Krish!!!"

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


if __name__ == "__main__":
    app.run(host='0.0.0.0')

