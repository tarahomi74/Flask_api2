from flask import Flask
from flask_restful import Api
import CourseController
import LoginController
import  PorfossorController

app = Flask(__name__)
api = Api(app)



api.add_resource(CourseController.list , '/courses', endpoint='courses')
api.add_resource(CourseController.insertCurse , '/insert', endpoint='insert')
api.add_resource(PorfossorController.list , '/profossors' , endpoint='profossors')
api.add_resource(LoginController.Login, '/login' , endpoint='Login')


if __name__ == '__main__':
    app.run('127.0.0.1',5000,True)



