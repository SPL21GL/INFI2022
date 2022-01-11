# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Todoitem(db.Model):
    __tablename__ = 'todoitems'

    itemId = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    dueDate = db.Column(db.Date)
    isDone = db.Column(db.Integer)
