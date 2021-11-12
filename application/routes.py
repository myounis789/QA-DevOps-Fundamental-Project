from flask import Flask, render_template, request, redirect
from application import app, db
from application.forms import AddUser, CustomerLogin

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

@app.route("/saveCust", methods=["GET","POST"])
def saveCust():
    form = CustomerLogin()
    if request.method == 'POST':
        name = form.custName.data
        userType = 'customer'
        email = form.email.data
        dob = form.birthDate.data
        phone = form.number.data
        loginid = "DKCWeb12"

        newCust = Users (Name = Name, UserType= = userType, Email = email, DoB = dob ,Phone = phone, LoginId=loginid)
        db.session.add(newCust)
        db.session.commit()
        return redirect("/")
    return render_template("displayId.html", customer=form)