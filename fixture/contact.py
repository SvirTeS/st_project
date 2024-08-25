from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php') and len(wd.find_elements_by_name("Delete")) > 0):
            # open home page
            wd.find_element_by_link_text("home").click()

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

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        self.open_home_page()
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        self.open_home_page()
        self.contact_cache = None

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def mod_first_contact(self):
        self.mod_contact_by_index(0)

    def mod_contact_by_index(self, index, contact):
        self.open_home_page()
        self.update_contact_by_index(index)
        self.fill_contact_data(contact)
        self.submit_mod_contact()
        self.contact_cache = None

    def mod_contact_by_id(self, id, contact):
        self.open_home_page()
        self.update_contact_by_id(id)
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector(f"input[value='{id}']").click()

    def update_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()

    def update_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector(f"a[href*='edit.php?id={id}']").click()

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
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.update_contact_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        middlename = wd.find_element_by_name('middlename').get_attribute('value')
        nickname = wd.find_element_by_name('nickname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        company = wd.find_element_by_name('company').get_attribute('value')
        title = wd.find_element_by_name('title').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        fax = wd.find_element_by_name('fax').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        homepage = wd.find_element_by_name('homepage').get_attribute('value')
        return Contact(id=id, firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                       title=title, company=company, address=address, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, fax=fax, email=email, email2=email2, email3=email3, homepage=homepage)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = re.search('H: (.*)', text).group(1)
        mobile_phone = re.search('M: (.*)', text).group(1)
        work_phone = re.search('W: (.*)', text).group(1)
        return Contact(id=id, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone)

    def add_contact_to_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name('to_group').click
        Select(wd.find_element_by_name('to_group')).select_by_value(group_id)
        wd.find_element_by_name('add').click()

    def remove_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        wd.find_element_by_xpath('group').click
        Select(wd.find_element_by_name('group')).select_by_value(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name('remove').click()


