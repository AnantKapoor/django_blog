from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Users/sumantkapoor/work/django_blog/geckodriver.exe')
browser = webdriver.Firefox(firefox_binary=binary)
'''


import unittest
import time

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()


    def test_can_create_and_save_a_cv(self):  
 
        self.browser.get('http://127.0.0.1:8000/admin')

        username_input = self.browser.find_element_by_id('id_username')  
        username_input.send_keys('anant')  

        password_input = self.browser.find_element_by_id('id_password')  
        password_input.send_keys('********')  
        password_input.send_keys(Keys.ENTER)  
        time.sleep(1)  

        self.browser.get("http://127.0.0.1:8000/admin/cv/education/add/")

        time.sleep(1)

        title_input = self.browser.find_element_by_id('id_title')  
        time.sleep(1)

        title = 'TestEducation'
        title_input.send_keys(title)

        grade_input = self.browser.find_element_by_id('id_grades')
        grade_input.send_keys("Full Marks")

        description='Anant is the best'
        desc_input =self.browser.find_element_by_id('id_description')
        time.sleep(1)
        desc_input.send_keys(description)

        date1='2020-12-12'
        grad_input =self.browser.find_element_by_id('id_graduation_date_0')
        time.sleep(1)
        grad_input.send_keys(date1)

        time1='11:00:00'
        grad1_input =self.browser.find_element_by_id('id_graduation_date_1')
        time.sleep(1)
        grad1_input.send_keys(time1)

        grade_input.send_keys(Keys.ENTER)  
        time.sleep(1)  

        self.browser.get('http://127.0.0.1:8000/cv')
        time.sleep(1)

        self.assertIn(title, self.browser.page_source )
        self.assertIn('Full Marks', self.browser.page_source )
        self.assertIn(description, self.browser.page_source )
        self.assertIn('Dec. 12, 2020', self.browser.page_source )
        self.assertIn('11 a.m.', self.browser.page_source )

if __name__ == '__main__':  
    unittest.main(warnings='ignore')