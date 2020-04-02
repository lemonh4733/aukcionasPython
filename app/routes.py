from flask import render_template, url_for, flash, redirect, request
from app import App, db
from app.forms import RegistrationForm, LoginForm, AddItemForm
from app.user import User
from app.item import Item
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

@App.route('/')
@App.route('/home')
def home():
    items = Item.query.all()
    return render_template('home.html', title="Home Page", items=items)

@App.route('/about')
def about():
    return render_template('about.html', title="About Page")

@App.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        check_user = User.query.filter_by(username=username).first()
        check_email = User.query.filter_by(email=email).first()
        if check_user:
            flash('This username already exist!', 'danger')
            return redirect(url_for('register'))
        elif check_email:
            flash('This email already exist!', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username, email=email, password=generate_password_hash(password, "sha256"))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Sign Up", form=form)

@App.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        flash('Login unsuccessful!', 'danger')
    return render_template('login.html', title="Sign In", form=form)

@App.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@App.route('/add', methods=['GET'])
@login_required
def add_item():
    form = AddItemForm()
    return render_template('add-item.html', title="Add Item", form=form)

@App.route('/add', methods=['POST'])
@login_required
def add_item_post():
    name = request.form["name"]
    category = request.form["category"]
    description = request.form["description"]
    country = request.form["country"]
    min_price = int(request.form["min_price"])
    date = request.form["end_day"]
    end_y = date[0:4]
    end_m = date[5:7]
    end_d = date[8:10]
    time = request.form["time"]
    user_id = current_user.id
    auction_image = request.form['auction_image']

    new_item = Item(name=name, category=category, description=description, country=country, min_price=min_price, auction_image=auction_image, end_day=datetime(int(end_y), int(end_m), int(end_d)), time=time, user_id=user_id)
    db.session.add(new_item)
    db.session.commit()
    flash('Item post created!', 'success')
    return redirect(url_for('home'))