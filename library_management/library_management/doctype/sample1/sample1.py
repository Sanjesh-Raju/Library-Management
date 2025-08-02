# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Sample1(Document):
	pass
# user = frappe.get_doc("User", "k7@gamil.com") 
# user.language = "fr"
# user.save()
# frappe.db.commit()
# frappe.msgprint(f"Language set to {user.language} for user {user.name}")

#--------------Form Dict: _lang 
# ?_lang=fr
#-------------Cookie: preferred_language 
# preferred_language =fr