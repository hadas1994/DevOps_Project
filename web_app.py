# The web interface will return the username of a given user id stored inside users table

import pymysql
from flask import Flask, request
app = Flask(__name__)
users = {}


@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                           db='nUaXW57hSo')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nUaXW57hSo.users;")
    for row in cursor:
        id = row[0]
        if str(id) == user_id:
            cursor.close()
            conn.close()
            return "<H1 id='user'>" + row[1] + "</H1>"
    else:
        return "<H1 id='error'>" + "no such user:" + user_id + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)
