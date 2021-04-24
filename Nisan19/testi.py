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
    if request.headers.get("bootcamp") == "devops":
        return render_template('devops.html')
    if request.method == "POST":
        details = request.form
        kilo = details['weight']
        boy = details['height']
        cur = mysql.connection.cursor()
        insert_query = """INSERT INTO sizes(kilo, boy) VALUES (%s, %s)"""
        cur.execute(insert_query,(kilo, boy))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
    cur = mysql.connection.cursor()
    get_query = """SELECT boy, kilo FROM sizes"""
    cur.execute(get_query)
    result=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return str(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
