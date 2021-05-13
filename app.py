from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'rental_db'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'


@app.route('/', methods=('GET',))
def index():
    header = {
        "img_url": "assets/img/bg8.jpg",
        "title": "Home At Last",
        "subtitle": "Welcome to Home At Last!  Where you can find your next home rental with ease!"
    }
    return render_template("index.html", header=header)


if __name__ == '__main__':
    app.run()
