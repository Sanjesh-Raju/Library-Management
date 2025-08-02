import frappe
from frappe import enqueue

def enqueue_notify(doc, method):
    enqueue(
        "library_management.library_management.background_tasks.notify_user",
        todo_name=doc.name,
        assigned_by=doc.assigned_by,
        queue="short"
    )