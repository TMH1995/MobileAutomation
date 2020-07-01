import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions
from selenium.webdriver.common.keys import Keys

desiredCap={
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "browserName":"Chrome",
    "chromedriverExecutable":"C:\Program Files\Drivers\chromedriver.exe"
}
driver=webdriver.Remote("http://localhost:4723/wd/hub",desiredCap)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//*[@id=\"txtUsername\"]").send_keys("Admin")
driver.find_element_by_xpath("//*[@id=\"txtPassword\"]").send_keys("admin123")
driver.find_element_by_xpath("//*[@id=\"txtPassword\"]").send_keys(Keys.ENTER)
