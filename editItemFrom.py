from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField

class EditItemForm(FlaskForm):
    itemId = HiddenField("itemId")
    title = StringField("title")
    description = TextAreaField("description")
    dueDate = DateField("dueDate")
    isDone = BooleanField("isDone")