// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.query_reports["Appointment"] = {
	"filters": [
		{
				'fieldname':'patient',
				'label':__('patient'),
				'fieldtype':'Data'
				
			},
			{
				'fieldname':'doctor',
				'label':__('Doctor'),
				'fieldtype':'Data'
				
			},
			{
				'fieldname':'appointment_date',
				'label':__('Date'),
				'fieldtype':'Date'
			},
			{
				'fieldname':'status',
				'fieldtype':'Select',
				'label':__('Status'),
				'options':['','Scheduled','Cancelled']
			}

	]
};
