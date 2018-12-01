from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import os
import logging
import user_input

options = Options()
options = webdriver.ChromeOptions()

options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox"); # Bypass OS security model
driver_path = "{}/app/lib/chromedriver".format(os.getcwd())
URL = "https://www.skyscanner.net"
URL = "http:127.0.0.1:5000/"
driver = webdriver.Chrome(driver_path, options=options)
driver.get(URL)

flight_data = user_input.flight_data

def insert_by_name(name, val):
    """Identifies html components and sends value"""
    try:
        name = driver.find_element_by_name(name)
    except Exception as e:
        raise(e)
    else:
        name.send_keys(val)

def search_flights(data):
    for k, v in data.items():
        insert_by_name(k, v)

if __name__ == '__main__':
    search_flights(flight_data)
