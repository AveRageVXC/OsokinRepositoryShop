from app.ORM import *
from app.setup import *
import sqlalchemy

@app.route('/')
def setup():
    return redirect('/code')

@app.route('/code')
def code():
    return render_template('code.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/items/<card>', methods=['GET', 'POST'])
def render_coffee(card):
    if request.method == 'POST':
        if session.get('login') is not None:
            user = Users.query.filter(Users.name==session.get('login')).one()
            product = get_videocard_by_url(card)
            if user:
                quantity = request.form.get('quantity')
                if get_product_by_url(card).amount >= int(quantity):
                    cartitem = None
                    try:
                        cartitem = Products_In_Cart.query.filter(sqlalchemy.and_(CartItem.product_name==product.name, CartItem.is_visible==True)).one()
                        cartitem.inc_amount(int(quantity))
                    except sqlalchemy.exc.NoResultFound:
                        cartitem = Products_In_Cart(
                            user_id=user.id,
                            product_name=product.name,
                            price=product.price,
                            amount=quantity
                        )

                    product.dec_amount(int(quantity))
                    db.session.add(cartitem)
                    db.session.commit()

                    flash('Товар добавлен в корзину', 'success')
                else:
                    flash('Недостаточно товара на складe', 'warning')
                    
            return render_template("videocard.html", item=get_videocard_by_url(card))

        flash('Пожалуйста, войдите в свой аккаунт, чтобы продолжить', 'warning')
    return render_template("videocard.html", item=get_videocard_by_url(card))

@app.route('/<login>', methods=['GET', 'POST'])
def render_profile(login):
    if session.get('login') == login:
        user = Users.query.filter(Users.name == login).one()
        if request.method == 'POST':
            old_password = request.form.get('old_password')
            new_password = request.form.get('new_password')

            if old_password:
                if user.validate(old_password):
                    user.set_password(new_password)
                    flash('Пароль изменен', 'success')
                    db.session.add(user)
                    db.session.commit()
                elif new_password == None:
                    flash('Новый пароль пуст', 'warning')
                else:
                    flash('Старый пароль неверен', 'warning')
        return render_template('profile.html', user=user, cart=get_cart_for_user(user.id), total_price=get_total_price_for_user(user.id))
        
    flash('Пожалуйста, войдите в свой аккаунт, чтобы продолжить', 'warning')
    return redirect('/login', code=301)

@app.route('/login', methods=["GET", "POST"])
def render_login():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        try:
            if Users.query.filter(Users.name == login).one().validate(password):
                session["login"] = login
                return redirect('/', code=301)
            flash("Неправильный пароль", "warning")
        except sqlalchemy.exc.NoResultFound:
            flash("Неправильный логин", "warning")
    return render_template('login.html')

@app.route("/logout")
def render_logout():
    if session.get("login"):
        session.pop("login")
        flash("Вы вышли из аккаунта", "success")
    return redirect("/", code=302)

@app.route('/catalog')
def catalog():
    cards = Videocards.query.all()
    return render_template('catalog.html', items=cards)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


