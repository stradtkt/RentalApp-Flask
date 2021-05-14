from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import _md5

app = Flask(__name__)
app.secret_key = 'asdklwsefdshje3l383ur83yro3hro3!@!@#(#(jdksdjskdnkd.v,df.edf,wd.wd,'
mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'rental_db'
mysql.init_app(app)


@app.route('/', methods=('GET',))
def index():
    header = {
        "img_url": "assets/img/bg8.jpg",
        "title": "Home At Last",
        "subtitle": "Welcome to Home At Last!  Where you can find your next home rental with ease!"
    }
    return render_template("index.html", header=header)


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        valid = True
        if request.form['email'] == "":
            valid = False
            flash("Email cannot be empty", "danger")
        if request.form['password'] == "":
            valid = False
            flash("Password cannot be empty", "danger")
        if not valid:
            return redirect("/")
        else:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
            user = cur.fetchone()
            if user:
                session['loggedin'] = True
                session['id'] = user['id']
                session['email'] = user['email']
                flash("You are now logged in!", "success")
            else:
                flash("There has been an error logging you in, try again!", "danger")
                return redirect("login")
    else:
        return render_template("login.html")


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        valid = True
        if request.form['email'] == "":
            valid = False
            flash("Email cannot be empty", 'danger')
        if request.form['first_name'] == "":
            valid = False
            flash("First Name cannot be empty", 'danger')
        if request.form['last_name'] == "":
            valid = False
            flash("Last Name cannot be empty", 'danger')
        if request.form['username'] == "":
            valid = False
            flash("Username cannot be empty", 'danger')
        if request.form['password'] == "":
            valid = False
            flash("Password cannot be empty", 'danger')
        if not valid:
            return redirect('/')
        else:
            try:
                cur = mysql.get_db().cursor()
                data = {
                    "username": request.form['username'],
                    "first_name": request.form['first_name'],
                    "last_name": request.form['last_name'],
                    "email": request.form['email'],
                    "password": _md5.md5(request.form['password']).hexdigest(),
                }
                cur.execute('''INSERT INTO `rental_db`.`users` (`first_name`, `last_name`, `username`, `email`, `password`, `created_at`) VALUES (:first_name, :last_name, :username, :email, :password, now())''')
                cur.commit()
                flash("Successfully Registered. Login now", 'success')
                return redirect('/')
            except Exception as e:
                print(f"{e}")
    else:
        return render_template("register.html")


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('email', None)
   # Redirect to login page
   return redirect(url_for('login'))


@app.route('/admin', methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        return render_template("admin/index.html")
    else:
        return render_template("admin/index.html")

if __name__ == '__main__':
    app.run()
