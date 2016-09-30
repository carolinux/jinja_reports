from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import RadioField, DateField, SelectField, BooleanField, TextField
from wtforms.validators import DataRequired, Email

class SyncForm(Form):
    email_textbox = TextField("*Your Email(required) [get the notified when sync starts and finishes]",[DataRequired(), Email()], default="")
