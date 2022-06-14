import time
import unittest
from appium import webdriver
from setting import Locator as L


class TestRegister(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DeviceAppium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_register_normal(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Email, L.fake_email)
        L.InputID(self, L.RegisterPage.Pwd, "123")
        L.InputID(self, L.RegisterPage.ConfirmPwd, "123")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.ValidateText(self, L.RegisterPage.SnackBar, "Registration Successful")

    def test_register_name_empty(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Email, L.fake_email)
        L.InputID(self, L.RegisterPage.Pwd, "123")
        L.InputID(self, L.RegisterPage.ConfirmPwd, "123")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.Validasi_Display(self, L.RegisterPage.NameEmpty)

    def test_register_email_empty(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Pwd, "123")
        L.InputID(self, L.RegisterPage.ConfirmPwd, "123")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.Validasi_Display(self, L.RegisterPage.EmailEmpty)

    def test_register_email_invalid_format(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Email, "dfaw17gmail.com")
        L.InputID(self, L.RegisterPage.Pwd, "123")
        L.InputID(self, L.RegisterPage.ConfirmPwd, "123")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.Validasi_Display(self, L.RegisterPage.EmailEmpty)

    def test_register_password_empty(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Email, L.fake_email)
        L.InputID(self, L.RegisterPage.ConfirmPwd, "123")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.Validasi_Display(self, L.RegisterPage.PasswordEmpty)

    def test_register_confirm_password_empty(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Email, L.fake_email)
        L.InputID(self, L.RegisterPage.Pwd, "123")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.Validasi_Display(self, L.RegisterPage.ConfirmPasswordEmpty)

    def test_register_password_confpasswrd_doesnt_match(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Email, L.fake_email)
        L.InputID(self, L.RegisterPage.Pwd, "123")
        L.InputID(self, L.RegisterPage.ConfirmPwd, "124")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.Validasi_Display(self, L.RegisterPage.ConfirmPasswordEmpty)

    def test_register_weak_password(self):
        L.ScrollByID(self, L.RegisterPage.LinkRegister)
        L.TapID(self, L.RegisterPage.LinkRegister)
        L.ScrollByID(self, L.RegisterPage.BTNRegister)
        L.InputID(self, L.RegisterPage.Name, "Fawwaz")
        L.InputID(self, L.RegisterPage.Email, L.fake_email)
        L.InputID(self, L.RegisterPage.Pwd, "a")
        L.InputID(self, L.RegisterPage.ConfirmPwd, "a")
        L.TapID(self, L.RegisterPage.BTNRegister)
        L.ValidateText(self, L.RegisterPage.SnackBar, "Registration Successful")
