from com.Jabong.PageRepo.Home.HomePage import *
from com.Jabong.PageRepo.Men.Clothing import *
import logging

class SignInJabong(SignIn, ClothingCategory):

    signIn = SignIn()
    testCaseId = 'SignIn_01'
    sheetName = 'SignInData'
    cc = ClothingCategory()
    sc = SportsCategory()

    # def __init__(cls):
    #     cls.testCaseId = 'SignIn_01'
    #     cls.sheetName = 'SignInData'

    def test_SignInJabong(cls):
        try:
            assert "Online Shopping India:" in cls.driver.title
            logging.info("Title verified.")
            cls.signIn.clickSignInLink()
            cls.signIn.enterMailId(cls.testCaseId, cls.sheetName)
            cls.signIn.enterPassword(cls.testCaseId, cls.sheetName)
            cls.signIn.clickSignInBtn()
            cls.signIn.verifyErrorMsg()
            cls.signIn.clickCancelBtn()
            logging.info("Sign-in Successful.")

        except:
            logging.error('Exception found in method.')
            cls.driver.save_screenshot('D:\CBT_Automation\Python\Workspace_Python\Jabong\Report\Screenshots\screenshot1.png')
            traceback.print_exception("there is some exception.")

    # def test_buyBlazzer(cls):
    #     cls.cc.clickMenBlock()
    #     cls.cc.clickSuitsBlazers_CC()
    #
    # def test_buyJerseys(cls):
    #     cls.sc.clickJerseys_SC()

if __name__ == '__main__':
    unittest.main()