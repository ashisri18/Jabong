from com.Jabong.PageRepo.Men.Clothing import *
#from com.Jabong.PageRepo.Sports

class BuyBlazzer(ClothingCategory):
    cc = ClothingCategory()
    sc = SportsCategory()

    def test_buyBlazzer(cls):
        cls.cc.clickMenBlock()
        cls.cc.clickSuitsBlazers_CC()

    def test_buyJerseys(cls):
        cls.sc.clickJerseys_SC()