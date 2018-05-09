from flask_restful import Resource
from flask import  g
from Auth import auth


class Login (Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(600)
        print(g.user)
        return {'token': token.decode('ascii'), 'duration': 600, 'lastname': g.user.lastname}

    @auth.login_required
    def post(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600, 'lastname': g.user.lastname}

