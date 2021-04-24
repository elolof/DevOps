from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'elif-sql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Elolof19'
app.config['MYSQL_DB'] = 'sizes'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        kilo = details['weight']
        boy = details['height']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sizes(kilo, boy) VALUES (%i, %i)", (kilo, boy))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
