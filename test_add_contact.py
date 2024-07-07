# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(firstname='Name', lastname='LastName', nickname='nick', title='title', company='company', address='city17', home_phone='123456', email='email@example.com', bday='1', bmonth='January', byear='1990'))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(firstname='', lastname='', nickname='', title='', company='', address='', home_phone='', email='', bday='', bmonth='-', byear=''))
    app.logout()

