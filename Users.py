from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app import users


class User(Resource):
    def get(self, name):
        try:
            user = users[name]
            return user, 200
        except KeyError as e:
            return f"User not found: {e}", 404

    def post(self, name):
        if name in users:
            return f"User {name} already exists", 400

        parser = RequestParser()
        parser.add_argument("age")
        args = parser.parse_args()
        user = {"name": name, "age": args.age}
        users[name] = user
        return user, 201

    def put(self, name):
        parser = RequestParser()
        parser.add_argument("age")
        args = parser.parse_args()

        if name in users:
            user = users[name]
            user["age"] = args["age"]
            return user, 200

        user = {"name": name, "age": args.age}
        users[name] = user
        return user, 201

    def delete(self, name):
        try:
            del users[name]
            return f"User {name} is deleted", 200
        except KeyError:
            return f"User {name} not found", 404


class Users(Resource):
    def get(self):
        return users, 200