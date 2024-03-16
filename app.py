from flask import Flask
from flask_restful import Api
from service1.controller import Service1
# from service2.controller import Controller2

app = Flask(__name__)
api = Api(app)

api.add_resource(Service1, '/automation/service1', '/automation/service1/<int:id>')

if __name__ == "__main__":
    app.run(debug=True, host='', port=5000)