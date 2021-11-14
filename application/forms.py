from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, SelectMultipleField, widgets
from wtforms import DateField, TimeField
from datetime import datetime
# ---------------------------------------------------------------

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# ---------------------------------------------------------------

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

class AddBooking(FlaskForm):
    description = StringField("Description")
    date = DateField("Booking Date")
    time = TimeField("Time")
    adults = IntegerField("No. of Adults")
    children = IntegerField("No. of Children")
    requests = MultiCheckboxField("Special Requests", choices=[('Power Socket'),('Window Seat'),('Wheelchair Access'),('Baby Changing facility'), ('Prayer Room'), ('Private Family room')] )
    submit = SubmitField("Book Now!")