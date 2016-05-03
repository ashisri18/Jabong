import unittest
import time
from selenium import webdriver
import Config
import logging

class Initilization(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,filename = 'D:\CBT_Automation\Python\Workspace_Python\Jabong\Report\Logs\example.log')

    if Config.Browser.lower() == 'Firefox'.lower():
            driver = webdriver.Firefox()
            logging.info('Firefox browser launched.')

    elif Config.Browser.lower() == 'Chrome'.lower():
            chrimeDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\chromedriver.exe"
            driver = webdriver.Chrome(chrimeDriver)
            logging.info('Chrome browser launched.')
    else:
            ieDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\IEDriverServer.exe"
            driver = webdriver.Ie



    def setUp(cls):
        #driver = cls.driver
        logging.info('Inside Setup method')
        cls.driver.get(Config.URL)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        time.sleep(3)

    # def tearDown(cls):
    #     logging.info("Inside TearDown Method.")
    #     cls.driver.close()

if __name__ == "__main__":
    unittest.main()