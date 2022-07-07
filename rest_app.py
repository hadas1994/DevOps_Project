# The REST API will read and write data using a MySQL table called users

from flask import Flask, request
from db_connector import insert_user, get_data, delete_data, put_data
app = Flask(__name__)
users = {}


@app.route('/user/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            return {'status': 'OK', 'user_id': user_id, 'user_name': get_data(user_id)[1]}, 200  # status code
        except:
            return {'status': 'error', "reason": "no such id"}, 500  # status code

    elif request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        try:
            insert_user(user_id, user_name)
            return {'user id': user_id, 'user_added': user_name, 'status': 'ok'}, 200  # status code
        except:
            return {"status": "error", "reason": "id already exists"}, 500  # status code

    elif request.method == 'DELETE':
        try:
            delete_data(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except:
            return {"status": "error", "reason": "no such id"}, 500  # status code

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        try:
            put_data(user_id, user_name)
            return {'user id': user_id, 'user_updated': user_name, 'status': 'ok'}, 200  # status code
        except:
            return {"status": "error", "reason": "no such id"}, 500  # status code


app.run(host='127.0.0.1', debug=True, port=5000)