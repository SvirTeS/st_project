# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname='Name', lastname='LastName', nickname='nick', title='title', company='company', address='city17', home_phone='123456', email='email@example.com', bday='1', bmonth='January', byear='1990'))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname='', lastname='', nickname='', title='', company='', address='', home_phone='', email='', bday='', bmonth='-', byear=''))


