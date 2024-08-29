from model.group import Group
import random


def test_mod_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name='test'))
    old_groups = db.get_group_list()
    group_choice = random.choice(old_groups)
    group = (Group(group_name="mod_group_name", group_header="mod_group_header", group_footer="mod_group_footer"))
    group.id = group_choice.id
    app.group.mod_group_by_id(group_choice.id, group)
    new_groups = db.get_group_list()
    old_groups = [group if x == group_choice else x for x in old_groups]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui is True:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


