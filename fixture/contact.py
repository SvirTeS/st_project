from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php') and len(wd.find_elements_by_name("Delete")) > 0):
            # open home page
            wd.get("http://localhost/addressbook/index.php")

    def open_page_to_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_contact_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            # fill contact data
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_data(self, contact):
        self.change_contact_fill_value('firstname', contact.firstname)
        self.change_contact_fill_value('lastname', contact.lastname)
        self.change_contact_fill_value('nickname', contact.nickname)
        self.change_contact_fill_value('title', contact.title)
        self.change_contact_fill_value('company', contact.company)
        self.change_contact_fill_value('address', contact.address)
        self.change_contact_fill_value('home', contact.home_phone)
        self.change_contact_fill_value('email', contact.email)

    def create(self, contact):
        wd = self.app.wd
        self.open_page_to_add_contact()
        # fill contact data
        self.fill_contact_data(contact)
        # save data
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def del_some_contact(self, index):
        self.open_home_page()
        self.select_contact_by_index(index)
        self.del_contact()
        self.contact_cache = None

    def del_first_contact(self):
        self.del_some_contact(0)

    def del_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()

    def mod_first_contact(self):
        self.mod_some_contact(0)

    def mod_some_contact(self, index, contact):
        self.open_home_page()
        self.update_contact_by_index(index)
        self.fill_contact_data(contact)
        self.submit_mod_contact()
        self.contact_cache = None

    def submit_mod_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def update_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()

    def open_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements("xpath", "//img[@alt='Details']")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, home_phone=all_phones[0],
                                                  mobile_phone=all_phones[1], work_phone=all_phones[2]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.update_contact_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = re.search('H: (.*)', text).group(1)
        work_phone = re.search('W: (.*)', text).group(1)
        mobile_phone = re.search('M: (.*)', text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone)
