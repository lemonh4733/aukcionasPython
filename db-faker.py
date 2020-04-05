from flask import Flask
from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from app.item import Item
from app.user import User
from app.category import Category
from datetime import datetime
from werkzeug.security import generate_password_hash

App = Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app/database.db"
db = SQLAlchemy(App)

count = 50
faker = Faker()

def create_admin():
    username = 'admin'
    password = 'admin123'
    email = 'info@auction.lt'

    new_user = User(username=username, email=email, password=generate_password_hash(password, "sha256"))
    db.session.add(new_user)
    db.session.commit()


def create_categories():
    cat1 = Category(cat_name="Fashion")
    cat2 = Category(cat_name="Motors")
    cat2 = Category(cat_name="Electronics")
    cat3 = Category(cat_name="Collectables & antiques")
    cat4 = Category(cat_name="Jewellery & watches")
    cat5 = Category(cat_name="Home & garden")
    cat6 = Category(cat_name="Sporting goods")
    cat7 = Category(cat_name="Toys & games")
    cat8 = Category(cat_name="Other")

    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(cat3)
    db.session.add(cat4)
    db.session.add(cat5)
    db.session.add(cat6)
    db.session.add(cat7)
    db.session.add(cat8)
    db.session.commit()


def create_items():
    for i in range(count):
        name = faker.word()
        description = faker.sentence()
        country = faker.country()
        min_price = int(faker.random_int(20, 500))
        end_y = 2020
        end_m = 4
        end_d = 20
        time = faker.random_int(20, 500)
        user_id = faker.random_int(1, 4)
        auction_image = "default.jpg"
        category_id = faker.random_int(1, 8)

        new_item = Item(name=name, category_id=category_id, description=description, country=country, min_price=min_price, auction_image=auction_image, end_day=datetime(int(end_y), int(end_m), int(end_d)), time=time, user_id=user_id)
        db.session.add(new_item)
        db.session.commit()

create_admin()
create_categories()
create_items()
    