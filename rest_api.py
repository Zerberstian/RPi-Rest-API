from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db =SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    messwert = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Messwerte(id={self.id}, messwert={self.messwert})'

@app.route('/')
def home():
    return '<h1>Flask REST APi</h1>'

if __name__ == '__main__':
    app.run(debug=True)
