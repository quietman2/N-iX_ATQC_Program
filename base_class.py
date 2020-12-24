from selenium.webdriver.support.ui import WebDriverWait


class Basic_class(object):
    def __init__(self, testcase, driver, timeout):
        self.testcase = testcase
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)