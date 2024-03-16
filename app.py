from flask import Flask
from flask_restful import Api
from users.controller import Users
from hotels.controller import Hotels

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/automation/users', '/automation/users/<int:id>')
api.add_resource(Hotels, '/automation/hotels', '/automation/hotels/<int:id>')

if __name__ == "__main__":
    app.run(debug=True, host='', port=5000)