from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField

class AddUser(FlaskForm):
    custName = StringField("Full Name")
    email = StringField("Email")
    birthDate = DateField("Date of Birth")
    number = IntegerField("Phone Number")
    submit = SubmitField("Register")