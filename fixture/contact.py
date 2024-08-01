from selenium.webdriver.support.select import Select
from model.contact import Contact


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
            allrows = wd.find_elements_by_css_selector("tr[name='entry']")
            for row in allrows:
                cells = row.find_elements_by_tag_name("td")
                checkbox = cells[0].find_element_by_tag_name("input")
                id = checkbox.get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
