from model.contact import Contact


def test_del_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname='test'))
    if app.contact.count() == 0:
        app.contact.create(contact)
    app.contact.del_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

