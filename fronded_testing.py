# for web interface testing

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:/Users/zhada/Downloads/chromedriver_win32/chromedriver.exe"))
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5001/users/get_user_data/7")
x = driver.find_element(by=By.ID, value="user")
print(x.text)
driver.quit()
