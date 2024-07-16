from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test', bday='31', bmonth='December', byear='2000'))
    app.contact.del_first_contact()

