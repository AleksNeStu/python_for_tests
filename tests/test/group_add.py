#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group add module"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixture.application import Application
from tests.generator.generic import random_data as r_data
from tests.model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name=r_data("name_", 5), header=r_data("header_", 5),
                           footer=r_data("footer_", 5)))
    app.session.logout()


# def test_add_group_empty(app):
#     app.login(app.login_data)
#     app.create_group(app.group_data_empty)
#     app.logout()