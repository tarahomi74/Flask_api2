from flask import request
from flask_restful import Resource
from BaseModel import Curse


class list(Resource):
    def get(self):
        courses = Curse.select()
        ls = [dict(
            id=c.id,
            list_prerequisite=c.list_prerequisite,
            name=c.name,
            price=c.price,
            presentation=c.presentation,
            status_prerequisite=c.status_prerequisite,
            type=c.type,
            unit_number=c.unit_number,
        ) for c in courses
              ]
        return dict(courses=ls)


class insertCurse(Resource):
    def post(self):
        request_json = request.get_json()
        curse = Curse()
        # Curse. id = request_json[' id']
        curse.list_prerequisit = request_json['list_prerequisit']
        curse.name = request_json['name']
        curse.price = request_json['price']
        curse.presentation = request_json['presentation']
        curse.status_prerequisite = request_json['status_prerequisite']
        curse.type = request_json['type']
        curse.unit_number = request_json['unit_number']

        return dict(
            status=curse.save()
        )
