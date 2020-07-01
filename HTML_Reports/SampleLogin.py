from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver=webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("http://testing-ground.scraping.pro/login")
        self.assertEqual("Web Scraper Testing Ground",self.driver.title,"Webtitle isn't matching")

    def test_login(self):
        self.driver.get("http://testing-ground.scraping.pro/login")
        self.driver.find_element_by_id("usr").send_keys("admin")
        self.driver.find_element_by_id("pwd").send_keys("12345")
        self.driver.find_element_by_xpath("//*[@id='case_login']/form/input[3]").click()
        self.status=self.driver.find_element_by_xpath("//*[@id='case_login']/h3").get_attribute('innerHTML')
        self.assertEqual("WELCOME :)11", self.status, "Webtitle isn't matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed......")


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\\TARIQ\\PycharmProjects\\MobileAutomation\\Reports'))
