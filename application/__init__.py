from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('secretkey')

db = SQLAlchemy(app)
