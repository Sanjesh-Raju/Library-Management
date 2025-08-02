# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class leavemanagement(Document):
	pass

# import frappe

# @frappe.whitelist()
# def download_file(name):
#     # Fetch the File document by name (DocType 'File')
#     file_doc = frappe.get_doc("File", name)

#     # Set filename for download
#     frappe.response.filename = file_doc.file_name

#     # Get the file content (this returns the file binary content)
#     frappe.response.filecontent = file_doc.get_content()

#     # Set the response type to 'download' which triggers the download response handler
#     frappe.response.type = "download"

#     # Optional: Set display content disposition
#     # "attachment" means the browser will download the file
#     # "inline" means the browser may display it (for PDFs, images, etc.)
    # frappe.response.display_content_as = "attachment"

@frappe.whitelist()
def download_file(docname):
    doc = frappe.get_doc("Sample1", docname)
    file_url = doc.attached_file
    if not file_url:
        frappe.throw(_("No file attached to this document"))
    file_doc = frappe.get_doc("File", {"file_url": file_url})
    if not file_doc:
        frappe.throw(_("File record not found"))
    frappe.response.filename = file_doc.file_name
    frappe.response.filecontent = file_doc.get_content()
    frappe.response.type = "download"
    frappe.response.display_content_as = "attachment"
