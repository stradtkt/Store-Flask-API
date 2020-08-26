from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
items = []
@app.route('/')
def home():
    return render_template('index.html')

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'Could not find item'}, 404

    def post(self, name):
        item =  {'name': name, 'price': 19.99}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')


if __name__ == "__main__":
    app.run(port=5000, debug=True)