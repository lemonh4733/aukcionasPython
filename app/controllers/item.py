import secrets
import os
from flask import render_template, url_for, flash, redirect, request
from app import App, db
from app.forms import AddItemForm, BidForm
from app.user import User
from app.item import Item
from app.offer import Offer
from flask_login import current_user, login_required
from datetime import datetime

@App.route('/add', methods=['GET'])
@login_required
def add_item():
    form = AddItemForm()
    return render_template('add-item.html', title="Add Item", form=form)

def save_image(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(App.root_path, 'static/images', picture_filename)
    form_picture.save(picture_path)
    return picture_filename

@App.route('/add', methods=['POST'])
@login_required
def add_item_post():
    form = AddItemForm()
    name = form.name.data
    category = form.category.data
    description = form.description.data
    country = form.country.data
    min_price = int(form.min_price.data)
    date = request.form["end_day"]
    end_y = date[0:4]
    end_m = date[5:7]
    end_d = date[8:10]
    time = form.time.data
    user_id = current_user.id
    auction_image = save_image(form.auction_image.data)

    new_item = Item(name=name, category=category, description=description, country=country, min_price=min_price, auction_image=auction_image, end_day=datetime(int(end_y), int(end_m), int(end_d)), time=time, user_id=user_id)
    db.session.add(new_item)
    db.session.commit()
    flash('Item post created!', 'success')
    return redirect(url_for('home'))

@App.route('/item/<int:item_id>', methods=['GET'])
@login_required
def item(item_id):
    form = BidForm()
    item = Item.query.get_or_404(item_id)
    offer = Offer.query.filter_by(item_id=item_id).order_by(Offer.id.desc()).first()
    return render_template('single-item.html', title=item.name, item=item, offerLen=len(item.offer), form=form)

@App.route('/my-items/<int:user_id>', methods=['GET'])
@login_required
def items(user_id):
    if user_id == current_user.id:
        items = Item.query.filter_by(user_id=user_id).order_by(Item.id.desc())
        return render_template('my-items.html', title="My Items", items=items)
    flash("You don't have permission", 'danger')
    return redirect(url_for('home'))

@App.route('/offer/<int:item_id>', methods=['POST'])
@login_required
def offer(item_id):
    form = BidForm()
    price = form.offer.data
    item = Item.query.get_or_404(item_id)
    new_offer = Offer(item_id=item_id, user_id=current_user.id, price=int(price))
    db.session.add(new_offer)

    print(price)
    print(item.min_price)
    if item.min_price < price:
        priceUpdate = Item.query.filter_by(id=item_id).first()
        priceUpdate.min_price = price
        db.session.commit()
        flash('Bid successful!', 'success')
    else:
        flash('Price too low!', 'info')
    return redirect(url_for('item',item_id=item_id))

@App.route('/offers/<int:item_id>', methods=['GET'])
@login_required
def offers(item_id):
    offers = Offer.query.filter_by(item_id=item_id)
    return render_template('offers.html', title="Offers", offers=offers)