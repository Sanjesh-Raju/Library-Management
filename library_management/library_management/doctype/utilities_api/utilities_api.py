# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UtilitiesAPI(Document):
	pass


def show_test_message():
    frappe.log_error("This is a scheduled message from show_test_message()", "Scheduled Task")
