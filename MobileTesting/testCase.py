from appium import webdriver
from selenium.webdriver.common.keys import Keys

desiredCap={
    "platformName": "Android",
    "platformVersion": "10.0",
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
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@index='0']").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

#Select a laptop
price= driver.find_element_by_xpath("//android.widget.TextView[@bounds='[297,592][461,647]']").get_attribute("text")

#Check the price and perform an assertion
print("The price of the first module is "+price)
assert price =="₹23,992","The price isn't matched"
