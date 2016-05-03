from com.Jabong.PageRepo.Men.Clothing import *
#from com.Jabong.PageRepo.Sports
import logging

class BuyBlazzer(ClothingCategory):
    cc = ClothingCategory()
    sc = SportsCategory()

    def test_buyBlazzer(cls):
        cls.cc.clickMenBlock()
        logging.info('Clicked on Men link.')
        cls.cc.clickSuitsBlazers_CC()
        logging.info('clicked on Blazers.')


    def test_buyJerseys(cls):
        cls.sc.clickJerseys_SC()
        logging.info('clicked on Jerseys..')

if __name__ == "__main__":
    unittest.main()