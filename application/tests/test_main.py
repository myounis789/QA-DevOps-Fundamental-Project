from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Users, Bookings
from application.forms import AddUser, CustomerLogin, AddBooking, AdminLogin, UpdateBooking, UpdateAccount 
import application.routes
import datetime

# -----------------23 app routes to be tested------------------ 
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        bookingdate=datetime.date(2000, 10, 11)
        sampleUser = Users(Name='John Smith', UserType='customer', Email='JohnSmith47@gmail.com', DoB=bookingdate, Phone='7432683755', LoginId='qw1tbU57')
        sampleBooking = Bookings(description='My party', specialRequest='Window Seat, Power Socket', date='2021-11-29', time='18:00:00', adult=5, guests=7, children=2, status='Upcoming')
        db.session.add(sampleUser, sampleBooking)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('homePage'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register Here!', response.data)

    def test_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Restaurant Reserver', response.data)

    def test_customerLogin(self):
        response = self.client.get(url_for('customerLogin'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Customer Login Page', response.data)

    def test_login(self):
        response = self.client.post(url_for('login'),
        data='Mohammed Younis', 
        follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ERROR', response.data)

