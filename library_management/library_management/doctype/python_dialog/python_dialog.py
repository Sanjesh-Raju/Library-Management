import frappe
from frappe.model.document import Document

class PythonDialog(Document):
#     def before_save(self):
#         # Simple message
#       #   frappe.msgprint("This is a simple message.")

#       #   # Message with title
#       #   frappe.msgprint(msg="Operation successful.", title="Success")

#       #   # Message with a list
#       #   frappe.msgprint(
#       #       msg=["Item A created", "Item B updated"],
#       #       title="Results",
#       #       as_list=True
#       #   )

#       #   # Manually format as HTML table
#       #   table_html = """
#       #   <table class="table table-bordered">
#       #       <thead>
#       #           <tr><th>Item</th><th>Status</th></tr>
#       #       </thead>
#       #       <tbody>
#       #           <tr><td>Item A</td><td>Created</td></tr>
#       #           <tr><td>Item B</td><td>Updated</td></tr>
#       #       </tbody>
#       #   </table>
#       #   """

#       #   frappe.msgprint(
#       #       msg=table_html,
#       #       title="Detailed Results",
#       #       wide=True
#       #   )
#       #   frappe.msgprint(
#       #       msg="""
#       #           <p>Backup completed successfully.</p>
#       #           <a href="/app/article" class="btn btn-primary" style="margin-top:10px;">View Logs</a>
#       #       """,
#       #       title="Backup Status",
#       #       indicator="green",
#       #       wide=True
#       #   )
        
#        frappe.msgprint(
#     msg="Would you like to create a backup?",
#     title="Backup",
#     primary_action={
#         "label": "Create Backup",
#         "server_action": "library_management.library_management.doctype.sensor_data.sensor_data.create_sensor_record",
#         "hide_on_success": True
#     }
    
# )  


    def before_save(self):
        # 1️⃣ Basic message
        # frappe.throw("This is a basic error message.")

        # 2️⃣ Custom exception class
        # frappe.throw(
        #     msg="This is a validation error.",
        #     exc=frappe.ValidationError
        # )

        # # 3️⃣ Custom title
        # frappe.throw(
        #     msg="You are not allowed to do this.",
        #     title="Permission Denied"
        # )

        # 4️⃣ Minimize the message box
        frappe.throw(
            msg="This message can be minimized.",
            title="Minimizable Error",
            is_minimizable=True
        )

        # # 5️⃣ Wide message box
        # frappe.throw(
        #     msg="This message box is wider than usual.",
        #     title="Wide Error",
        #     wide=True
        # )

        # # 6️⃣ Message as a list
        # frappe.throw(
        #     msg=[
        #         "Field A is required.",
        #         "Field B must be greater than 0.",
        #         "Field C must be unique."
        #     ],
        #     title="Validation Failed",
        #     as_list=True
        # )

        # # 7️⃣ Primary action (with a global client-side JavaScript function)
        # frappe.throw(
        #     msg="An error occurred during backup.",
        #     title="Backup Error",
        #     primary_action={
        #         "label": "Retry Backup",
        #         "server_action": "library_management.library_management.doctype.sensor_data.sensor_data.create_sensor_record",
        #         "hide_on_success": True
        #     }
        # )





