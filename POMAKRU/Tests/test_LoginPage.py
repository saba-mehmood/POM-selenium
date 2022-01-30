import pytest


from POMAKRU.Config.config import TestData
from POMAKRU.Tests.test_Base import BaseTest
from POMAKRU.Pages.LoginPage import LoginPage

class TestLogin(BaseTest):
    def test_login(self):
        self.loginPage=LoginPage(self.driver)
        self.loginPage.Login(TestData.EMAIL)