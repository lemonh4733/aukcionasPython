from flask import render_template, url_for, flash, redirect, request
from app import App
from app.user import User
from app.item import Item
from app.offer import Offer
from pprint import pprint

@App.route('/')
@App.route('/home')
def home():
    items = Item.query.order_by(Item.id.desc()).limit(4)
    items2 = Item.query.order_by(Item.id.desc()).offset(4).limit(4)
    return render_template('home.html', title="Home Page", items=items, items2=items2)

@App.route('/about')
def about():
    return render_template('about.html', title="About Page")

@App.route('/all')
def all():
    page = request.args.get('page', 1, type=int)
    items = Item.query.order_by(Item.id.desc()).paginate(page=page, per_page=12)
    return render_template('all.html', title="All Items", items=items)