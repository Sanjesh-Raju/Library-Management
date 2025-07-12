# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date

class ProjectTask(Document):
    # def before_save(self):
    #     self.task_name = 'SANJESH'

    #     if self.status == 'Open':
    #         self.description = 'New Description'
    #         self.start_date=date.today()
    #     else:
    #         self.description =""
    #         self.start_date=""

    # def after_insert(self):
    #     frappe.msgprint(f"created task name:{self.task_name}")

    # def before_insert(self):
    #     self.status = "Open"

    # def validate(self):
    #     if not self.end_date:
    #         frappe.throw("fill the End Date")
    #         frappe.msgprint("")

    # # def before_submit(self):
    # #     if self.status != "Completed":
    # #         frappe.throw("Only completed tasks can be submitted.")

    # def after_submit(self):
    #     frappe.msgprint("Task is submitted.")

    # def before_cancel(self):
    #     if self.status == "Completed":
    #         frappe.throw("Completed tasks cannot be canceled.") 
    # def after_cancel(self):
    #     frappe.msgprint("Task  has been canceled.")
        
    # def after_delete(self):
    #     frappe.throw(" delete a task in progress.")
        
    def before_print(self, print_settings):
        frappe.throw(" printing a task in progress.")

import frappe
from frappe import _

@frappe.whitelist()
def create_task(task_name=None,status=None):
    doc = frappe.get_doc({
        "doctype": "Project Task",
        "task_name": task_name,
        "status": status
    })
    doc.insert()
    frappe.db.commit()
    return doc

@frappe.whitelist()
def get_task():
    tasks = frappe.get_all(
        "Project Task",
        fields=["*"]
    )
    return tasks

@frappe.whitelist()
def update_task(name, status):
    doc = frappe.get_doc("Project Task", name)
    doc.status = status
    doc.save()
    return doc

@frappe.whitelist()
def delete_task(name):
    frappe.delete_doc("Project Task", name)
    return {"status": "deleted", "name": name}

