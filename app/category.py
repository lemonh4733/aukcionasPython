from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(80), nullable=False)

