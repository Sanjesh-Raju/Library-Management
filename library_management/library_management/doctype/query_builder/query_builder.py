# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# from frappe.model.utils.tree import get_descendants_of
# from frappe.query_builder.functions import Concat
# from frappe.query_builder.functions import Extract
# from frappe.query_builder.functions import Now
# from frappe.query_builder.functions import IfNull
# from frappe.query_builder.functions import Abs
# from pypika.functions import Count
# from pypika.functions import Sum
# from pypika.functions import Avg
# from pypika.functions import Min
# from pypika.functions import Max



class QueryBuilder(Document):
       pass	
#-----------------------------frappe.qb.get_query -------------------------
	# query = frappe.qb.get_query("User")
	# users = query.run(as_dict=True)
	# print(users)
 
	# query = frappe.qb.get_query("User", fields=["name", "email"])
	# users = query.run(as_dict=True)
	# print(users)
	# query = frappe.qb.get_query(
	# 	"User",
	# 	fields=["name as user_name", "email as user_email"]
	# 	)
	# users = query.run(as_dict=True)
    # print(users)


	# query = frappe.qb.get_query("User", fields=["name", "email"])
	# users = query.run(as_dict=True)
	# print(users)
	# query = frappe.qb.get_query("User", fields="name, email")
	# users = query.run(as_dict=True)
	# print(users)
	# query = frappe.qb.get_query("User", fields="*")
	# users = query.run(as_dict=True)
	# print(users)
    # query = frappe.qb.get_query(
    #     "User",
    #     fields=["name as user_name", "email as user_email"]
    # )
    # users = query.run(as_dict=True)
	# print(users)
 
 
# query = frappe.qb.get_query(
#     "Query Builder",
#     fields=["name", "name1.full_name as customer_name"],
#     filters={"name": "QB-001"}
# )
# so_data = query.run(as_dict=True)
# print(so_data)

# query = frappe.qb.get_query(
#     "Query Builder",
#     fields=["name", "items.item_code"],
#     filters={"name": "QB-001"}
# )
# so_items = query.run(as_dict=True)
# print(so_items)


# query = frappe.qb.get_query(
#     "Query Builder",
#     fields=[
#         "name",
#         {"items": ["item_code", "qty", "rate"]} 
#     ],
#     filters={"docstatus": 1},
#     limit=1
# )

# results = query.run(as_dict=True)
# print("hiiiiiiiiiiiiiiiiii",results)



# COUNT - Count rows or non-null values
from frappe.query_builder import DocType
from pypika.functions import Count

# Replace with your actual DocType
MyDoc = DocType("Query Builder")
query = (
    frappe.qb
    .from_(MyDoc)
    .select(
        Count(MyDoc.name).as_("name")
    )
    
)
result = query.run()
frappe.msgprint(str(result))


# query = (
#     frappe.qb
#     .from_(MyDoc)
#     .select(
#         Count(MyDoc.name)
#     )
# )

# result = query.run()
# frappe.msgprint(f"Total Records:{result[0][0]}")

# # COUNT(*) - Count all rows including nulls
# query = frappe.qb.get_query(
#     "Sales Invoice",
#     fields=[{"COUNT": "'*'", "as": "total_invoices"}]
# )

# # SUM - Calculate sum of numeric values
# query = frappe.qb.get_query(
#     "Sales Invoice",
#     fields=[{"SUM": "grand_total", "as": "total_sales"}],
#     filters={"docstatus": 1}
# )

# # AVG - Calculate average of numeric values
# query = frappe.qb.get_query(
#     "Sales Invoice",
#     fields=[{"AVG": "grand_total", "as": "avg_invoice_amount"}],
#     group_by="customer"
# )

# # MAX - Find maximum value
# query = frappe.qb.get_query(
#     "User",
#     fields=[{"MAX": "creation", "as": "latest_user_date"}]
# )

# # MIN - Find minimum value
# query = frappe.qb.get_query(
#     "User",
#     fields=[{"MIN": "creation", "as": "earliest_user_date"}]
# )
