import time

from selenium import webdriver
path=r'C:\Users\Sohail\PycharmProjects\bookmyshow\drivers\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)


url="https://in.bookmyshow.com/explore/home/bengaluru"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element("xpath",'//a[text()="Activities"]').click()

# driver.find_element("xpath",'//div[text()="Browse by Venues"]').click()
driver.find_element("xpath","//div[.='Wonderla Amusement Park Bangalore']").click()
driver.find_element("xpath",'//div[@class="df-ak df-bu df-bv"]').click()
driver.find_element("xpath",'//span[text()=22]').click()
driver.find_element("xpath",'//li[@data-id="time-pill"]').click()
driver.find_element("xpath","//button[.='Continue']").click()
driver.find_element("xpath", "//div[.='Senior Citizen']/../..//div[.='Add']").click()
driver.find_element("xpath", "//button[.='Proceed']").click()
driver.find_element("xpath", '//input[@type="text"]').send_keys("shaik mahammad sohail")
driver.find_element("xpath", '//input[@type="number"]').send_keys("9121694697")
driver.find_element("xpath",'//input[@type="email"]').send_keys("sohelshaik1742@gmail.com")
driver.find_element("xpath", '//input[@type="checkbox"]').click()
driver.find_element("xpath", "//button[.='Submit']").click()
# driver.find_element("xpath",'//button[@id="homedelivery-login-to-proceed-button"]').click()
driver.find_element("xpath",'//button[text()="Login to Proceed"]').click()
driver.find_element("id","mobileNo").send_keys("9121694697")
driver.find_element("xpath","//button[text()='Continue']").click()
# driver.find_element("xpath",'//li[@id="dTUPI"]').click()
# driver.find_element("xpath",'//button[text()="Continue"]').click()
#driver.find_element("xpath",'//button[@class="styles__LoginSubmitButton-dh558f-37 hxDztA"]').click()
# driver.find_element(("xpath",'(//div[@class="styles__ButttonWrap-dh558f-14 ghrqhk"])[1]')).click()
# driver.find_element("xpath",'//div[@class="styles__ButttonWrap-dh558f-14 ghrqhk"]').click()
# driver.find_element("xpath", '//div[@class="df-ak df-bu df-bv"]').click()
# driver.find_element("xpath",'(//div[@class="styles__ButttonWrap-dh558f-14 ghrqhk"])[1]').click()
# driver.find_element("class","whsOnd zHQkBf").send_keys("sohelshaik1742@gmail.com")

# driver.find_element("xpath",'(//div[@data-id="add-tickets"])[1]').click()
# driver.find_element("xpath",'(//div[text()="Add"])[1]').click()
# driver.find_element("xpath","//div[.='Children (Under 10)']/../..//div[.='Add']").click()
# driver.find_element("xpath",'(//div[text()="Add"])[3]').click()
# driver.find_element("xpath",'(//div[@class="df-bv df-bw df-bx df-f df-l"])[1]').click()

#driver.find_element("xpath",'//div[@class="sc-28e42w-0 cAaAqt"]').click()
# driver.find_element("class","sc-7o7nez-0 bRdSOI").click()
#time.sleep(2)
# driver.find_element("class name",'sc-28e42w-0.cAaAqt').click()

#driver.find_element("xpath","(//div[text()='Browse by Venues'])[2]").click()
#driver.find_element("xpath","(//div[text()='Browse by Venues'])[2]").click()

#driver.find_element("xpath",'(//a[@class="sc-fOICqy faULzO"])[6]').click()
#driver.find_element("class name","sc-28e42w-0.cAaAqt").click()
#driver.find_element("xpath",'(//div[@class="sc-7o7nez-0 bRdSOI"]').click()
# driver.find_element("xpath",'(//div[@class="df-be df-cd df-eg"])[9]').click()
# driver.find_element("class","df-a df-aj df-al df-am df-ci df-d df-eo df-ep df-eq df-er df-es df-et df-eu").click()




