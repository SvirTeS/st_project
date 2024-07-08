class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def init_group_creation(self):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_name("new").click()

    def init_first_group_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()

    def create(self, group):
        wd = self.app.wd
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

    def submit_group_creation(self):
        wd = self.app.wd
        # submit group create
        wd.find_element_by_name("submit").click()

    def submit_group_edition(self):
        wd = self.app.wd
        # submit group create
        wd.find_element_by_name("update").click()

    def return_group_page(self):
        wd = self.app.wd
        # return group page
        wd.find_element_by_link_text("group page").click()

    def del_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion group
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def mod_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.init_first_group_edition()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        self.submit_group_edition()
        self.return_group_page()
