import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#Get all the tests from LoginTest, SignupTest, PaymentTest, PaymentReturnsTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Creating test suites
SanityTestSuite=unittest.TestSuite([tc1,tc2]) #Sanity test suite
FunctionalTestSuite=unittest.TestSuite([tc3,tc4]) #Functional test suite
MasterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4]) #Master test suite

unittest.TextTestRunner(verbosity=2).run(FunctionalTestSuite)

# runner= HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_name="Full report 2",output = r'C:\Users\\TARIQ\\PycharmProjects\\MobileAutomation\\Reports')
# runner.run(MasterTestSuite)
