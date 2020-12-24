from selenium import webdriver
import login_page
import email_page
import unittest



class IuaMailTest(unittest.TestCase):
    TIMEOUT = 20
    EMAIL = "quietman@i.ua"
    PASSWORD = "bigbang10"

    @classmethod
    def setUpClass(cls):
        cls.baseURL = "https://www.i.ua/"
        cls.driver = webdriver.Chrome()



    def setUp(self):
        self.login = login_page.Login_page(self, self.driver, 100)
        self.email = email_page.Emails(self, self.driver, self.TIMEOUT)

    def test_emails(self):
        self.login.open_page(self.baseURL)
        self.login.user_login(self.EMAIL, self.PASSWORD)
        emails = self.email.get_emails(10)
        self.assertEqual(10, len(emails))



    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(catchbreak=True)