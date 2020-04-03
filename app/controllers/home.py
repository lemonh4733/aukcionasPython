from flask import render_template, url_for, flash, redirect, request
from app import App
from app.user import User
from app.item import Item
from app.offer import Offer
from pprint import pprint

@App.route('/')
@App.route('/home')
def home():
    items = Item.query.order_by(Item.id.desc()).all()
    Offer.query.order_by(Offer.id.desc()).all()
    return render_template('home.html', title="Home Page", items=items)

@App.route('/about')
def about():
    return render_template('about.html', title="About Page")