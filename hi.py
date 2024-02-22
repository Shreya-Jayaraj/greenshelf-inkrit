from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shelf'
    CORS(app)
    return app

app = create_app()
db = SQLAlchemy(app)

class Login(db.Model):
    Username = db.Column(db.String(200), primary_key=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.Integer)


#Login(Username = "abhi",password = "Karakkat" , owner = "abhijith")

class Item_Qty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    qnty = db.Column(db.Integer)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    item_image  = db.Column(db.String(600),nullable = False)
    prod_desc = db.Column(db.String(500))
    owner_uname = db.Column(db.String(200),nullable = False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        '''new_login = Login(Username="abhi", password="Karakkat", phone_no="9188037677")
        db.session.add(new_login)
        db.session.commit()'''
    app.run(debug=True)
