from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Django', self.browser.title)  
        self.fail('Finish the test!')  


if __name__ == '__main__':  
    unittest.main(warnings='ignore')