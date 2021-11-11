from flask import Flask, render_template, request, redirect
from application import app, db


@app.route("/")
def homePage():
    return render_template("homepage.html")

@app.route("/register")
def register():
    return render_template("registration.html")