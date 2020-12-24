from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://www.i.ua")

    first_name = browser.find_element_by_name("login").send_keys("quietman@i.ua")

    last_name = browser.find_element_by_name("pass").send_keys("bigbang10")

    button = browser.find_element_by_css_selector('[tabindex="5"]').click()

    lists = browser.find_elements_by_css_selector('[firstdomain]')

    print("Found " + str(len(lists)) + " searches:")

    i = 0
    for listitem in lists:
        print(listitem.get_attribute('firstdomain'))
        i = i + 1
        if (i > 10):
            break

finally:
    browser.quit()