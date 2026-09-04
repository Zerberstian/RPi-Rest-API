from rest_api import db, app

with app.app_context():
    db.create_all()