from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/ooty'
db=SQLAlchemy(app)
class Book(db.Model):
        sno=db.Column(db.Integer,primary_key=True)
        name=db.Column(db.String(80),nullable=False)
        phone_num=db.Column(db.String(12),nullable=False)
        #msg=db.Column(db.Integer,primary_key=True)
        email=db.Column(db.String(30),nullable=False)
