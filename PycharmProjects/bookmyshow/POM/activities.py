import re
import time
from library.excel_lib import ReadExcel
from library.config import Config


class Activitiespage:
    read_xl = ReadExcel()
    reg_locators = read_xl.read_locators(Config.LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def clickon_activities(self):
        locator = self.reg_locators["clickon_activities"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def clickonwonderla_amusementpark_banglore(self):
        locator = self.reg_locators["clickonwonderla_amusementpark_banglore"]
        self.driver.find_element(*locator).click()

    def clickon_book(self):
        locator = self.reg_locators["clickon_book"]
        self.driver.find_element(*locator).click()

    def clickon_date(self):
        locator = self.reg_locators["clickon_date"]
        self.driver.find_element(*locator).click()

    def clickon_time(self):
        locator = self.reg_locators["clickon_time"]
        self.driver.find_element(*locator).click()

    def clickon_continue(self):
        locator = self.reg_locators["clickon_continue"]
        self.driver.find_element(*locator).click()

    def clickon_add(self):
        locator = self.reg_locators["clickon_add"]
        self.driver.find_element(*locator).click()

    def clickon_proceed(self):
        locator = self.reg_locators["clickon_proceed"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def clickon_fname(self,fname):
        locator = self.reg_locators["clickon_fname"]
        self.driver.find_element(*locator).send_keys(fname)
        time.sleep(2)

    def clickon_number(self,Phnumber):
        if isinstance(Phnumber,float):
            Phnumber = str(int(Phnumber))
            assert len(Phnumber)==10
        locator = self.reg_locators["clickon_number"]
        self.driver.find_element(*locator).send_keys(Phnumber)
        time.sleep(2)

    def clickon_email(self, email_address):
        if isinstance(email_address,float):
            email_address = str(int(email_address))
        locator = self.reg_locators["clickon_email"]
        self.driver.find_element(*locator).send_keys(email_address)
        time.sleep(2)

    def clickon_checkbox(self):
        locator = self.reg_locators["clickon_checkbox"]
        self.driver.find_element(*locator).click()

    def clickon_submit(self):
        locator = self.reg_locators["clickon_submit"]
        self.driver.find_element(*locator).click()
