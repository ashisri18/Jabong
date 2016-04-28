from com.Jabong.GenericLib.Initilization import *
from selenium.webdriver.common.action_chains import ActionChains
from com.Jabong.PageRepo.Home.Home_Page_Constants import *

class ClothingCategory(Initilization):

    driver = Initilization.driver

    def clickMenBlock(cls):
        menBlock = cls.driver.find_element_by_xpath("//ul[@id='mainTopNav']/li[@class='nav-men']")
        menBlock.click()
#        cls.driver.find_element_by_xpath(Home_Page_Constants.Men_Link).click()
        time.sleep(2)

    def clickSuitsBlazers_CC(cls):
#        menBlock = cls.driver.find_element_by_xpath("//ul[@id='mainTopNav']/li[@class='nav-men']")
        suitsBlazers = cls.driver.find_element_by_xpath("//div[@class='dropdown-container row']//a[text()='Suits & Blazers']")
#        ActionChains(cls.driver).move_to_element(menBlock).perform()
        time.sleep(3)
        suitsBlazers.click()
        time.sleep(3)

class SportsCategory(Initilization):

    driver = Initilization.driver

    def clickJerseys_SC(cls):
        sportsBlock = cls.driver.find_element_by_xpath("//ul[@id='mainTopNav']/li[@class='nav-sports']")
        jerseys = cls.driver.find_element_by_xpath("//div[@class='dropdown-container row']//a[text()='Jerseys']")
        ActionChains(cls.driver).move_to_element(sportsBlock).perform()
        time.sleep(3)
        jerseys.click()
        time.sleep(3)