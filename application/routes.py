from flask import Flask, render_template, request, redirect
from application import app, db
from application.forms import AddUser, CustomerLogin, AddBooking, UpdateBooking
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
    data2=Bookings.query.filter_by(uid=data.UserId).all()
    return render_template("userLanding.html", user=data, bookings=data2)

@app.route("/userHome/managebookings/<currentId>")
def manageBookings(currentId):
    data=Users.query.filter_by(LoginId=currentId).first()
    data2=Bookings.query.filter_by(uid=data.UserId).all()
    return render_template("manageBookings.html", user=data, bookings=data2)

# ---------------------Customer Actions-------------------------------------

# -----------------------View Booking---------------------------------------
@app.route("/userHome/viewBooking/<currentId>/int:<bookingId>")
def viewBooking(currentId, bookingId):
    data=Users.query.filter_by(LoginId=currentId).first()
    data2=Bookings.query.filter_by(bookingId=bookingId).first()
    return render_template("viewBooking.html", user=data, bookings=data2)



# -----------------------Edit Booking---------------------------------------
@app.route("/userHome/updateBooking/<currentId>/int:<bookingId>", methods = ["GET", "POST"])
def editBooking(currentId, bookingId):
    form = UpdateBooking()
    currentBooking = Bookings.query.filter_by(bookingId=bookingId).first()
    currentUser=Users.query.filter_by(LoginId=currentId).first()
    if request.method == 'POST':
        currentBooking.description = form.newDescription.data
        currentBooking.adult = form.newAdults.data
        currentBooking.children = form.newChildren.data
        currentBooking.guests = form.newAdults.data + form.newChildren.data
        currentBooking.specialRequest = ', '.join(form.newRequests.data)
        db.session.commit()
        return redirect(f"/userHome/{currentId}")

    return render_template('updateBooking.html', form=form, booking=currentBooking, user=currentUser)

# -----------------------Delete Booking-------------------------------------
@app.route("/userHome/deleteBooking/<currentId>/int:<bookingId>")
def deleteBooking(currentId, bookingId):
    currentBooking = Bookings.query.filter_by(bookingId=bookingId).first()
    db.session.delete(currentBooking)
    db.session.commit()
    return redirect(f"/userHome/{currentId}")

# ---------------------Customer Actions-------------------------------------

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
    form=AddBooking()
    data=Users.query.filter_by(LoginId=currentId).first()
    return render_template("newBooking.html", user=data, form=form)

@app.route("/userHome/addBooking/<currentId>", methods=["POST"])
def addBooking(currentId):
    form=AddBooking()

    desc = form.description.data
    spRequest = ', '.join(form.requests.data)
    bookingDate = form.date.data
    bookingTime = form.time.data
    custAdult = form.adults.data
    custChild = form.children.data
    guests = custAdult + custChild
    bookingStatus = 'Upcoming'
    currentUser = Users.query.filter_by(LoginId=currentId).first()
    newBookings = Bookings(description = desc, specialRequest = spRequest, date = bookingDate, time = bookingTime, adult = custAdult, children = custChild, guests = guests, status = bookingStatus, uid=currentUser.UserId)
    db.session.add(newBookings)
    db.session.commit()

    return redirect(f"/userHome/{currentId}")