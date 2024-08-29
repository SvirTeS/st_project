from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(Contact(firstname='test'))
    if orm.get_group_list() == 0:
        app.group.create(Group(group_name='test'))
    groups_list = orm.get_group_list()
    group_choice = random.choice(groups_list)
    contacts_list = orm.get_contacts_not_in_group(group_choice)
    contact_choice = random.choice(contacts_list)
    contact_choice_id = contact_choice.id
    app.contact.add_contact_to_group_by_id(contact_choice.id, group_choice.id)
    contacts_in_group = orm.get_contacts_in_group(group_choice)
    assert any(c.id == contact_choice_id for c in contacts_in_group)


def test_remove_contact_from_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(Contact(firstname='test'))
    if orm.get_group_list() == 0:
        app.group.create(Group(group_name='test'))
    groups_list = orm.get_group_list()
    group_choice = random.choice(groups_list)
    contacts_list = orm.get_contact_list()
    contact_choice = random.choice(contacts_list)
    contact_choice_id = contact_choice.id
    app.contact.remove_contact_from_group_by_id(contact_choice.id, group_choice.id)
    contacts_in_group = orm.get_contacts_in_group(group_choice)
    assert any(c.id != contact_choice_id for c in contacts_in_group)