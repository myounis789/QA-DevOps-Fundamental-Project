from flask import Flask, render_template, request, redirect
from application import app, db
from application.forms import AddUser, CustomerLogin
from application.models import Users, Bookings
# ----------------------------------------------
import string, random

def generateKey(size=8, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
# ----------------------------------------------

@app.route("/")
def homePage():
    return render_template("homepage.html")

@app.route("/register")
def register():
    form = AddUser()
    return render_template("registration.html", form=form)

@app.route("/customer")
def customerLogin():
    form = CustomerLogin()
    return render_template("customerLogin.html", form=form)

@app.route("/login", methods=["POST"])
def login():
    form = CustomerLogin()
    currentName = form.custName.data
    currentId = form.yourId.data
    data = Users.query.all()
    # Verifying login credentials
    for record in data:
        # Debugging--------
        # print(record.Name)
        # print(record.LoginId," - ", currentId)
        # Debugging--------
        if record.Name == currentName and record.LoginId == currentId:
            return redirect(f"/userHome/{currentId}")
    return '<h1 style="color:red;"> ERROR: Login credentials do not match! Please try again </h1>'

@app.route("/userHome/<currentId>")
def userHome(currentId):
    data=Users.query.filter_by(LoginId=currentId).first()
    return render_template("userLanding.html", user=data)

@app.route("/saveCust", methods=["GET","POST"])
def saveCust():
    form = AddUser()
    if request.method == 'POST':
        name = form.custName.data
        userType = 'customer'
        email = form.email.data
        dob = form.birthDate.data
        phone = form.number.data
        loginid = generateKey()

        newCust = Users(Name = name, UserType = userType, Email = email, DoB = dob ,Phone = phone, LoginId=loginid)
        db.session.add(newCust)
        db.session.commit()
        return render_template("displayId.html", customer=newCust)
    return render_template("registration.html")

@app.route("/userHome/newBooking/<currentId>")
def newBooking(currentId):
    data=Users.query.filter_by(LoginId=currentId).first()
    return render_template("newBooking.html", user=data)
