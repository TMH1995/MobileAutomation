from appium import webdriver

desiredCap={
    "platformName": "Android",
    "platformVersion": "10.0",
    "automationName": "Appium",
    "app": "C:\\APK\\ApiDemos-debug.apk"
}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desiredCap)
