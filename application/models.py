from application import db

class Users(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.CHAR(20))
    UserType = db.Column(db.CHAR(10))
    Email = db.Column(db.String(50), unique=True)
    DoB = db.Column(db.Date)
    Phone = db.Column(db.String(15), unique=True)
    LoginId = db.Column(db.String(10), unique=True)
