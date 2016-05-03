import sys

import unittest
from com.Jabong.Scripts.Login.SignIn import SignInJabong
from com.Jabong.Scripts.Men.Clothing import BuyBlazzer

class Test_Suite(unittest.TestCase):
    def test_main(self):
        print('Inside Test_Suite class.')
        self.suite = unittest.TestSuite()
        self.suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(SignInJabong),
                             unittest.defaultTestLoader.loadTestsFromTestCase(BuyBlazzer)])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)

import unittest
if __name__=="__main__":
    unittest.main
