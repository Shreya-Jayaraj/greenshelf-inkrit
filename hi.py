from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newshelf'
    CORS(app)
    return app

app = create_app()
db = SQLAlchemy(app)

class Login(db.Model):
    Username = db.Column(db.String(200), primary_key=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.Integer)

class Item_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    item_image  = db.Column(db.String(600),nullable = False)
    prod_desc = db.Column(db.String(500))
    owner_uname = db.Column(db.String(200),nullable = False)
    qty = db.Column(db.Integer)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        """new_login = Login(Username="hannah", password="abcd", phone_no="9881231417")
        db.session.add(new_login)
        db.session.commit()
        app.run(debug=True)"""
    

@app.route('/create-item', methods=['POST'])
def create_item():
    data = request.get_json()

    new_item = Item_Details(
        item=data.get('item'),
        item_image=data.get('item_image'),
        prod_desc=data.get('prod_desc'),
        owner_uname=data.get('owner_uname'),
        qty = data.get('qty')
    )

    db.session.add(new_item)
    db.session.commit()

    return "Item created successfully"

@app.route('/create-item', methods=['PUT'])
def update_phone():
    data = request.get_json()
    owner_uname = data.get('owner_uname')
    phone_no = data.get('phone_no')
    owner = Login.query.filter_by(Username=owner_uname).first()

    owner.phone_no = phone_no
    db.session.commit()
    return jsonify({'message': 'Phone number updated successfully'})

@app.route('/home', methods=['GET'])
def display():
    items = Item_Details.query.all()
    item_list = [{'id': item.id, 'item': item.item, 'item_image': item.item_image, 'prod_desc':item.prod_desc, 'owner_uname':item.owner_uname, 'qty':item.qty} for item in items]
    return jsonify({'items': item_list})

@app.route('/delete-item', methods=['DELETE'])
def delete():
    data = request.get_json()
    item_name = data.get('item')
    item = Item_Details.query.filter_by(item=item_name).first()
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)