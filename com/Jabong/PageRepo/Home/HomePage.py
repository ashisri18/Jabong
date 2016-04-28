from com.Jabong.GenericLib.Initilization import *
import time

class SignIn(Initilization):

    driver = Initilization.driver

    def clickSignInLink(cls):
        signInLink = cls.driver.find_element_by_xpath("//a[text()='Sign In']")
        signInLink.click()
        time.sleep(2)

    def enterMailId(cls):
        emailIdTxtBox = cls.driver.find_element_by_id("login-email")
        emailIdTxtBox.send_keys('ashi.sri.18@gmail.com')

    def enterPassword(cls):
        passwordTxtBox = cls.driver.find_element_by_name("password")
        passwordTxtBox.send_keys("Ashish Srivastava")

    def clickSignInBtn(cls):
        signInBtn = cls.driver.find_element_by_xpath("//button[text()='SIGN IN']")
        signInBtn.click()
        time.sleep(5)
