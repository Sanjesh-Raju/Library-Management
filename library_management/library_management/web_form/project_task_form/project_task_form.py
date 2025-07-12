import frappe
from frappe import _	
# def get_context(context):
# 	# do your magic here
# 	pass
def get_context(context):
    context.breadcrumbs = [
        {"label": _("Jobs"), "route": "library"}  
    ]
