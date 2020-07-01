import unittest




class Test(unittest.TestCase):
    def test_firstcase(self):
        print("This is my first test case")

    def test_secondcase(self):
        print("This is my second test case")

    def test_thirdcase(self):
        print("This is my third test case")

if __name__=="main":
    unittest.main()