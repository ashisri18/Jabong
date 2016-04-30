from com.Jabong.GenericLib.Initilization import *
import time
from com.Jabong.GenericLib.ExcelSheet import *

class SignIn(Initilization, ExcelSheet):

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
