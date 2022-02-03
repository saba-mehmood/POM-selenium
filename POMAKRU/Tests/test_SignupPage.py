import pytest
from POMAKRU.Config.config import TestData
from POMAKRU.Tests.test_Base import BaseTest
from POMAKRU.Pages.SignupPage import SignUp

class TestSignup(BaseTest):
    def test_signup(self):
        self.signupPage=SignUp(self.driver)
        self.signupPage.Signup(TestData.EMAIL_SIGNUP,TestData.FIRST_NAME,TestData.LAST_NAME,TestData.ADDRESS,
        TestData.CITY,TestData.ZIP_CODE,TestData.PHONE_NO, TestData.SSN
        )
        