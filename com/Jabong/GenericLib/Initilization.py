import unittest
import time
from selenium import webdriver
import Config
import logging

class Initilization(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    if Config.Browser.lower() == 'Firefox'.lower():
        driver = webdriver.Firefox()

    elif Config.Browser.lower() == 'Chrome'.lower():
        chrimeDriver = "E:\Automation\BackUp\Git\Jabong\chromedriver.exe"
        driver = webdriver.Chrome(chrimeDriver)

    else:
        ieDriver = "E:\Automation\BackUp\Git\Jabong\IEDriverServer.exe"
        driver = webdriver.Ie

    def setUp(cls):

        cls.driver.get(Config.URL)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        time.sleep(3)

#    def tearDown(cls):
#        cls.driver.close()

