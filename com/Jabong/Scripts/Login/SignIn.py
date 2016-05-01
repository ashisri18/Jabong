from com.Jabong.PageRepo.Home.HomePage import *

class SignInJabong(SignIn):

    signIn = SignIn()
    testCaseId = 'SignIn_01'
    sheetName = 'SignInData'

    # def __init__(cls):
    #     cls.testCaseId = 'SignIn_01'
    #     cls.sheetName = 'SignInData'

    def test_SignInJabong(cls):
        cls.signIn.clickSignInLink()
        cls.signIn.enterMailId(cls.testCaseId, cls.sheetName)
        cls.signIn.enterPassword(cls.testCaseId, cls.sheetName)
        cls.signIn.clickSignInBtn()
