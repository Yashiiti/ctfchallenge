from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abcd1234'
app.config['MYSQL_DB'] = 'flask_mysql_login'

mysql = MySQL(app)
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    x='SELECT * FROM users WHERE username = %s AND password = %s', (username, password)
    print(x)
    y="SELECT * FROM users WHERE username='" + username + "' or password='" + password + "'"
    print(y)
    cursor.execute(y)
    # cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    try:
        user = cursor.fetchone()
    except:
        return "flag{sqli_is_fun"+"}"

    if user:
        session['user_id'] = user[0]
        return "ctf{sqli_is_fun"+"}" 
    else:
        return 'Invalid username or password'
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

