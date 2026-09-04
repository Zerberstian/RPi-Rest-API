from flask import Flask

app = Flask(__name__)

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db =SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messwert = db.Column(db.Integer)

    def __repr__(self):

@app.route('/')
def home():
    return '<h1>Flask REST APi</h1>'

if __name__ == '__main__':
    app.run(debug=True)
'''