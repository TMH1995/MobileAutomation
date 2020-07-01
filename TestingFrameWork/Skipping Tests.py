import unittest


class Test(unittest.TestCase):
    @unittest.SkipTest
    def test_firstcase(self):
        print("This is my first test case")

    def test_secondcase(self):
        print("This is my second test case")

    def test_thirdcase(self):
        print("This is my third test case")

    @unittest.skip("The test isn't ready yet")
    def test_fourthcase(self):
        print("This is my fourth test case")

    def test_fifthcase(self):
        print("This is my fifth test case")

    @unittest.skipIf(1==1,"Number aren't equal")
    def test_sixthcase(self):
        print("This is my sixth test case")


if __name__=="main":
    unittest.main()