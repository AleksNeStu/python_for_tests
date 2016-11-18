#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class GroupHelper:
    """Class for represent Group."""
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        """Open group page."""
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        """Return to group page from another tab."""
        wd = self.app.wd
        # wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text :
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        """Fill group forms of new data or modify exist data."""
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def select_first_group(self):
        """Select first group."""
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def create(self, group):
        """Create group filling requirements fields."""
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        """Modify group editing requirements fields."""
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        """Delete first group on the group page."""
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def delete_all_groups(self):
        """Delete all groups on the group page."""
        wd = self.app.wd
        self.open_groups_page()
        # check that the group's list is not empty and check group elements
        if len(wd.find_elements_by_css_selector("#content input")) == 6:
            pass
        else:
            # check group's elements
            elements = wd.find_elements_by_name("selected[]")
            for i in range(1, len(elements)+1):
                wd.find_element_by_css_selector("#content input:nth-of-type({})".
                                                format(i+3)).click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()