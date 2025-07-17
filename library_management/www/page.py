# In library_management/www/my_page.py

import frappe

def get_context(context):
    context.doctype = frappe.form_dict.get("doctype")
    return context
