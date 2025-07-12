# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class StudentMarks(Document):
	pass

import frappe

@frappe.whitelist()
def student_marks(student_name, subject_name, marks, status):
    message = f"Student: {student_name}, Subject: {subject_name}, Marks: {marks}, Status: {status}"
    frappe.log_error(message, "Student Marks Submission")
    return f"Received marks for {student_name} in {subject_name}: {marks} ({status})"



