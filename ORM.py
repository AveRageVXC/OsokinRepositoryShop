from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    surname = db.Column(db.String(100), nullable = False)
    login = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.BigInteger, nullable = False)
    telephone = db.Column(db.String(15), nullable = False, unique = True)
    date_of_registration = db.Column(db.String(10), nullable = False)
    birth_date = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return f'{self.id} {self.name}'

class Orders(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
    user_id = db.Column(db.Integer, nullable = False)
    cost = db.Column(db.Integer, nullable = False)
    provider = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'{self.id} {self.name}'

class Products(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'{self.id} {self.name}'

class Products_In_Cart(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    products_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} {self.name}'



db.create_all()

user = Users(name='Пётр', surname='Чортов', login= 'petya123@mail.ru', telephone='+79165434565', date_of_registration='2016.10.14', birth_date='1998.05.12', password ='542345341' )

db.session.add(user)
db.session.commit()



print(Users.query.all())