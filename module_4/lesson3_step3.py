import unittest
from selenium import webdriver


class TestRegistration(unittest.TestCase):

    def test_page1(self):

        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first = browser.find_element_by_css_selector('input.first[required]')
        first.send_keys('Firstname')

        last = browser.find_element_by_css_selector('input.second[required]')
        last.send_keys('Lastname')

        email = browser.find_element_by_css_selector('input.third[required]')
        email.send_keys('email@example.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Wrong')
        browser.quit()

    def test_page2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)


        first = browser.find_element_by_css_selector('input.first[required]')
        first.send_keys('Firstname')

        last = browser.find_element_by_css_selector('input.second[required]')
        last.send_keys('Lastname')

        email = browser.find_element_by_css_selector('input.third[required]')
        email.send_keys('email@example.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Wrong')
        browser.quit()


if __name__ == "__main__":
    unittest.main()
