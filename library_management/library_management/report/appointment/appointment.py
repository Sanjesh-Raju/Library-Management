# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart_data(data)
    report= get_report_summary(data)
    return columns, data, None, chart,report



def get_columns():
    return [
    {
				'fieldname':'patient',
				'label':_('patient'),
				'fieldtype':'Data'
				
			},
			{
				'fieldname':'doctor',
				'label':_('Doctor'),
				'fieldtype':'Data'
				
			},
			{
				'fieldname':'appointment_date',
				'label':_('Date'),
				'fieldtype':'Date'
			},
			{
				'fieldname':'status',
				'fieldtype':'Select',
				'label':_('Status'),
				'options':['','Scheduled','Cancelled']
			}
    ]



def get_data(filters):
    condition = "1=1"
    
    if filters.get("patient"):
        condition += f" AND A.patient LIKE '{filters.get('patient')}%'"

    if filters.get("doctor"):
        condition += f" AND A.doctor LIKE '{filters.get('doctor')}%'"

    if filters.get("appointment_date"):
        condition += f" AND A.appointment_date='{filters.get('appointment_date')}'"

    if filters.get("status"):
        condition += f" AND A.status='{filters.get('status')}'"
   
    query = f"""
        SELECT
            A.patient,
            A.doctor,
            A.appointment_date,
            A.status
           
        FROM
            `tabAppointment` A
        WHERE
            {condition}
        ORDER BY A.appointment_date DESC
    """
    
    return frappe.db.sql(query,as_dict=True)




def get_chart_data(data):
    status_count = {"Scheduled": 0, "Cancelled": 0}

    for entry in data:
        if entry.get("status") == "Scheduled":
            status_count["Scheduled"] += 1
        elif entry.get("status") == "Cancelled":
            status_count["Cancelled"] += 1

    chart = {
        "data": {
            "labels": ["Scheduled", "Cancelled"],
            "datasets": [
                {
                    "name": "Appointments",
                    "values": [status_count["Scheduled"], status_count["Cancelled"]]
                }
            ]
        },
        "type": "pie",
        "height": 300
    }

    return chart


def get_report_summary(data):
    scheduled, cancelled = 0, 0

    for entry in data:
        if entry.get("status") == "Scheduled":
            scheduled += 1
        elif entry.get("status") == "Cancelled":
            cancelled += 1

    return [
        {
            "value": scheduled,
            "indicator": "Green",
            "label": "Scheduled Appointments",
            "datatype": "Int"
        },
        {
            "value": cancelled,
            "indicator": "Red",
            "label": "Cancelled Appointments",
            "datatype": "Int"
        },
    ]
