from flask import Flask, jsonify, request

app = Flask(__name__)

""" Initial data in my to do list """
items = [
    {'id': 1, 'name': "Item 1", 'description': 'This is the item 1'},
    {'id': 2, 'name': "Item 2", 'description': 'This is the item 2'},
]


@app.route('/')
def home():
    return 'Welcome to the sample To DO List App'


""" GET: Retrieve all the items """


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


""" GET: Retrieve specific item by id """


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'Error': 'Item not found'})
    return jsonify(item)


""" POST: Create a new task """


@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or  'name' not in request.json:
        return jsonify({'Error': 'Item not found'})
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json('name'),
        'description': request.json('description')
    }
    items.append(new_item)
    return jsonify(new_item)


""" PUT: Update an existing item """


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'Error': 'Item not found'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)


""" DELETE: Delete an item """


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': 'Item deleted'})


if __name__ == "__main__":
    app.run(debug=True)
