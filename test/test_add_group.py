# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application
from fixture.group import GroupHelper


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="group_name", group_header="group_header", group_footer="group_footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()

