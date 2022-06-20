from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from assertpy import assert_that
from faker import Faker


class Locator(object):
    url_api = "https://jsonplaceholder.typicode.com/posts"
    fake = Faker()
    fake_email = fake.email()

    DeviceAppium = {
        "appium:udid": "emulator-5554",
        "platformName": "Android",
        "app": "C:/Users/dfaww/PycharmProjects/test-automation/apk/test.apk",
        "appium:appPackage": "com.loginmodule.learning",
        "appium:appActivity": "com.loginmodule.learning.activities.LoginActivity"
    }

    # FUNCTION
    @staticmethod
    def ScrollByID(self, id):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)' +
                                 f'.scrollIntoView(new UiSelector().resourceIdMatches(\"{id}\"))')

    @staticmethod
    def TapID(self, elem):
        self.driver.find_element(By.ID, elem).click()

    @staticmethod
    def InputID(self, elem, text):
        self.driver.find_element(By.ID, elem).send_keys(text)

    @staticmethod
    def ValidateText(self, elem, text):
        assert_that(self.driver.find_element(By.ID, elem).text).contains(text)

    @staticmethod
    def Validasi_Display(self, elem):
        assert_that(self.driver.find_element(By.XPATH, elem).is_displayed()).is_equal_to(True)

    @staticmethod
    def StepRegister(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)' +
                                 f'.scrollIntoView(new UiSelector().resourceIdMatches(\"com.loginmodule.learning:id/textViewLinkRegister\"))')
        self.driver.find_element(By.ID, "com.loginmodule.learning:id/textViewLinkRegister").click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)' +
                                 f'.scrollIntoView(new UiSelector().resourceIdMatches(\"com.loginmodule.learning:id/appCompatButtonRegister\"))')
        self.driver.find_element(By.ID, "com.loginmodule.learning:id/textInputEditTextName").send_keys("Fawwaz")
        self.driver.find_element(By.ID, "com.loginmodule.learning:id/textInputEditTextEmail").send_keys(
            "dfawwaz17@gmail.com")
        self.driver.find_element(By.ID, "com.loginmodule.learning:id/textInputEditTextPassword").send_keys("123")
        self.driver.find_element(By.ID, "com.loginmodule.learning:id/textInputEditTextConfirmPassword").send_keys("123")
        self.driver.find_element(By.ID, "com.loginmodule.learning:id/appCompatButtonRegister").click()

    # LOCATOR
    class RegisterPage:
        LinkRegister = "com.loginmodule.learning:id/textViewLinkRegister"
        BTNRegister = "com.loginmodule.learning:id/appCompatButtonRegister"
        Name = "com.loginmodule.learning:id/textInputEditTextName"
        Email = "com.loginmodule.learning:id/textInputEditTextEmail"
        Pwd = "com.loginmodule.learning:id/textInputEditTextPassword"
        ConfirmPwd = "com.loginmodule.learning:id/textInputEditTextConfirmPassword"
        SnackBar = "com.loginmodule.learning:id/snackbar_text"
        NameEmpty = '//android.widget.TextView[@text="Enter Full Name"]'
        EmailEmpty = '//android.widget.TextView[@text="Enter Valid Email"]'
        PasswordEmpty = '//android.widget.TextView[@text="Enter Password"]'
        ConfirmPasswordEmpty = '//android.widget.TextView[@text="Password Does Not Matches"]'

    class LoginPage:
        Email = "com.loginmodule.learning:id/textInputEditTextEmail"
        Pwd = "com.loginmodule.learning:id/textInputEditTextPassword"
        BTNLogin = "com.loginmodule.learning:id/appCompatButtonLogin"
        LinkLogin = "com.loginmodule.learning:id/appCompatTextViewLoginLink"
        HomeWelcome = "com.loginmodule.learning:id/textViewName"
        SnackBar = "com.loginmodule.learning:id/snackbar_text"
        EmailEmpty = '//android.widget.TextView[@text="Enter Valid Email"]'
        PasswordEmpty = '//android.widget.TextView[@text="Enter Valid Email"]'

