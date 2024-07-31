from model.contact import Contact


def test_mod_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname='mod_name', lastname='mod_lname', nickname='mod_nick', title='mod_title',
                company='mod_company', address='mod_address', home_phone='mod_123321', email='mod_user@example.com'))
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    app.contact.mod_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_mod_first_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname='mod_name'))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    app.contact.mod_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
