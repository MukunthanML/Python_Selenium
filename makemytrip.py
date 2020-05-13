from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.makemytrip.com/')
driver.maximize_window()

#driver.find_element_by_xpath("//*[@class='specialFare']/li[1]").click()
# print(driver.find_element_by_xpath("//*[@class='specialFare']/li[1]").text


# driver.find_element_by_xpath("//*[text()='Student Fare']").click()
# print(driver.find_element_by_xpath("//*[text()='Student Fare']").text)


# driver.find_element_by_xpath("//*[contains(text(),'Student')]").click()
# print(driver.find_element_by_xpath("//*[contains(text(),'Student')]").text)


driver.find_element_by_xpath("//*[contains(text(),'STUDENT')]").click()
print(driver.find_element_by_xpath("//*[contains(text(),'STUDENT')]").text)
