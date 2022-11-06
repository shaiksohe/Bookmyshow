import pytest
from library.config import Config
from selenium import webdriver


@pytest.fixture(params=["chrome"])
def init_driver(request):
    global driver
    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path = Config.CHROME_PATH )
    #
    # else:
    #     driver = webdriver.Edge(executable_path=Config.MSEDGE_PATH)

    driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()