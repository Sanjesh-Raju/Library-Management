# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DialogAPI(Document):
	pass


@frappe.whitelist()
def server_action(name):
        doc = frappe.get_doc('Dialog API', name)
        doc.delete()
        return f" Driver '{name}' deleted successfully."

