from model.contact import Contact


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test', bday='31', bmonth='December', byear='2000'))
    app.contact.mod_first_contact(
        Contact(firstname='mod_name', lastname='mod_lname', nickname='mod_nick', title='mod_title',
                company='mod_company', address='mod_address', home_phone='mod_123321', email='mod_user@example.com',
                bday='31', bmonth='December', byear='2000'))


def test_mod_first_contact_firstname_and_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test', bday='31', bmonth='December', byear='2000'))
    app.contact.mod_first_contact(Contact(firstname='mod_name', bday='31', bmonth='December', byear='2000'))