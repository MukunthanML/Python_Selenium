from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.implicitly_wait(5)
# select radio button 2 and assert
driver.find_element_by_css_selector("input[value='radio2']").click()

# Select Indonesia from suggestion dropdown and assert


driver.find_element_by_xpath("//*[@id='autocomplete']").send_keys("ind")

auto_suggestions = driver.find_elements_by_class_name("ui-menu-item")
for suggestion in auto_suggestions:
    if suggestion.text == 'Indonesia':
        suggestion.click()

# Select option 2 from static option dropdown and assert
dropdown = Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_visible_text("Option2")

# Select check box 1,3 and assert
driver.find_element_by_id("checkBoxOption1").click()
driver.find_element_by_id("checkBoxOption3").click()


# Enter your name in text box(under Switch To Alert Example)
# Click alert button and assert alert message should have your name in alert message.
# then accept alert box.
driver.find_element_by_id("name").send_keys("Mukunthan")
driver.find_element_by_id("alertbtn").click()
alert1 = driver.switch_to.alert
assert "Mukunthan" in alert1.text
alert1.accept()


# Enter your name in text box(under Switch To Alert Example)
# Click confirm button and assert alert message should have your name in alert message.
# then cancel alert box.
driver.find_element_by_id("name").send_keys("Mukunthan")
driver.find_element_by_id("confirmbtn").click()
alert2 = driver.switch_to.alert
assert "Mukunthan" in alert1.text
alert2.dismiss()

# Click on open window button, and switch to new window(child window) and assert title. Then switch back to original window.
driver.find_element_by_id("openwindow").click()
handles = driver.window_handles
print('No of window(s) opened', len(handles))
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]

driver.switch_to.window(window_after)
print(driver.title)
title1 = "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"
assert title1 == driver.title
driver.close()
driver.switch_to.window(window_before)

# Click on open tab button, and switch to new tab(child window) and assert title. Then switch back to original window.e
driver.find_element_by_id("opentab").click()
handles = driver.window_handles
print('No of tabs(s) opened', len(handles))

window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
print(driver.title)
title2 ="Rahul Shetty Academy"
assert title2 == driver.title
driver.close()
driver.switch_to.window(window_before)
# Interrogate the web table and get the rows which has testing in it.
# Get the count of courses having selenium in it.
course_rows = driver.find_elements_by_xpath("//table[@id='product']//tr/td[2]")
testing_courses = [course.text for course in course_rows if 'selenium' in str(course.text).lower()]
print('Selenium related courses', testing_courses)
print('Selenium related courses - count: ', len(testing_courses))


# Enter your name in text box under 'Element Displayed Example'.
# Click Hide button and assert the text box is not shown
# Click Show button and assert the text box is shown and assert text value with value that we entered.

hide_text_box = driver.find_element_by_name("show-hide")
hide_text_box.send_keys("Play")
driver.find_element_by_id("hide-textbox").click()
assert not hide_text_box.is_displayed()
driver.find_element_by_id("show-textbox").click()
assert hide_text_box.is_displayed()
assert hide_text_box.get_attribute('value') == "Play"


# Mouse hover the 'Mouse hover' button get the all the options and log in console.

mouse_hover_button = driver.find_element_by_id("mousehover")
ActionChains(driver).move_to_element(mouse_hover_button).perform()
mouse_hover_options = driver.find_elements_by_css_selector("div .mouse-hover-content a")
print('Mouse hover options:')
for option in mouse_hover_options:
    print(option.text)

# Get the total count of iframe/frame/frameset present in current page.
# Switch to first iframe and get all list of urls in iframe and switch back to main window.

frames = driver.find_elements_by_tag_name("iframe")
print('Frames count: ', len(frames))
driver.switch_to.frame(frames[0])
frame_urls = driver.find_elements_by_tag_name("a")
print('URLs count in frame: ', len(frame_urls))
# Close the main windows and all child windows.
driver.quit()
