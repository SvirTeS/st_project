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

    def fill_group_data(self, group):
        wd = self.app.wd
        # fill group form
        self.change_group_fill_value('group_name', group.group_name)
        self.change_group_fill_value('group_header', group.group_header)
        self.change_group_fill_value('group_footer', group.group_footer)

    def change_group_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.init_group_creation()
        self.fill_group_data(group)
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
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion group
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def mod_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.init_first_group_edition()
        self.fill_group_data(group)
        self.submit_group_edition()
        self.return_group_page()

