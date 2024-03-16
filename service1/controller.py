import json
from flask_restful import Resource

class Service1(Resource):
    def __init__(self):
        self.datafile = 'data/data.json'
        try:
            with open(self.datafile) as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def get(self, id=None):
        if id:
            for item in self.data:
                if item["id"] == id:
                    return item
            return {"message": "Item not found"}, 404
        return self.data

    def post(self):
        new_item = {"id": len(self.data) + 1, "name": "Item " + str(len(self.data) + 1)}
        self.data.append(new_item)
        try:
            with open(self.datafile, 'w') as f:
                json.dump(self.data, f)
        except IOError:
            return {"message": "Error writing to file"}, 500
        return new_item, 201