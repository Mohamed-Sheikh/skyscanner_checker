from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
import logging

import user_input

options = Options()
options = webdriver.ChromeOptions()

options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox"); # Bypass OS security model
driver_path = "{}/app/lib/chromedriver".format(os.getcwd())
URL = "https://www.skyscanner.net"
#URL = "http:127.0.0.1:5000/"
driver = webdriver.Chrome(driver_path, options=options)
driver.get(URL)

flight_data = user_input.flight_data

def tab_keys(browser):
    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB)
    actions.perform()

def insert_by_name(name, val):
    """Identifies html components and sends value"""
    try:
        name = driver.find_element_by_name(name)
    except Exception as e:
        raise(e)
    else:
        name.send_keys(val)


def insert_by_class_name(name, val):
     name = driver.find_element_by_class_name(name)
     name.send_keys(val)

def insert_by_xpath(path, val):
     name = driver.find_element_by_xpath(path).click()
     name.send_keys(val)

def search_flights(data):
    for k, v in data.items():
        insert_by_name(k, v)

if __name__ == '__main__':
    #search_flights(flight_data)
    insert_by_name('origin-fsc-search', 'London')
    tab_keys(driver)
    insert_by_name('destination-fsc-search', 'Toronto')
    tab_keys(driver)
    insert_by_xpath("//*select[@name='months']/option[2]", "09/11/2019")
