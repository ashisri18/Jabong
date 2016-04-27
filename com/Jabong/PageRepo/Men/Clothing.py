from com.Jabong.GenericLib.Initilization import *
from selenium.webdriver.common.action_chains import ActionChains
class ClothingCategory(Initilization):

    driver = Initilization.driver


    def clickMenBlock(cls):
        menBlock = cls.driver.find_element_by_xpath("//ul[@id='mainTopNav']/li[@class='nav-men']")
        menBlock.click()
        time.sleep(2)

    def clickSuitsBlazzer_CC(cls):
#        menBlock = cls.driver.find_element_by_xpath("//ul[@id='mainTopNav']/li[@class='nav-men']")
        suitsBlazzers = cls.driver.find_element_by_xpath("//div[@class='dropdown-container row']//a[text()='Suits & Blazers']")
#        ActionChains(cls.driver).move_to_element(menBlock).perform()
        suitsBlazzers.click()
        time.sleep(3)
