from model.contact import Contact


def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.mod_first_contact(Contact(firstname='mod_name', lastname='mod_lname', nickname='mod_nick', title='mod_title', company='mod_company', address='mod_address', home_phone='mod_123321', email='mod_user@example.com', bday='31', bmonth='December', byear='2000'))
    app.session.logout()