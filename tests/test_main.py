from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Users, Bookings
from application.forms import AddUser, CustomerLogin, AddBooking, AdminLogin, UpdateBooking, UpdateAccount 
import application.routes

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
        sampleUser = Users(name='John Smith', dept='IT', subject='Python', salary=20000, marks=300)
        sampleBooking = Bookings
        db.session.add(sample)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_emps_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)