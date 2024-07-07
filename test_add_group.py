# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.fill_group_form(Group(group_name="group_name", group_header="group_header", group_footer="group_footer"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.fill_group_form(Group(group_name="", group_header="", group_footer=""))
        self.logout()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_group_page(self):
        wd = self.wd
        # return group page
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
        wd = self.wd
        # submit group create
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.wd
        self.open_group_page()
        self.init_group_creation()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        self.submit_group_creation()
        self.return_group_page()

    def init_group_creation(self):
        wd = self.wd
        # init group creation
        wd.find_element_by_name("new").click()

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
