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
driver.implicitly_wait(5)
driver.find_element_by_accessibility_id("Search on flipkart").click()
driver.find_element_by_xpath("//android.widget.EditText[@content-desc='Search grocery products in Supermart']").send_keys('iphone\n')
driver.execute_script('mobile: performEditorAction', {'action': 'search'})
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()