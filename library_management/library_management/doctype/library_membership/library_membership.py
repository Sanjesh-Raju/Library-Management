# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

import frappe


class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")

        # get loan period and compute to_date by adding loan_period to from_date
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
    
    
    # your_app/your_app/library_membership/library_membership.py


    def after_insert(self):
        self.send_email()

    def send_email(self):
        recipient = "sanjesh@tridotstech.com"
        subject = f"Library Membership Created: {self.name}"
        message = f"""
        <p>Hello {self.full_name},</p>
        <p>Your library membership has been successfully created.</p>
        <p><strong>Member ID:</strong> {self.library_member}</p>
        <p><strong>Valid From:</strong> {self.from_date}</p>
        <p><strong>Valid Until:</strong> {self.to_date}</p>
        <br>
        <p>Thank you,<br>Library Team</p>
        """

        frappe.sendmail(
            recipients=[recipient],
            subject=subject,
            message=message,
            reference_doctype=self.doctype,
            reference_name=self.name
        )
