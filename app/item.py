from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    min_price = db.Column(db.Integer, nullable=False)
    offer = db.relationship('Offer', backref='offer', lazy=True)
    auction_image = db.Column(db.String(256), nullable=False)
    end_day = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

