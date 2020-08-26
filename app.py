from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'GameInfo',
        'items': [
            {
                'name': 'The Witcher 3',
                'price': 29.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass



if __name__ == "__main__":
    app.run(port=5000, debug=True)