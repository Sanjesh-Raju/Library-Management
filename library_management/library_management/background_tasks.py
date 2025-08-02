import frappe
import time

import frappe
from frappe.desk.doctype.notification_log.notification_log import enqueue_create_notification

import frappe
from frappe.desk.doctype.notification_log.notification_log import enqueue_create_notification

def notify_user(todo_name, assigned_by):
    todo = frappe.get_doc("ToDo", todo_name)
    user = todo.owner or "Administrator"
    from_user = assigned_by or frappe.session.user or "Administrator"

    # ✅ Correct order: users list, then notification dict
    enqueue_create_notification(
        [user],  # ✅ List of user IDs (not a document)
        {
            "type": "Alert",
            "document_type": "ToDo",
            "document_name": todo.name,
            "subject": f"New ToDo assigned: {todo.description}",
            "from_user": from_user
        }
    )








# def notify_user(todo_name, assigned_by):
#     todo = frappe.get_doc("ToDo", todo_name)
#     user = todo.owner

#     # Send a notification
#     frappe.publish_realtime(
#         event="msgprint",
#         message=f"You have a new ToDo: {todo.description}",
#         user=user
#     )

