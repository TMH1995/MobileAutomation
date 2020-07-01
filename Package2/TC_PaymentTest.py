import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print("This is payment in Dollars")
        self.assertTrue(True)
    def test_paymentInEuros(self):
        print("This is payment in Euros")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()