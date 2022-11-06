import time

from behave import *
from selenium import webdriver

path = r'C:\Users\Sohail\PycharmProjects\bookmyshow\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)


@given(u'user is able to launch the browser')
def lanuchthe_browser(context):
    path = r'C:\Users\Sohail\PycharmProjects\bookmyshow\drivers\chromedriver.exe'
    context.driver = webdriver.Chrome(executable_path=path)


@when(u'user is able to enter the url')
def enterthe_url(context):
    context.driver.get(r"https://in.bookmyshow.com/explore/home/bengaluru")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u'user is able to click on activities')
def clickon_activities(context):
    context.driver.find_element("xpath", "//a[text()='Activities']").click()
    context.driver.implicitly_wait(2)


@then(u'user is able to select one activity')
def select_oneactivity(context):
    context.driver.find_element("xpath", "//div[.='Wonderla Amusement Park Bangalore']").click()
    context.driver.implicitly_wait(2)


@then(u'user is able to book the activity')
def book(context):
    context.driver.find_element("xpath", '//div[@class="df-ak df-bu df-bv"]').click()


@then(u'user is able to slect date and time')
def date_time(context):
    context.driver.find_element("xpath", '//span[text()=22]').click()


@then(u'user is able to click on continue')
def clickon_continue(context):
    context.driver.find_element("xpath", '//li[@data-id="time-pill"]').click()


@then(u'user is able to add the ticket')
def add_ticket(context):
    context.driver.find_element(r"xpath", "//button[.='Continue']").click()


@then(u'user is able to select the ticket')
def select_ticket(context):
    context.driver.find_element("xpath", "//div[.='Senior Citizen']/../..//div[.='Add']").click()


@then(u'user is able to click on proceed')
def proceed(context):
    context.driver.find_element("xpath", "//button[.='Proceed']").click()
    time.sleep(3)


@then(u'user is able to enter the full name "{full_name}"')
def name(context, full_name):
    context.driver.find_element("xpath", '//input[@type="text"]').send_keys(full_name)


@then(u'user is able to enter the "{mobile_number}"')
def step_impl(context, mobile_number):
    context.driver.find_element("xpath", '//input[@type="number"]').send_keys(mobile_number)


@then(u'user is able to enter the email address "{email_address}"')
def step_impl(context, email_address):
    context.driver.find_element("xpath", '//input[@type="email"]').send_keys(email_address)


@then(u'user is able to click on checkbox')
def checkbox(context):
    context.driver.find_element("xpath", '//input[@type="checkbox"]').click()


@then(u'user is able to click on submit')
def clickon_submit(context):
    context.driver.find_element("xpath", "//button[.='Submit']").click()
    context.driver.implicitly_wait(10)


@then(u'user is able to click on proceed to pay')
def clickon_proceedtopay(context):
    context.driver.find_element("xpath", '//button[text()="Login to Proceed"]').click()


@then(u'user is able to enter the mobile number into textfield "{phone_number}"')
def phone_num(context, phone_number):
    context.driver.find_element("id", "mobileNo").send_keys(phone_number)


@then(u'user is able to click on continue button')
def clickon_continuebutton(context):
    context.driver.find_element("xpath", "//button[text()='Continue']").click()
    context.driver.close()
