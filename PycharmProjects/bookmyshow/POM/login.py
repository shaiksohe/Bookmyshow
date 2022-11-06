import re
from library.excel_lib import ReadExcel
from library.config import Config


class Loginpage:
    read_xl = ReadExcel()
    login_locators = read_xl.read_locators(Config.LOCATORS_SHEET)

    def _init_(self, driver):
        self.driver = driver

    def login_link(self):
        locator = self.login_locators["login_link"]
        self.driver.find_element(*locator).click()

    def enter_email(self, email):
        locator = self.login_locators["email_text"]
        self.driver.find_element(*locator).send_keys()

    def enter_password(self, password):
        locator = self.login_locators["pwd_text"]
        self.driver.find_element(*locator).send_keys()

    def click_remember_me_checkbox(self):
        locator = self.login_locators["remember_check_box"]
        self.driver.find_element(*locator).click()

    def click_forgot_pwd(self):
        locator = self.login_locators["forgot_pwd"]
        self.driver.find_element(*locator).click()

    def click_login_button(self):
        locator = self.login_locators["login_btn"]
        self.driver.find_element(*locator).click()
