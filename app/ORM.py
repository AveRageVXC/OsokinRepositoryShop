from app.setup import db
import hashlib, datetime, os

class Users(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
    name = db.Column(db.String(100), nullable = False, unique=True)
    password = db.Column(db.String(30), nullable = False)
    date_of_registration = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'{self.id} {self.name}'
    
    def validate(self, password):
        return self.password == hashlib.md5(password.encode("utf8")).hexdigest()

    def set_password(self, password):
        self.password = hashlib.md5(password.encode('utf8')).hexdigest()

class Videocards(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(100), unique=True)
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
    
    def inc_amount(self, amount):
        self.quantity += amount

    def dec_amount(self, amount):
        self.quantity -= amount
    
    

class Products_In_Cart(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.Integer, db.ForeignKey(Videocards.id), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_visible = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'{self.id} {self.name}'

    def update_visibility(self):
        self.is_visible = False
    
    def inc_amount(self, amount):
        self.quantity += amount

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text)

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
                        picture_url = '3070.jpg',
                        price = 120000,
                        quantity = 1000)

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
                        picture_url = '3080.jpg',
                        price = 1900000,
                        quantity = 100)

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
                        picture_url = '3090.jpg',
                        price = 270000,
                        quantity = 100)
    
    feedback = Reviews(name='раян гослинг',
        email='tayangosling@rayangosling.com',
        text='купил 3 видеокарты в этом магазине. выбило пробки дома. ни о чем не жалею. 5 звезд.'
    )
    db.session.add(feedback)

    if len(list(Users.query.all())) == 0:
        dummy = Users(
                    name='vlad',
                    password=''
                )
        dummy.set_password('12345678')
        db.session.add(dummy)   

    db.session.add(RTX3070)
    db.session.add(RTX3080)
    db.session.add(RTX3090)
    db.session.commit()

def create_db():
    db.create_all()

def get_videocard_by_url(name):
    return Videocards.query.filter(Videocards.name == name).one()

def get_videocard_id_by_url(name):
    return Videocards.query.filter(Videocards.name == name).one().id

def get_videocards():
    return Videocards.query.all()

def get_reviews():  
    return Reviews.query.all()

def get_cart_for_user(user_id):
    return Products_In_Cart.query.filter(Users.id == user_id)

def disable_cart_for_user(user_id):
    cart = get_cart_for_user(user_id)
    for cart_item in cart:
        cart_item.update_visibility()
        db.session.add(cart_item)
    db.session.commit()

def get_total_price_for_user(user_id):
    cart = get_cart_for_user(user_id)
    total_price = 0
    for cart_item in cart:
        if cart_item.is_visible:
            total_price += cart_item.quantity * cart_item.price
    return total_price
