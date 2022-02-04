from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}


# @api.route("/hello")
@api.route('/hello', '/world')
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


# @api.route("/<string:todo_id>")
@api.route('/todo/<string:todo_id>', endpoint='todo_ep')
class TodoAPI(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True)
