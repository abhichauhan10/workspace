# coding=utf-8

'''
Challenge 3 - Loops:
Loops can be used to write your own wait statements.  They can also be used to iteration through a list of items.

For this challenge, go to copart and print a list of all the “Popular Items” of vehicle Make/Models on the home page and the URL/href for each type.  This list can dynamically change depending on what is authored by the content creator but using a loop will make sure that everything will be displayed regardless of the list size.

Author: Abhishek Chauhan
email: abhishek.chauhan@dish.com

'''

import unittest
from selenium import webdriver

POPULAR_ITEMS = "//*[@id=\"tabTrending\"]/div[1]"
POPULAR_CATEGORIES = "//*[@id=\"tabTrending\"]/div[3]"


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/abhishek/mywork/STG/challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com/")

        print "========== POPULAR ITEMS ==========="
        popular_elemets = self.driver.find_element_by_xpath(POPULAR_ITEMS)
        child_element = popular_elemets.find_elements_by_xpath('.//*')
        for child in child_element:
            if child.get_attribute("href") != None:
                print ("Text = %s and Url = %s " % (child.text, child.get_attribute("href")))

        print "\n======== POPULAR CATEGORIES ========"
        popular_elemets = self.driver.find_element_by_xpath(POPULAR_CATEGORIES)
        child_element = popular_elemets.find_elements_by_xpath('.//*')
        for child in child_element:
            if child.get_attribute("href") != None:
                print ("Text = %s and Url = %s " % (child.text, child.get_attribute("href")))


if __name__ == '__main__':
    unittest.main()
