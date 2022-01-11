from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField

class AddItemForm(FlaskForm):
    title = StringField("title")
    description = TextAreaField("description")
    dueDate = DateField("dueDate")
    isDone = BooleanField("isDone")