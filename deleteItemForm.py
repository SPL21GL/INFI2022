from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField

class DeleteItemForm(FlaskForm):
    itemId = HiddenField("itemId")