from flask import Flask, render_template, request, redirect
from application import app, db
from application.forms import AddEmp, EditEmp
from application.models import Employees


@app.route("/")
def homePage():
    data = Employees.query.all()
    return render_template("homepage.html", records=data)