import time
import unittest
from appium import webdriver
from setting import Locator as L


class TestLogin(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DeviceAppium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login_normal(self):
        L.StepRegister(self)
        self.driver.back()
        L.InputID(self, L.LoginPage.Email, "dfawwaz17@gmail.com")
        L.InputID(self, L.LoginPage.Pwd, "123")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.ValidateText(self, L.LoginPage.HomeWelcome, "dfawwaz17@gmail.com")

    def test_login_account_not_registered(self):
        L.InputID(self, L.LoginPage.Email, "dfawwaz99@gmail.com")
        L.InputID(self, L.LoginPage.Pwd, "123")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.ValidateText(self, L.LoginPage.SnackBar, "Wrong Email or Password")

    def test_login_account_wrong_email(self):
        L.InputID(self, L.LoginPage.Email, "dfawwaz177@gmail.com")
        L.InputID(self, L.LoginPage.Pwd, "123")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.ValidateText(self, L.LoginPage.SnackBar, "Wrong Email or Password")

    def test_login_account_wrong_password(self):
        L.InputID(self, L.LoginPage.Email, "dfawwaz17@gmail.com")
        L.InputID(self, L.LoginPage.Pwd, "1234")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.ValidateText(self, L.LoginPage.SnackBar, "Wrong Email or Password")

    def test_login_account_email_empty(self):
        L.InputID(self, L.LoginPage.Pwd, "1234")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.Validasi_Display(self, L.LoginPage.EmailEmpty)

    def test_login_password_empty(self):
        L.InputID(self, L.LoginPage.Email, "dfawwaz17@gmail.com")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.Validasi_Display(self, L.LoginPage.PasswordEmpty)

    def test_login_email_wrong_format(self):
        L.InputID(self, L.LoginPage.Email, "dfawwaz17gmail.com")
        L.InputID(self, L.LoginPage.Pwd, "123")
        L.TapID(self, L.LoginPage.BTNLogin)
        L.Validasi_Display(self, L.LoginPage.EmailEmpty)
