from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import base_class
import re

LOCATORS = {
    "email": lambda amount: (By.XPATH, '//div/a/span[@class="frm"]' % amount) # span.frm
}

class Emails(base_class.Basic_class):

    def get_emails(self, amount):
        emails = []
        email_tags = self.driver.find_elements_by_xpath('//div/a/span[@class="frm"]') #find_elements_by_css_selector('span.frm')
        for item in email_tags[:amount]:
            emails.append(item.text)
        return emails


        # for i in range(amount):
        #     email = self.driver.find_element(*LOCATORS["email"](i + 1)).text
        #     emails.append(email)
        # return emails