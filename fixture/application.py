from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        elif browser == 'firefox':
            self.wd = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        elif browser == 'safari':
            self.wd = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
