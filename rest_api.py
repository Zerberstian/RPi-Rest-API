from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db =SQLAlchemy(app)
api = Api(app)

class PlantModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plant_name = db.Column(db.String(100), nullable=False)
    waterlevel = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Plant(id={self.id}, plant_name={self.plant_name}, waterlevel={self.waterlevel})'


plant_args = reqparse.RequestParser()
plant_args.add_argument('plant_name', type=str, help='Plant name is required', required=True)
plant_args.add_argument('waterlevel', type=int, help='Water level is required', required=True)

plantFields = {
    'id': fields.Integer,
    'name': fields.String,
    'waterlevel': fields.Integer
} 

class Plants(Resource):
    @marshal_with(plantFields)
    def get(self):
        plants = PlantModel.query.all()
        return plants

    @marshal_with(plantFields)
    def post(self):
        args = plant_args.parse_args()
        plant = PlantModel(id=args["id"], name=args["name"], waterlevel=args["waterlevel"])
        db.session.add(plant)
        db.session.commit()
        plants = PlantModel.query.all()
        return plants, 201

api.add_resource(Plants, '/api/plants/')

@app.route('/')
def home():
    return '<h1>Flask REST APi</h1>'

if __name__ == '__main__':
    app.run(debug=True)