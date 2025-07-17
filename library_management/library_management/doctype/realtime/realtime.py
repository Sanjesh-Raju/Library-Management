
# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Realtime(Document):
    def before_save(self):
        # This will be triggered after a new Realtime document is inserted
        frappe.publish_realtime('new_task_created', {
            'task_name': self.name1
        })
