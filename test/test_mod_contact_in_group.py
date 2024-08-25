from model.contact import Contact
from model.group import Group
import fixture.orm
import random


def test_add_contact_in_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    contacts_list = db.get_contact_list()
    groups_list = db.get_group_list()
    contact_choice = random.choice(contacts_list)
    group_choice = random.choice(groups_list)
    app.contact.add_contact_to_group_by_id(contact_choice.id, group_choice.id)
    #assert any(c.id == contact_choice.id for c in fixture.orm.ORMFixture.get_contacts_in_group(group_choice))


def test_remove_contact_from_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    contacts_list = db.get_contact_list()
    groups_list = db.get_group_list()
    contact_choice = random.choice(contacts_list)
    group_choice = random.choice(groups_list)
    app.contact.remove_contact_from_group_by_id(contact_choice.id, group_choice.id)



