from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import os

options = Options()
options = webdriver.ChromeOptions()

options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox"); # Bypass OS security model
driver_path = "{}/chromedriver".format(os.getcwd())
URL = "https://www.skyscanner.net"
#URL = "http:127.0.0.1:5000/"
print("path is : {}".format(driver_path))
driver = webdriver.Chrome(driver_path, options=options)
driver.get(URL)

dest_search = driver.find_element_by_name('from_dest')
driver.send_keys('loooooool')

