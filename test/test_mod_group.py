from model.group import Group
import random


def test_mod_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name='test'))
    old_groups = db.get_group_list()
    group_choice = random.choice(old_groups)
    group = (Group(group_name="mod_group_name", group_header="mod_group_header", group_footer="mod_group_footer"))
    app.group.mod_group_by_id(group_choice.id, group)
    new_groups = db.get_group_list()
    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


