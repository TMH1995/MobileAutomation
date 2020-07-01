#assertEqual & assertNotEqual

import unittest
from appium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        desiredCap = {
            "platformName": "Android",
            "deviceName":"Android Emulator",
            "automationName": "UiAutomator2",
            "browserName": "Chrome",
            "chromedriverExecutable": "C:\Program Files\Drivers\chromedriver.exe"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredCap)
        driver.get("http://www.google.com/")
        titleOfWebPage=driver.title
        self.assertEqual("Google",titleOfWebPage,"webpage title aren't same")
        #self.assertNotEqual("Google",titleOfWebPage)

if __name__ == "__main__":
    unittest.main()
