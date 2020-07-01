#assertIn & assertNotIn

import unittest
from appium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        list={"python","selenium","appium","java"}
        self.assertIn("python",list)
        #self.assertIn("C++", list)
        #self.assertNotIn("C++", list)
if __name__ == "__main__":
    unittest.main()
