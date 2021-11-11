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