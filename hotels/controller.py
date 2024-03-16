import json
from flask_restful import Resource

class Hotels(Resource):
    def __init__(self):
        self.datafile = 'data/hotels.json'
        try:
            with open(self.datafile) as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def get(self, id=None):
        if id is None:
            return self.data
        for hotel in self.data:
            if hotel["id"] == id:
                return hotel
        return {"message": "Hotel not found"}, 404

    def post(self, hotel):
        try:
            new_hotel = {"id": len(self.data) + 1, "name": hotel['name'], "location": hotel['location'], "rating": hotel['rating']}
            self.data.append(new_hotel)
        except Exception as e:
            return {"message": "Error creating hotel: " + str(e)}, 500
        try:
            with open(self.datafile, 'w') as f:
                json.dump(self.data, f)
        except IOError:
            return {"message": "Error writing to file"}, 500
        return new_hotel, 201

    def delete(self, id):
        if id is None:
            return {"message": "No ID provided"}, 400

        for i, hotel in enumerate(self.data):
            if hotel["id"] == id:
                del self.data[i]
                try:
                    with open(self.datafile, 'w') as f:
                        json.dump(self.data, f)
                except IOError:
                    return {"message": "Error writing to file"}, 500
                return {"message": "Hotel deleted"}, 200
        return {"message": "Hotel not found"}, 404