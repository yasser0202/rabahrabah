from flask import Flask , render_template , url_for
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import defaultload
from datetime import datetime
from flask import session as login_session
import random , string

app = Flask(__name__)
app.secret_key = "thisshouldbereplacedwithsecretkeywhenin"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rabah.db"
db = SQLAlchemy(app)


#this class represents the table of the user in the database
class  User(db.Model):
       
       #user detials
       id = db.Column(db.Integer,primary_key=True)
       firstname = db.Column(db.String(20),nullable=False)
       lastname = db.Column(db.String(20),nullable=False)
       profession = db.Column(db.String(30),nullable=False)
       willaya = db.Column(db.String(20),nullable=False)
       datecreated = db.Column(db.DateTime , default=datetime.utcnow)

       #contact detial 
       tele = db.Column(db.String(17),nullable=False)
       tele2 = db.Column(db.String(17))
       email = db.Column(db.String(30))        
       
       #whenever new user is created it returns his id
       def  __repr__(self):
           return self.id


@app.route('/')
def index():
    return render_template("index.html")

    
if __name__  == "__main__":
    app.run(debug=True)    