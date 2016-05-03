from com.Jabong.GenericLib.Initilization import *
import time
from com.Jabong.GenericLib.ExcelSheet import *
import logging
import sys, traceback

class SignIn(Initilization, ExcelSheet):
#    logging.basicConfig(level=logging.INFO, filename='D:\CBT_Automation\Python\Workspace_Python\Jabong\Report\Logs\example.log')
    driver = Initilization.driver
    excelSheet = ExcelSheet()

    def clickSignInLink(cls):
        signInLink = cls.driver.find_element_by_xpath("//a[text()='Sign In']")
        signInLink.click()
        time.sleep(2)

    def enterMailId(cls, testCaseId, sheetName):
        data = cls.readData(testCaseId, sheetName)
        print(data)
        emailIdTxtBox = cls.driver.find_element_by_id("login-email")
        emailIdTxtBox.send_keys(data[1])

    def enterPassword(cls, testCaseId, sheetName):
        data = cls.readData(testCaseId, sheetName)
        passwordTxtBox = cls.driver.find_element_by_name("password")
        passwordTxtBox.send_keys(data[2])

    def clickSignInBtn(cls):
        signInBtn = cls.driver.find_element_by_xpath("//button[text()='SIGN IN']")
        signInBtn.click()
        time.sleep(5)

    def verifyErrorMsg(cls):
        #try:
            expectedMsg = 'Incorrect username or password.'
            actualMsg = cls.driver.find_element_by_xpath("//span[contains(text(),'Incorrect username or password.')]").text
            cls.assertEqual(expectedMsg, actualMsg, 'Error message is not verified.')
            logging.info('Error message verified.')
        # except:
        #     logging.error('Error msg not verified, so Assertion failed.')
        #     cls.driver.save_screenshot('D:\CBT_Automation\Python\Workspace_Python\Jabong\Report\Screenshots\screenshot1.png')
        #     traceback.print_exception("there is some exception.")

    def clickCancelBtn(cls):
        cancelBtn = cls.driver.find_element_by_class_name("close")
        cancelBtn.click()
        time.sleep(2)
