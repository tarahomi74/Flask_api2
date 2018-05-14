from flask_restful import Resource

from Auth import auth2
from BaseModel import Mesal


class list(Resource):
    @auth2.login_required
    def get(self):
        time = Mesal.select()
        ls = [dict(
            id =c.id,
            name=c.name,
            family =c.family,
            number=c.number,
        ) for c in time
              ]
        return dict(Mesal=ls)
