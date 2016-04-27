import unittest
import time
from selenium import webdriver

class Initilization(unittest.TestCase):

    driver = webdriver.Firefox()

    def setUp(cls):
        cls.driver.get("http://www.jabong.com/")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        time.sleep(5)

#    def tearDown(cls):
#        cls.driver.close()

