from app.setup import db
import hashlib, datetime, os

class Users(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    surname = db.Column(db.String(100), nullable = False)
    login = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(30), nullable = False)
    telephone = db.Column(db.String(15), nullable = False, unique = True)
    date_of_registration = db.Column(db.String(10), nullable = False)
    birth_date = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return f'{self.id} {self.name}'
    
    def validate(self, password):
        return self.password == hashlib.md5(password.encode("utf8")).hexdigest()

    def set_password(self, password):
        self.password = hashlib.md5(password.encode('utf8')).hexdigest()

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

class Videocards(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(100))
    core = db.Column(db.String(100))
    techprocess = db.Column(db.Integer)
    transistors = db.Column(db.Integer)
    core_clock = db.Column(db.Integer)
    shaders_clock = db.Column(db.Integer)
    shaders = db.Column(db.Integer)
    memory_bus = db.Column(db.String(100))
    interface = db.Column(db.String(100))
    energousage = db.Column(db.Integer)
    date = db.Column(db.String(10))
    picture_url = db.Column(db.String(100))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} {self.name} {self.core} {self.techprocess} {self.transistors} {self.core_clock} {self.shaders_clock} {self.shaders} {self.memory_bus} {self.interface} {self.energousage} {self.date} {self.picture_url} {self.price} {self.quantity}'

def start_db():
    RTX3070 = Videocards(name = "RTX3070",
                        core = "GA104",
                        techprocess = 8,
                        transistors = 17400,
                        core_clock = 1500,
                        shaders_clock = 1500,
                        shaders = 5888,
                        memory_bus = "256-bit",
                        interface = "PCI-E 4.0",
                        energousage = 220,
                        date = "15.10.2020",
                        picture_url = "{{ url_for('static', filename='3070.jpg') }}",
                        price = 120000,
                        quantity = 4)

    RTX3080 = Videocards(name = "RTX3080",
                        core = "GA102",
                        techprocess = 8,
                        transistors = 28300,
                        core_clock = 1440,
                        shaders_clock = 1440,
                        shaders = 8704,
                        memory_bus = "320-bit",
                        interface = "PCI-E 4.0",
                        energousage = 320,
                        date = "17.04.2020",
                        picture_url = "{{ url_for('static', filename='3080.jpg') }}",
                        price = 1900000,
                        quantity = 3)

    RTX3090 = Videocards(name = "RTX3090", core = "GA102",
                        techprocess = 8,
                        transistors = 28300,
                        core_clock = 1395,
                        shaders_clock = 1395,
                        shaders = 10496,
                        memory_bus = "384-bit",
                        interface = "PCI-E 4.0",
                        energousage = 350,
                        date = "24.09.2020",
                        picture_url = "{{ url_for('static', filename='3090.jpg') }}",
                        price = 270000,
                        quantity = 2)

    db.session.add(RTX3070)
    db.session.add(RTX3080)
    db.session.add(RTX3090)
    db.session.commit()

def create_db():
    db.create_all()
