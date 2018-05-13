from flask import Flask
from flask_restful import Api

import ChoiceCourseController
import CourseController
import LoginController
import  PorfossorController

app = Flask(__name__)
api = Api(app)



api.add_resource(CourseController.list , '/courses', endpoint='courses')
api.add_resource(CourseController.Delete , '/delete/<int:course_id>', endpoint='delete')
api.add_resource(ChoiceCourseController.Delete , '/choicedelete/<int:course_id>', endpoint='choicedelete')
api.add_resource(CourseController.updateCurse , '/updateCurse', endpoint=' updateCurse')
api.add_resource(CourseController.insertCurse , '/insert', endpoint='insert')
api.add_resource(PorfossorController.list , '/profossors' , endpoint='profossors')
api.add_resource(LoginController.Login, '/login' , endpoint='Login')
api.add_resource(ChoiceCourseController.list, '/chcourse' , endpoint='ChoiceCourses')



if __name__ == '__main__':
    app.run('127.0.0.1',5000,True)



