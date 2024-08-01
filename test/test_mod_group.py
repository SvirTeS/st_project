from model.group import Group
from random import randrange


def test_mod_some_group(app):
    old_groups = app.group.get_group_list()
    group = (Group(group_name="mod_group_name", group_header="mod_group_header", group_footer="mod_group_footer"))
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    app.group.mod_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_mod_some_group_name(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(group_name="mod_group_name"))
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    app.group.mod_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_mod_some_group_header(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(group_name="mod_group_name"))
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    app.group.mod_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
