# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data =get_columns(),get_data(filters)
	return columns, data


def get_columns():
	columns=[
		{
            'fieldname': 'article',
            'fieldtype': 'Link',
            'label': _('Article'),
            'options': 'Article',
        },
		{
			'fieldname':'library_member',
			'fieldtype':'Link',
			'label':_('Library Member'),
			'options':'Library Member',
		},
		{
			'fieldname':'type',
			'fieldtype':'Select',
			'label':'Status',
			'options':['Issue','Return'],
		},
		{
			'fieldname':'date',
			'fieldtype':'Date',
			'label':'Date',
		},
        {
			'fieldname':'from_date',
			'fieldtype':'Date',
			'label':'Membership From Date',
		},
        {
			'fieldname':'to_date',
			'fieldtype':'Date',
			'label':'Membership To Date',
		}, {
			'fieldname':'noofbook',
			'fieldtype':'Int',
			'label':'No.of.book',
		}
	]
	return columns	

def get_data(filters):
    condition = 'L.docstatus = 1'
    
    if filters.get("article"):
        condition += f" AND L.article='{filters.get('article')}'"

    if filters.get("library_member"):
        condition += f" AND L.library_member='{filters.get('library_member')}'"

    if filters.get("type"):
        condition += f" AND L.type='{filters.get('type')}'"

    if filters.get("date"):
        condition += f" AND L.date='{filters.get('date')}'"
    if filters.get("from_date"):
        condition += f" AND M.from_date>='{filters.get('from_date')}'"
    if filters.get("to_date"):
        condition += f" AND M.to_date<='{filters.get('to_date')}'"
    if filters.get("noofbook"):
    
        condition += f" AND PD.noofbook='{filters.get('noofbook')}'"
    query = f"""
	SELECT
		L.article,
		L.library_member,
		L.type,
		L.date,
		M.from_date,
		M.to_date,
		PD.noofbook
	FROM
		`tabLibrary Transaction` L
	JOIN
		`tabLibrary Membership` M ON L.library_member = M.library_member
	LEFT JOIN
		`tabArticle` A ON L.article = A.name
	LEFT JOIN
		`tabproduct detail` PD ON PD.parent = A.name
	WHERE
		{condition}
	ORDER BY L.date DESC

"""

    return frappe.db.sql(query)

