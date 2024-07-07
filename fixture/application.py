from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.wd.implicitly_wait(30)

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

    def add_contact(self, contact):
        wd = self.wd
        self.open_page_to_add_contact()
        # fill contact data
        # input name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # input last name
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # input nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # input title
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # input company
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # input address
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # input home_phone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # input email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # input bday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # save data
        wd.find_element_by_name("submit").click()

    def open_page_to_add_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()