# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DatabaseAPI(Document):
    def before_save(self):
        

        #-----------------------get_list
        # doc = frappe.db.get_list('Database API')
        # frappe.msgprint(f"this is a get_list: {doc}")

        #---------------------get_list(pluck)
        # doc1 = frappe.db.get_list('Database API', pluck='name')
        # frappe.msgprint(f"this is a get_list(pluck): {doc1}")

        #----------------------filtered list
        # doc2 = frappe.db.get_list(
        #     'Database API',
        #     filters={
        #         'status': 'Open'
        #     },
        #     fields=['name','subject', 'date'],
        #     order_by='date desc',
        #     start=1,
        #     page_length=3,
        #     as_list=True
        # )
        # frappe.msgprint(f"get_list: {doc2}")

#-------------------------------get_all

        # records = frappe.db.get_all('Database API', fields=['name', 'subject', 'date'])
        # frappe.msgprint(f"get_all: {records}")
        
        # records = frappe.db.get_all(
        #     'Database API',
        #     filters={
        #         'status': 'Open'
        #     },
        #     fields=['name', 'subject', 'date'],
        #     order_by='date desc',
        #     limit_page_length=3
        # )
        # frappe.msgprint(f"get_all: {records}")

#------------------------get_value
        # Get single value
        # subject = frappe.db.get_value('Database API', 'DB002', 'subject')
        # frappe.msgprint(f"Single subject: {subject}")

        # # Get multiple values
        # subject, date = frappe.db.get_value('Database API', 'DB002', ['subject', 'date'])
        # frappe.msgprint(f"Subject: {subject}, Date: {date}")

        # # Get values as dict
        # task_dict = frappe.db.get_value('Database API', 'DB002', ['subject', 'date'], as_dict=1)
        # frappe.msgprint(f"Dict Result → Subject: {task_dict.subject}, Date: {task_dict.date}")

        # # Get by filters (first match)
        # subject, date = frappe.db.get_value('Database API', {'status': 'Open'}, ['name1', 'date'])
        # frappe.msgprint(f"First Open → Subject: {name1}, Date: {date}")
        #timezone = frappe.db.get_single_value('System Settings', 'timezone')
        # frappe.msgprint(f" single doctype {timezone}")

#------------------------set_value
        # frappe.db.set_value('Database API', 'DB002', 'subject', 'Updated Subject',update_modified=False)
        
#------------------------exists

        # doc = frappe.db.exists("Database API", {"name1": "san"})
        # if doc:
        #         frappe.msgprint(f"Already exists: {doc}")
        
#------------------------count

        # doc=frappe.db.count('Database API', {'status': 'Open'})
        # frappe.msgprint(f"no.of.record:{doc}")
        
#------------------------delete

        # doc=frappe.db.delete('Database API', {'status': 'Open'})
        # frappe.msgprint(f"The record delete")
        
#------------------------truncate

        # frappe.db.truncate("Database API")
        # frappe.msgprint(f"all record the delete")
        
        # frappe.db.set_value('Database API', 'DB007', 'status', 'Open')
        # frappe.db.commit() 
        
        # result = frappe.db.sql("SELECT name, status FROM `tabTask` WHERE status=%s", ("Open",))
        # for row in result:
        #         frappe.msgprint(row[0], row[1])
        
        frappe.db.add_unique("Database API", "name1")




