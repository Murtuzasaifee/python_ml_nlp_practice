from flask import Flask, request, jsonify

app = Flask(__name__)

## Initial data in TODO List
items = [
    {
        'id': 1,
        'name': 'item1',
        'description': 'item1 description'
    },
    {
        'id': 2,
        'name': 'item2',
        'description': 'item2 description'
    }
]

@app.route('/')
def home():
    return 'Welcome to TODO List'

## Get all items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## Get specific Item
@app.route('/items/<int:item_id>')
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    else:
        return jsonify(item)
    
## Add new item
@app.route('/items',methods=['POST'])
def add_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Please provide name"})
    
    new_item = {
        'id': items[-1]['id']+1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

## Update item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    
    return jsonify(item)

## Delete item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id']!=item_id]
    return jsonify({"result":"Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)