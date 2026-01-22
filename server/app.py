from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# GET /bakeries - returns a list of all bakeries with their baked goods
@app.route('/bakeries', methods=['GET'])
def get_bakeries():
    bakeries = Bakery.query.all()
    return jsonify([bakery.to_dict() for bakery in bakeries])

# GET /bakeries/<int:id> - returns a single bakery with its baked goods
@app.route('/bakeries/<int:id>', methods=['GET'])
def get_bakery(id):
    bakery = Bakery.query.get(id)
    if bakery:
        return jsonify(bakery.to_dict())
    return jsonify({"error": "Bakery not found"}), 404

# GET /baked_goods/by_price - returns all baked goods sorted by price (descending)
@app.route('/baked_goods/by_price', methods=['GET'])
def get_baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    return jsonify([baked_good.to_dict() for baked_good in baked_goods])

# GET /baked_goods/most_expensive - returns the most expensive baked good
@app.route('/baked_goods/most_expensive', methods=['GET'])
def get_most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if baked_good:
        return jsonify(baked_good.to_dict())
    return jsonify({"error": "No baked goods found"}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)