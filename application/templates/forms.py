from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField

class AddUser(FlaskForm):
    custName = StringField("name")
    email = EmailField("mail")
    birthDate = DateField("dob")
    number = IntegerField("num")
