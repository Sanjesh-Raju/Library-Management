import frappe
from frappe.model.document import Document

class DocumentAPI(Document):
        def before_save(self):
                new_doc = frappe.new_doc("Employee")
                new_doc.employee_name = "Inserted from Script"
                new_doc.insert(
                ignore_permissions=True,
                ignore_links=True,
                ignore_if_duplicate=True,
                ignore_mandatory=True
                )
                frappe.msgprint(f"Document inserted successfully: {new_doc.name}")
                
        
        

                
#---------get_doc
        # emp = frappe.get_doc("Employee", "EMP-005")
        # self.title = emp.employee_name
        # frappe.msgprint("title field is updated....")
#---------get_single_value
        # doc = frappe.db.get_single_value("System Settings", "time_zone")
        # frappe.msgprint(f"System timezone is {doc}")
#---------new_doc
        # doc1 = frappe.db.exists("Document API", "TK010")
        # if not doc1:
        #     doc2 = frappe.new_doc('Employee')
        #     doc2.employee_name = 'Test'
        #     doc2.insert()
        #     frappe.msgprint('Created Successfully!')
        # else:
        #     frappe.msgprint('Record exist?')
#----------get_doc|>
        # doc3 = frappe.get_doc({
        #     'doctype': 'Document API',
        #     'title': 'New Task'
        # })
        # doc3.insert()
        
        # doc4 = frappe.get_doc(
        #     doctype = 'Document API',
        #     title: 'New Task'
        # )
        # doc4.insert()

#--------------------get_last_doc 
        # doc5=frappe.get_last_doc('Document API')
        # frappe.msgprint(f"last_doc is {doc5}")
        
        # doc6 = frappe.get_last_doc('Document API', filters={"Status": "Cancelled"},order_by="modified desc")
        # frappe.msgprint(f"last_doc with filters is {doc6}")
        
#----------------------------delete_doc
        # doc7=frappe.delete_doc('Document API', 'TK003')
        # frappe.msgprint(f"last_doc with filters is TK003")
        
        # tasks= frappe.get_doc("Document API", "TK003")
        # frappe.delete_doc("Document API", tasks)
        # frappe.msgprint(f"{tasks}cancelled task deleted.")
#-------------rename_doc 
        # frappe.rename_doc('Document API', 'TK004', 'TK002')
        # frappe.msgprint("rename_doc")
#-------------get_meta
        # meta = frappe.get_meta('Document API')
        # meta1 = meta.has_field('status')               # boolean
        # frappe.msgprint(f"Does 'status' field exist? {meta1}")

        
        # meta = frappe.get_meta("Document API")
        # for field in meta.fields:
        #         print(field.fieldname, field.fieldtype)
                
        # meta = frappe.get_meta("Document API")

        # for perm in meta.permissions:
        #         frappe.msgprint(
        #         f"Role: {perm.role}, Level: {perm.permlevel}, "
        #         f"Read: {perm.read}, Write: {perm.write}, Create: {perm.create}, "
        #         f"Delete: {perm.delete}, Submit: {perm.submit}, Cancel: {perm.cancel}"
        #         )

#-----------------doc.insert

                # new_doc = frappe.new_doc("Employee")
                # new_doc.employee_name = "Inserted from Script"
                # new_doc.insert(
                # ignore_permissions=True,
                # ignore_links=True,
                # ignore_if_duplicate=True,
                # ignore_mandatory=True
                # )
                # frappe.msgprint(f"Document inserted successfully: {new_doc.name}")
                
#-------------------------------doc_save

                # doc = frappe.get_doc("Employee","EMP-014")
                # doc.employee_name = "Inserted"
                # doc.save(
                #         ignore_permissions=True, # ignore write permissions during insert
                #         ignore_version=True # do not create a version record
                #         )
                # frappe.msgprint(f"Document change successfully: {doc.name}")
                
#--------------------------------doc.delete()
                # doc = frappe.get_doc("Document API", "TK003")
                # doc.delete()
                # frappe.msgprint(f"TK003 Delete  successfully")

#--------------------------------.get_doc_before_save()
                # doc=frappe.get_doc("Document API","TK002")
                # old_doc = self.get_doc_before_save()
                # if old_doc.status == doc.status:
                #         frappe.msgprint("The status is Same")
                # else:
                #         frappe.msgprint("The status is not Same")
                
#------------------------------has_value_changed

                # if self.has_value_changed("status"):
                #         frappe.msgprint(f"Status changed from '{self.get_doc_before_save().status}' to '{self.status}'")
                
#---------------------------doc.reload()

                # doc = frappe.get_doc("Document API", "TK002")
                # doc.status = "Open"
                # doc.reload()
                # frappe.msgprint("doc_reload")

#--------------------------check_permission

                # doc = frappe.get_doc("Document API", "TK001")
                # # Check if current user has  permission
                # doc1=doc.check_permission(permtype='read') 
                # frappe.msgprint("Current user has read permission.")
                
#---------------------------get_title

                # doc = frappe.get_doc("Document API", "TK001")
                # frappe.msgprint(f"The document title is: {doc.get_title()}")
                
#---------------------------db_set

                # doc = frappe.get_doc("Employee", "EMP-014")
                # if doc:
                #         doc.db_set("status", 'Active')
                
#--------------------------doc.append

                        # doc = frappe.get_doc("Employee", "EMP-014")
                        # doc.append("document", {
                        # "item_name": "Sample Book",
                        # "quantity": 2,
                        # "price": 150
                        # })
                        # doc.save()
                        # frappe.db.commit()
                        # frappe.msgprint("Child row added successfully.")
                        
#-----------------------------

        # def say_hello(self):
        #         frappe.msgprint(f"Hello from {self.name}")
                
        # doc = frappe.get_doc("Document API", "TK001")
        # doc.run_method("say_hello")
























