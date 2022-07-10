# for REST API and Database testing

import requests

# POST – will accept user_name parameter inside the JSON payload.
res = requests.post('http://127.0.0.1:5000/user/2', json={"user_name": "Jack"})
if res.ok:
    print(res.json())
else:
    print("test failed")

# GET – returns the username stored in the database for a given user id.
res = requests.get('http://127.0.0.1:5000/user/2')
if res.ok:
    print(res.json())
else:
    print("test failed")

# # PUT – will modify existing username (in the database).
# res = requests.put('http://127.0.0.1:5000/user/1', json={"user_name": "george"})
# if res.ok:
#     print(res.json())
# else:
#     print("test failed")
#
# # DELETE – will delete existing user (from database).
# res = requests.delete('http://127.0.0.1:5000/user/1')
# if res.ok:
#     print(res.json())
# else:
#     print("test failed")
