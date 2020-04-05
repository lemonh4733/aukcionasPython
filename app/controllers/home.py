from flask import render_template, url_for, flash, redirect, request
from app.forms import SearchForm
from app import App
from app.user import User
from app.item import Item
from app.offer import Offer
from app.category import Category
from pprint import pprint

@App.route('/')
def home():
    form = SearchForm()
    categories = Category.query.all()

    datalist = Item.query.all()

    items = Item.query.order_by(Item.id.desc()).limit(4)
    items2 = Item.query.order_by(Item.id.desc()).offset(4).limit(4)

    trending = Item.query.order_by(Item.views.desc()).limit(4)
    trending2 = Item.query.order_by(Item.views.desc()).offset(4).limit(4)
    return render_template('home.html', title="Home Page", items=items, items2=items2, trending=trending, trending2=trending2, form=form, categories=categories, datalist=datalist)

@App.route('/search', methods=["POST", "GET"])
def search():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    query = form.search.data
    items = Item.query.order_by(Item.id.desc()).filter(Item.name.like("%"+query+"%")).all()


    return render_template('search.html', title="Search query: "+query, items=items, form=form)

@App.route('/about')
def about():
    return render_template('about.html', title="About Page")

@App.route('/all')
def all():
    page = request.args.get('page', 1, type=int)
    items = Item.query.order_by(Item.id.desc()).paginate(page=page, per_page=12)
    return render_template('all.html', title="All Items", items=items)