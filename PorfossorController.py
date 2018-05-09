from flask_restful import Resource
from BaseModel import profssor


class list(Resource):
    def get(self):
        profssors = profssor.select()
        ls = [dict(
             id= c.id,
             firstname = c.firstname,
             lastname = c.lastname,
             father=c.father,
             sex= c.sex,
             national_code= c.national_code,
             birthday=c.birthday,
             location_brith=c.location_brith,
             password=c.password,
             phone=c.phone,
             mobile=c.mobile,
             address=c.address,
             img=c.img,
        )for c in profssors
        ]
        return dict(profssors= ls)
