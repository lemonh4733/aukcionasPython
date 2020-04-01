from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "becf55ac435bb4faa6c925ec354b84b5"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref='owner', lazy=True)

    def __repr__(self):
        return "User('{self.username}','{self.email}')"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    min_price = db.Column(db.Integer, nullable=False)
    auction_image = db.Column(db.String(256), nullable=False)
    end_day = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return """Item('{self.name}','{self.category}"""


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page")

@app.route('/about')
def about():
    return render_template('about.html', title="About Page")

@app.route('/register', methods=['GET', 'POST'])
def register():
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
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin123":
            flash('You Logged In!', 'success')
            return redirect(url_for('home'))
        else: 
            flash('Login unsuccessful!', 'danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)