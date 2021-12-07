
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
import time
from selenium.webdriver.common.by import By
import urllib
import re
import yaml
import os.path

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
with open(BASE_DIR + "/secrets.yaml") as file:
	yaml_dict = yaml.safe_load(file)
	username, password, url = yaml_dict["username"], yaml_dict["password"], yaml_dict["url"]

CHROME_DRIVER = "/usr/bin/chromedriver"

options = Options()
options.add_argument("--headless")

chrome_service = fs.Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(url)

driver.implicitly_wait(5)

username_form = driver.find_element(By.NAME, "user")
password_form = driver.find_element(By.NAME, "pass")

username_form.send_keys(username)
password_form.send_keys(password)

driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "ログイン").click()

driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "再起動").click()

driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "再起動").click()

driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "OK").click()

time.sleep(3)

driver.quit()
