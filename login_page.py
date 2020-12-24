from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import base_class

LOCATORS = {
    "email": (By.XPATH, '//input[@type="text" and @name="login"]'), # input[name="login"]
    "password": (By.XPATH, '//input[@type="password" and @name="pass"]'), # input[type="password"]
    "enter_button": (By.XPATH, '//form[@name="lform"]/p/input[@type="submit"]'), # form[name="lform"] input[type="submit"]
}


class Login_page(base_class.Basic_class):

    def open_page(self, url):
        self.driver.get(url)

    def user_login(self, email, password):
        self.driver.find_element(*LOCATORS["email"]).send_keys(email)
        self.driver.find_element(*LOCATORS["password"]).send_keys(password)
        self.driver.find_element(*LOCATORS["enter_button"]).click()