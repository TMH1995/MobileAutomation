import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions
from selenium.webdriver.common.keys import Keys

desiredCap={
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "app": "C:\\APK\\Flipkart Online Shopping App_v7.6_apkpure.com.apk"
}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desiredCap)
driver.implicitly_wait(30)
driver.find_element_by_id("com.flipkart.android:id/select_btn").click()
driver.find_element_by_xpath("//android.widget.LinearLayout[@content-desc='0112 777 1446']/android.widget.LinearLayout").click()
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()

#interact with hamburger icon
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()

#Select electronics category
driver.find_element_by_xpath("//*[@text='Electronics']").click()

#Select Laptops products
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']").click()
time.sleep(5)

#Scrolling
for i in range(2):
    driver.swipe(550,2045,550,500,900)
    time.sleep(2)

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()
