from flask import *
from flask_sqlalchemy import SQLAlchemy
from ORM import Videocards


app = Flask(__name__)

# class Videocards():
#     def init(self, name, core, techprocess, transistors, core_clock, shaders_clock, shaders, memory_bus, interface, energousage, date, picture_url):
#         self.name = name
#         self.core = core
#         self.techprocess = techprocess
#         self.transistors = transistors
#         self.core_clock = core_clock
#         self.shaders_clock = shaders_clock
#         self.shaders = shaders
#         self.memory_bus = memory_bus
#         self.interface = interface
#         self.energousage = energousage
#         self.date = date
#         self.picture_url = picture_url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NewDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def setup():
    return redirect('/code')

@app.route('/code')
def code():
    return render_template('code.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/catalog')
def catalog(items):
    d = list(Videocards.query.all())
    return render_template('catalog.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/RTX3070')
def RTX3070():
    return render_template('RTX3070.html')

@app.route('/RTX3080')
def RTX3080():
    return render_template('RTX3080.html')

@app.route('/RTX3090')
def RTX3090():
    return render_template('RTX3090.html')


if __name__ == '__main__':
    print(list(Videocards.query.all())[0])
    app.run(debug=True)
