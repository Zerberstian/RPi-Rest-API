from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
import os

'''
file_path = "../x-api-key.txt"

def read_text_file(file_path):
    """
    Reads a text file and returns its contents as a string.
    Includes error handling for common issues.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

x_api_key = read_text_file(file_path)
print(x_api_key)
'''

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "database.db").replace(chr(92), "/")}'
db = SQLAlchemy(app)
api = Api(app)

class PlantModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plant_name = db.Column(db.String(100), nullable=False)
    waterlevel = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Plant(id={self.id}, plant_name={self.plant_name}, waterlevel={self.waterlevel})'


plant_args = reqparse.RequestParser()
plant_args.add_argument('plant_name', type=str, help='Plant name is required', required=True, location='json')
plant_args.add_argument('waterlevel', type=int, help='Water level is required', required=True, location='json')

plantFields = {
    'id': fields.Integer,
    'plant_name': fields.String,
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
        plant = PlantModel(plant_name=args["plant_name"], waterlevel=args["waterlevel"])
        db.session.add(plant)
        db.session.commit()
        plants = PlantModel.query.all()
        return plants, 201
 
class Plant(Resource):
    @marshal_with(plantFields)
    def get(self, id):
        plant = PlantModel.query.filter_by(id=id).first()

        if not plant: 
            abort(404, message="Plant not found lol")

        return plant
    
    @marshal_with(plantFields)
    def patch(self, id):
        args = plant_args.parse_args()
        plant = PlantModel.query.filter_by(id=id).first()

        if not plant: 
            abort(404, message="Plant not found lol")

        plant.plant_name = args["plant_name"]

        plant.waterlevel = args["waterlevel"]

        db.session.commit()
        return plant, 200
'''   
    @marshal_with(plantFields)
    def delete(self, id):
        plant = PlantModel.query.filter_by(id=id).first()

        if not plant: 
            abort(404, message="Plant not found lol")

        db.session.delete(plant)
        db.session.commit()

        plants = PlantModel.query.all()
        return plants, 204
'''

api.add_resource(Plants, '/api/plants/')
api.add_resource(Plant, '/api/plants/<int:id>')

@app.route('/')
def home():
    return '<h1>Flask REST APi</h1>'

print("======== ROUTES ========")
print(app.url_map)
print("========================")

if __name__ == '__main__':
    app.run(debug=True)
