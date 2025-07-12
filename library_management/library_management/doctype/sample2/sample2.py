# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Sample2(Document):
    pass
@frappe.whitelist()
def fetch_sample1_data(unique):
    if unique:
        sample1_doc = frappe.get_doc("Sample1", unique)
        return {
            "full_name": sample1_doc.full_name,
            "phone": sample1_doc.phone
        }
