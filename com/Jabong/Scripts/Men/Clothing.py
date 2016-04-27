from com.Jabong.PageRepo.Men.Clothing import *
class BuyBlazzer(ClothingCategory):
    cc = ClothingCategory()
    def test_buyBlazzer(cls):
        cls.cc.clickMenBlock()
        cls.cc.clickSuitsBlazzer_CC()