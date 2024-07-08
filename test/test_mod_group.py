from model.group import Group


def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(group_name="mod_group_name", group_header="mod_group_header", group_footer="mod_group_footer"))
    app.session.logout()