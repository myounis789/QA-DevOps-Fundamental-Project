from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField

class AddUser(FlaskForm):
    custName = StringField("Full Name")
    email = StringField("Email")
    birthDate = DateField("Date of Birth")
    number = IntegerField("Phone Number")
    submit = SubmitField("Register")

class CustomerLogin(FlaskForm):
    custName = StringField("Full Name")
    yourId = StringField("Login-ID")
    submit = SubmitField("Log in")

class AdminLogin(FlaskForm):
    adminName = StringField("Full Name")
    adminId = StringField("Login-ID")
    submit = SubmitField("Log in")
