from application import db
import application.models

db.drop_all()
db.create_all()