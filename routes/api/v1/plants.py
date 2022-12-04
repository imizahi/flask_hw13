from app import api, db
from flask_restful import Resource
from flask import request
from models.models import Plant as PlantModel
from models.models import Employee as EmployeeModel

class PlantResource(Resource):

    def get(self):
        filter = request.args
        query = PlantModel.query
        if len(filter) < 1:
            plants = query.all()
        else:
            for key in filter.keys():
                print(key)
                plants = query.filter(getattr(PlantModel, key) == filter.get(key))

        plant_data = []
        for plant in plants:
            plant_data.append(plant.serialize())
        return plant_data

    def post(self):
        data = request.json
        plant = PlantModel(
            id=data.get("id"),
            title=data.get("title"),
            location=data.get("location"),
        )
        db.session.add(plant)
        db.session.commit()
        return plant.serialize()

class SinglePlantResource(Resource):
    def get(self, id):
        plant = PlantModel.query.get(id)
        return plant.serialize()

    def put(self, id):
        data = request.json
        plant = PlantModel.query.get(id)
        plant.id = data.get("id", plant.id)
        plant.title = data.get("title", plant.title)
        plant.location = data.get("location", plant.location)
        db.session.add(plant)
        db.session.commit()
        return plant.serialize()
    
    def delete(self, id):
        plant = PlantModel.query.get(id)
        employee = EmployeeModel.query.all()
        for emp in employee:
            if emp.plant_id == plant.id:
                return {"need to delete employee": employee.serialize()}
        db.session.delete(plant)
        db.session.commit()
        return plant.serialize()

api.add_resource(PlantResource, "/api/v1/plants")
api.add_resource(SinglePlantResource, "/api/v1/plants/<int:id>")
