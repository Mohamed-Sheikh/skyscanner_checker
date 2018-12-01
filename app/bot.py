from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

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

def insert_keys(browser, key):
    actions = ActionChains(browser)
    actions.send_keys(key)
    actions.perform()
    time.sleep(2)

def insert_by_name(name, val):
    """Identifies html components and sends value"""
    try:
        name = driver.find_element_by_name(name)
    except Exception as e:
        raise(e)
    else:
        name.send_keys(val)


def insert_by_class_name(name, val=None, send=True):
     if send:
         name = driver.find_element_by_class_name(name)
         name.send_keys(val)
     else:
         driver.find_element_by_class_name(name).click()

def insert_by_xpath(path, val):
     name = driver.find_element_by_xpath(path).click()
     name.send_keys(val)

def search_flights(data):
    for k, v in data.items():
        insert_by_name(k, v)

def search_location(_from, to):
    insert_by_name('origin-fsc-search', _from)
    insert_keys(driver, Keys.TAB)
    insert_by_name('destination-fsc-search', to)
    insert_keys(driver, Keys.TAB)

def search_dates(from_date, to_date):

    driver.find_element_by_id("depart-fsc-datepicker-button").click()
    time.sleep(0.5)
    driver.find_element_by_id("depart-calendar__bpk_calendar_nav_select").click()
    time.sleep(0.5)
    pyautogui.typewrite("Ja", 0.25)
    pyautogui.keyDown("enter")
    insert_keys(driver, Keys.ENTER)
    time.sleep(0.5)

    driver.find_element_by_xpath(f'//button[@*="{from_date}"]').click()
    driver.find_element_by_id("return-fsc-datepicker-button").click()
    time.sleep(0.5)


    driver.find_element_by_id("return-calendar__bpk_calendar_nav_select").click()
    pyautogui.typewrite("Ja", 0.25)
    driver.find_element_by_xpath(f'//button[@*="{to_date}"]').click()

def ticket_type(_type="Economy"):
    if _type == "Premium Economy":
        pyautogui.typewrite("pr", 0.25)
        pyautogui.keyDown("enter")
    elif _type == "Business":
        pyautogui.typewrite("bu", 0.25)
        pyautogui.keyDown("enter")
    elif _type == "First":
        pyautogui.typewrite("fi", 0.25)
        pyautogui.keyDown("enter")

    time.sleep(0.25)
    driver.find_element_by_id("fsc-class-travellers-trigger-1PZXn").click()
    time.sleep(0.25)
    driver.find_element_by_xpath('//button[contains(text(), "Done")]').click()
    driver.find_element_by_xpath('//button[@aria-label="Search flights"]').click()
if __name__ == '__main__':
    search_location('London', 'Toronto')
    search_dates('Saturday, 12 January 2019', 'Friday, 18 January 2019')
    ticket_type()
