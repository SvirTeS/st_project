from model.contact import Contact
import random


def test_mod_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    contact = (Contact(firstname='mod_name', lastname='mod_lname', nickname='mod_nick', title='mod_title',
                company='mod_company', address='mod_address', home_phone='mod_123321', email='mod_user@example.com'))
    contact_choice = random.choice(old_contacts)
    app.contact.mod_contact_by_id(contact_choice.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts = [contact if x == contact_choice else x for x in old_contacts]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui is True:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

