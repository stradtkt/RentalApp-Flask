from db import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=False, nullable=False)
    last_name = db.Column(db.String, unique=False, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password


class Owners(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=False, nullable=False)
    last_name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    photo = db.Column(db.BLOB, unique=False, nullable=True)
    description = db.Column(db.TEXT, unique=False, nullable=True)
    phone = db.Column(db.String, unique=False, nullable=True)

    def __init__(self, first_name, last_name, email, photo, description, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.photo = photo
        self.description = description
        self.phone = phone


class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('Owners.id'))
    title = db.Column(db.String, unique=False, nullable=True)
    address = db.Column(db.String, unique=False, nullable=False)
    city = db.Column(db.String, unique=False, nullable=False)
    state = db.Column(db.String, unique=False, nullable=False)
    zipcode = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.TEXT, unique=False, nullable=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    beds = db.Column(db.Integer, unique=False, nullable=False)
    baths = db.Column(db.DECIMAL, unique=False, nullable=False)
    garage = db.Column(db.Integer, unique=False, nullable=False)
    sqft = db.Column(db.Integer, unique=False, nullable=False)
    lotsize = db.Column(db.Integer, unique=False, nullable=False)
    photo_main = db.Column(db.BLOB, unique=False, nullable=False)
    photo_1 = db.Column(db.BLOB, unique=False, nullable=True)
    photo_2 = db.Column(db.BLOB, unique=False, nullable=True)
    photo_3 = db.Column(db.BLOB, unique=False, nullable=True)
    photo_4 = db.Column(db.BLOB, unique=False, nullable=True)
    photo_5 = db.Column(db.BLOB, unique=False, nullable=True)
    photo_6 = db.Column(db.BLOB, unique=False, nullable=True)
    photo_7 = db.Column(db.BLOB, unique=False, nullable=True)

    def __init__(self, title, address, city, state, zipcode, description, price, beds, baths, garage, sqft, lotsize, photo_main, photo_1, photo_2, photo_3, photo_4, photo_5, photo_6, photo_7):
        self.title = title
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.description = description
        self.price = price
        self.beds = beds
        self.baths = baths
        self.garage = garage
        self.sqft = sqft
        self.lotsize = lotsize
        self.photo_main = photo_main
        self.photo_1 = photo_1
        self.photo_2 = photo_2
        self.photo_3 = photo_3
        self.photo_4 = photo_4
        self.photo_5 = photo_5
        self.photo_6 = photo_6
        self.photo_7 = photo_7


class Contacts(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    prop = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=False, nullable=True)
    message = db.Column(db.Text, unique=False, nullable=False)
    contact_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now)
    property_id = db.Column(db.Integer, db.ForeignKey('Property.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, prop, name, email, phone, message, contact_date, property_id, user_id):
        self.prop = prop
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
        self.contact_date = contact_date
        self.property_id = property_id
        self.user_id = user_id
