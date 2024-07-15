from model.group import Group


def test_mod_first_group(app):
    app.group.mod_first_group(
        Group(group_name="mod_group_name", group_header="mod_group_header", group_footer="mod_group_footer"))


def test_mod_first_group_name(app):
    app.group.mod_first_group(Group(group_name="mod_group_name"))


def test_mod_first_group_header(app):
    app.group.mod_first_group(Group(group_header="mod_group_header"))
