// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.query_reports["Library Report"] = {
	"filters": [
		{
                'fieldname': 'article',
                'label': __('Article'),
                'fieldtype': 'Link',
                'options': 'Article',
            },
			{
				'fieldname':'library_member',
				'label':__('Library Member'),
				'fieldtype':'Link',
				'options':'Library Member',
			},
			{
				'fieldname':'type',
				'label':__('Status'),
				'fieldtype':'Select',
				'options':['','Issue','Return'],
			},
			{
				'fieldname':'date',
				'label':__('Date'),
				'fieldtype':'Date',
			},
			{
				'fieldname':'from_date',
				'fieldtype':'Date',
				'label':__('Membership From Date')
			},
			{
				'filename':'to_date',
				'fieldtype':'Date',
				'label':__('Membership To Date')
			}
	]
};
