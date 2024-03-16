import json
from flask import request
from flask_restful import Resource
from io import BytesIO
from users.validations import validate_file

class Users(Resource):
    def __init__(self):
        self.datafile = 'data/data.json'
        try:
            with open(self.datafile) as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def get(self, id=None):
        if id is None:
            return self.data
        for item in self.data:
            if item["id"] == id:
                return item
        return {"message": "Item not found"}, 404

    def post(self):
        if 'file' in request.files:
            # Handle CSV file
            file = request.files['file']
            is_valid, message = validate_file(BytesIO(file.read()))
            if not is_valid:
                return {"message": message}, 400
            return {"message": "File is valid"}, 200
        
        else:
            # Handle user creation
            try:
                new_item = {"id": len(self.data) + 1, "name": "Item " + str(len(self.data) + 1)}
                self.data.append(new_item)
            except Exception as e:
                return {"message": "Error creating item: " + str(e)}, 500
            try:
                with open(self.datafile, 'w') as f:
                    json.dump(self.data, f)
            except IOError:
                return {"message": "Error writing to file"}, 500
            return new_item, 201

    def delete(self, id):
        if id is None:
            return {"message": "No ID provided"}, 400

        for i, item in enumerate(self.data):
            if item["id"] == id:
                del self.data[i]
                try:
                    with open(self.datafile, 'w') as f:
                        json.dump(self.data, f)
                except IOError:
                    return {"message": "Error writing to file"}, 500
                return {"message": "Item deleted"}, 200