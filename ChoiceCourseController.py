from flask_restful import Resource

from Auth import auth2
from BaseModel import ChoiceCourse


class list(Resource):
    def get(self):
        chcourses = ChoiceCourse.select()
        ls = [dict(
            id =c.id,
            Student_student_number =c.Student_student_number,
            status =c.status,
            score =c.score,
            semeter =c.semeter,
            Group_Course_code_course =c.Group_Course_code_course,
            status_pay =c.status_pay,
        ) for c in chcourses
              ]
        return dict(ChoiceCourse=ls)


class Delete(Resource):
    @auth2.login_required
    def delete(self, course_id):
        try:
            course = ChoiceCourse.get(id=course_id)
        except ChoiceCourse.DoesNotExist:
            return None, 404
        course.delete_instance()
        return dict(status=True, id=course_id), 200
