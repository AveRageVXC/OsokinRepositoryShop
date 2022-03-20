from flask import *

app = Flask(__name__)

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
def catalog():
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
    app.run(debug=True)