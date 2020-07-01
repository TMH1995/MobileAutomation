import unittest



def setUpModule():
    print ("SetUpModule")
def tearDownModule():
    print("tearDownModule")

class Test(unittest.TestCase):
    @classmethod
    def setUp(self):#Execute before each test case
        print("This is login test")
    @classmethod
    def tearDown(self) :#Execute after each test case
        print("This is logout test")
    @classmethod
    def setUpClass(cls):#Execute once before all test methods in the class
        print("Open Application")
    @classmethod
    def tearDownClass(cls):#Execute once after all test methods in the class
        print("Close Application")

    def test_firstcase(self):
        print("This is my first test case")

    def test_secondcase(self):
        print("This is my second test case")

    def test_thirdcase(self):
        print("This is my third test case")

if __name__=="main":
    unittest.main()