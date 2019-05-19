from flask import Flask, render_template
from flask_restful import Api

from Users import User, Users

app = Flask(__name__)
api = Api(app)

users = {
    "Flori": {"name": "Flori", "age": 24},
    "Benno": {"name": "Benno", "age": 24},
    "Andy": {"name": "Andy", "age": 24},
    "Michael": {"name": "Michael", "age": 24},
}

api.add_resource(User, "/user/<string:name>")
api.add_resource(Users, "/users/")


@app.route('/')
def hello_world(name: str = None):
    return render_template('home.html', name=name)


@app.route('/<str:name>')
def hello_world(name: str = None):
    return render_template('home.html', name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return str(post_id)


@app.route('/user2/<str:name>')
def show_user(name: str) -> str:
    return f"Username: {name}"



if __name__ == '__main__':
    app.run()
