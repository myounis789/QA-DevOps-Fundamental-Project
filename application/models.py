from application import db

class Users(db.Model):
    UserId = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.CHAR(20))
    UserType = db.Column(db.CHAR(10))
    Email = db.Column(db.String(50), unique=True)
    DoB = db.Column(db.Date)
    Phone = db.Column(db.String(15), unique=True)
    LoginId = db.Column(db.String(10), unique=True)
    Bookings = db.relationship("bookings", backref="user")

class Bookings(db.Model):
    bookingId = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(50))
    specialRequest = db.Column(db.String(50))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    status = db.column(db.String(15))
    uid = db.column(db.Integer, db.ForeignKey(Users.UserId))
    
