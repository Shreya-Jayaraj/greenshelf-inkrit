from flask import Flask, request
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
class Item_Qty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    qnty = db.Column(db.Integer)

class Item_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    item_image  = db.Column(db.String(600),nullable = False)
    prod_desc = db.Column(db.String(500))
    owner_uname = db.Column(db.String(200),nullable = False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        new_login = Login(Username="abhi", password="Karakkat", phone_no="9876543214")
        db.session.add(new_login)
        db.session.commit()
    app.run(debug=True)

@app.route('/create-item', methods=['POST'])
def create_item():
    data = request.get_json()

    new_item = Item_Details(
        id = data.get('id'),
        item = data.get('item'),
        item_image = data.get('item_image'),
        prod_desc = data.get('prod_desc'),
        owner_uname = data.get('owner_uname')
                            )
    
    db.session.add(new_item)
    db.session.commit()


