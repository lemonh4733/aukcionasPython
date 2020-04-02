from flask import Flask
from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from app.item import Item
from datetime import datetime

App = Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app/database.db"
db = SQLAlchemy(App)

count = 50
faker = Faker()

categories = [
    'Tech', 'Auto', 'Clothes'
]

for i in range(count):
    name = faker.word()
    category = faker.word(categories);
    description = faker.sentence()
    country = faker.country()
    min_price = int(faker.random_int(20, 500))
    end_y = 2020
    end_m = 4
    end_d = 20
    time = faker.random_int(20, 500)
    user_id = 1
    auction_image = "default.jpg"

    new_item = Item(name=name, category=category, description=description, country=country, min_price=min_price, auction_image=auction_image, end_day=datetime(int(end_y), int(end_m), int(end_d)), time=time, user_id=user_id)
    db.session.add(new_item)
    db.session.commit()
    