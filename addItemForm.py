from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms import validators

class AddItemForm(FlaskForm):
    title = StringField("title",validators=[validators.InputRequired()])
    description = TextAreaField("description", validators=[validators.InputRequired(), validators.Length(5, 20)])
    dueDate = DateField("dueDate")
    isDone = BooleanField("isDone")