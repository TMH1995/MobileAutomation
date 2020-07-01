import unittest

class SignupTest(unittest.TestCase):
    def test_SignupbyEmail(self):
        print("This is Signup by email test")
        self.assertTrue(True)
    def test_SignupbyFacebook(self):
        print("This is Signup by Facebook test")
        self.assertTrue(True)

    def test_SignupbyTwitter(self):
        print("This is Signup by Twitter test")
        self.assertTrue(True)


if __name__== "__main__":
    unittest.main()