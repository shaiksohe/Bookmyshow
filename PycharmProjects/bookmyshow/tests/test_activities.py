import datetime
import pytest
from POM.activities import Activitiespage
from library.excel_lib import ReadExcel
from library.config import Config




class TestActivitiespage:

    read_xl = ReadExcel()
    data = read_xl.read_testdata("activities")

    @pytest.mark.parametrize("fname, Phnumber,email_address", data)
    def test_valid_credentials(self,init_driver,fname, Phnumber,email_address):
        driver = init_driver
        ap = Activitiespage(driver)

        try:
            ap.clickon_activities()
            ap.clickonwonderla_amusementpark_banglore()
            ap.clickon_book()
            ap.clickon_date()
            ap.clickon_time()
            ap.clickon_continue()
            ap.clickon_add()
            ap.clickon_proceed()
            ap.clickon_fname(fname)
            ap.clickon_number(Phnumber)
            ap.clickon_email(email_address)
            ap.clickon_checkbox()
            ap.clickon_submit()


        except BaseException as err_msg:
            # td = datetime.datetime.now()
            # name = f"screenshot_{td.hour}{td.minute}{td.second}.png"
            # # path = r"C:\Users\91779\PycharmProjects\pythonProject1\screenshot\\"
            # driver.save_screenshot(Config.SCREENSHOTS_PATH+name)
            raise err_msg
