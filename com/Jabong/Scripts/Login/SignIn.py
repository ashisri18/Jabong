from com.Jabong.PageRepo.Home.HomePage import *

class SignInJabong(SignIn):

    signIn = SignIn()

    def test_SignInJabong(cls):
        cls.signIn.clickSignInLink()
        cls.signIn.enterMailId()
        cls.signIn.enterPassword()
        cls.signIn.clickSignInBtn()
