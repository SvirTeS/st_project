from model.group import Group


def test_mod_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    app.group.mod_first_group(
        Group(group_name="mod_group_name", group_header="mod_group_header", group_footer="mod_group_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_mod_first_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    app.group.mod_first_group(Group(group_name="mod_group_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_mod_first_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(group_name='test'))
    app.group.mod_first_group(Group(group_header="mod_group_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)