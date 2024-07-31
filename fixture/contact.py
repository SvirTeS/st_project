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
        wd = self.app.wd
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

    def del_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion group
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()

    def mod_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact data
        self.fill_contact_data(contact)
        # submit
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts
