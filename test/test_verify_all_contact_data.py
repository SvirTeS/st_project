import re
from random import randrange
from model.contact import Contact


def test_verify_all_contact_data(app, db):
    all_contacts_from_ui = app.contact.get_contact_list()
    all_contacts_from_db = db.get_contact_list()
    assert len(all_contacts_from_ui) == len(all_contacts_from_db)
    for contact_ui in all_contacts_from_ui:
        contact_db = next(filter(lambda c: c.id == contact_ui.id, all_contacts_from_db))
        assert contact_ui.firstname == contact_db.firstname.strip()
        assert contact_ui.lastname == contact_db.lastname.strip()
        assert contact_ui.address == contact_db.address.strip()
        assert contact_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_ui.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '', filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
