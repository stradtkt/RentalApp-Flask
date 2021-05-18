from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
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


@app.route('/about', methods=('GET',))
def about():
    header = {
        "img_url": "assets/img/bg1.jpg",
        "title": "About Home At Last",
        "subtitle": "About Home At Last. Welcome to the about page where you can learn about our company and our mission statement."
    }
    return render_template("about.html", header=header)


@app.route('/contact', methods=('GET',))
def contact():
    header = {
        "img_url": "assets/img/bg2.jpg",
        "title": "Contact Home At Last",
        "subtitle": "Contact Home At Last and we will get back to you in a short amount of time!"
    }
    return render_template("contact.html", header=header)


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
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
        header = {
            "img_url": "assets/img/bg7.jpg",
            "title": "Login To Your Account",
            "subtitle": "Login to your account so you can make payments or find the next home you want to live in!",
        }
        return render_template("login.html", header=header)


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        valid = True
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = _md5.md5(request.form['password']).hexdigest()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cur.fetchone()
        if user:
            flash("Email already exists", "info")
            return redirect("/login")
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
            cur.execute('INSERT INTO users VALUES (%s, %s, %s, %s, %s)',
                        (first_name, last_name, username, email, password))
            cur.connection.commit()
            flash("Successfully Registered. Login now", 'success')
            return redirect('/login')
    else:
        header = {
            "img_url": "assets/img/bg6.jpg",
            "title": "Register Today",
            "subtitle": "You are just a form away from becoming a member to this site to find the house or condo that you love!",
        }
        return render_template("register.html", header=header)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/admin', methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        pass
    else:
        return render_template("admin/index.html")


if __name__ == '__main__':
    app.run()
