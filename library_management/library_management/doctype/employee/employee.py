# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee(Document):
    pass
@frappe.whitelist()
def func1():
	frappe.msgprint("This fuction is worked")

