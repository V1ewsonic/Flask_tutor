from flask import Flask, render_template, url_for, redirect, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

# ROUTING
@app.route('/')
def index():
    return "hello world"

@app.route('/nama')
def nama():
    return "halaman nama"

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

@app.route('/mahasiswa')
def halmahasiswa():
    kelas = '4KA14'
    return render_template('mhs.html',kelas=kelas)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dosen'))
    return render_template('login.html')

@app.route('/dosen')
def haldosen():
    alamat = ['Depok','Jakarta','Bogor','Kemang']
    return render_template('dosen.html', alamat=alamat)


if __name__ == '__main__':
    app.run(debug=True, port='3000')
