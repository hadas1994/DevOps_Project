# for Web interface, REST API and Database testing

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

res = requests.post('http://127.0.0.1:5000/user/6', json={"user_name": "test1"})
if res.ok:
    print(res.json())
else:
    print("test failed")

res = requests.get('http://127.0.0.1:5000/user/6')
if res.ok:
    print(res.json())
else:
    print("test failed")

driver = webdriver.Chrome(service=Service("C:/Users/zhada/Downloads/chromedriver_win32/chromedriver.exe"))
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5001/users/get_user_data/6")
x = driver.find_element(by=By.ID, value="user")
print(x.text)
driver.quit()
