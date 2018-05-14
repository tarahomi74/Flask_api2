from flask_restful import Resource

from Auth import auth2
from BaseModel import TimeCourse


class list(Resource):
    @auth2.login_required
    def get(self):
        timecourses = TimeCourse.select()
        ls = [dict(
            id =c.id,
            days=c.days,
            time =c.time,
            classes=c.classes,
            rotatory =c.rotatory,
            day_rotatory =c.day_rotatory,
        ) for c in timecourses
              ]
        return dict(TimeCourse=ls)
