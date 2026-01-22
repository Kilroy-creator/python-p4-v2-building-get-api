from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    
    baked_goods = db.relationship('BakedGood', backref='bakery', lazy=True)
    
    serialize_rules = ('-baked_goods.bakery',)
    
    def __repr__(self):
        return f'<Bakery {self.id}: {self.name}>'

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    
    serialize_rules = ('-bakery.baked_goods',)
    
    def __repr__(self):
        return f'<BakedGood {self.id}: {self.name} - ${self.price}>'