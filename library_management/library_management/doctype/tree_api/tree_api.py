# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet
from frappe.model.document import Document


class TreeAPI(NestedSet):
    def autoname(self):
        if self.member_name:
            self.name = self.member_name
 
@frappe.whitelist()
def get_children(parent=None):
    return frappe.get_list(
        "Tree API",
        fields=["name", "member_name as title", "is_group"],
        filters={"parent_tree_api": parent or ""}
    )

 
@frappe.whitelist()
def add_node(parent=None, member_name=None, age=None, gender=None, relation=None, is_group=0):
    doc = frappe.get_doc({
        "doctype": "Tree API",
        "member_name": member_name,
        "age": age,
        "gender": gender,
        "relation": relation,
        "parent_tree_api": parent,
        "is_group": int(is_group) 
    })
    doc.insert()
    return doc