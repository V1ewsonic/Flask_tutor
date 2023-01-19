from flask_mysqldb import MySQL
from flask import Flask, render_template, url_for, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

# ROUTING
@app.route('/dosen')
def dosen():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM DOSEN''')
    dosen = cursor.fetchall()
    cursor.close()

    return render_template('dosen.html', dosen=dosen)