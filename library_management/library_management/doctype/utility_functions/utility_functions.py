# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import *
from frappe.utils.pdf import get_pdf
from datetime import datetime          

class UtilityFunctions(Document):
    def before_save(self):
       
        # a=now()
        # frappe.msgprint(f"Now:{a}")
        
        # a=getdate()
        # frappe.msgprint(f"getdate:{a}")
        
        # a=today()
        # frappe.msgprint(f"today:{a}")
        
        # date=getdate()
        # a=add_to_date(date, years=10, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0, as_string=False, as_datetime=False)
        # frappe.msgprint(f"today:{a}")
        
        # date_1 = today()
        # date_2 = add_to_date(date_1, days=10)
        # date=date_diff(date_2, date_1)
        # date=days_diff(date_2, date_1)
        # date=month_diff(date_2, date_1)
        # frappe.msgprint(f"date_diff:{date}")
        
        # a=pretty_date(now()) 
        # frappe.msgprint(f"pretty_date:{a}")
        
        # a=format_duration(50) # '50s'
        # b=format_duration(10000) # '2h 46m 40s'
        # c=format_duration(1000000) # '11d 13h 46m 40s'
		# # Convert days to hours
  		# d=format_duration(1000000, hide_days=True) # '277h 46m 40s'
        # frappe.msgprint(f"format_duration:{(a,b,c,d)}")
        
        # a=comma_and([1, 2, 3]) # "'1', '2' and '3'"
        # b=comma_and(['Apple', 'Ball', 'Cat'], add_quotes=False) # 'Apple, Ball and Cat'
        # c=comma_and('abcd') # 'abcd'
        # frappe.msgprint(f"comma_and:{(a,b,c)}")
        
        # a=money_in_words(900) # 'INR Nine Hundred and Fifty Paisa only.'
        # b=money_in_words(900.50) # 'INR Nine Hundred and Fifty Paisa only.'
        # c=money_in_words(900.50, 'USD') # 'USD Nine Hundred and Fifty Centavo only.'
        # d=money_in_words(900.50, 'USD', 'Cents') # 'USD Nine Hundred and Fifty Cents only.'
        # frappe.msgprint(f"money_in_words:{(a,b,c,d)}")
        
        # a=random_string(40) # 'mcrLCrlvkUdkaOe8m5xMI8IwDB8lszwJsWtZFveQ'
        # b=random_string(6) # 'htrB4L'
        # c=random_string(6) #'HNRirG'
        # frappe.msgprint(f"random_string:{(a,b,c)}")
        
        # a=unique([1, 2, 3, 1, 1, 1])
        # b=unique('abcda') 
        # c=unique(('Apple', 'Apple', 'Banana', 'Apple'))
        # frappe.msgprint(f"unique:{(a,b,c)}")
        
        # a=get_abbr('Gavin') 
        # b=get_abbr('Coca Cola Company') 
        # c=get_abbr('Mohammad Hussain Nagaria', max_len=3) 
        # frappe.msgprint(f"get_abbr:{(a,b,c)}")
        
        # a=validate_url('google') # False
        # b=validate_url('https://google.com') # True
        # c=validate_url('https://google.com', throw=True) # throws ValidationError
        # frappe.msgprint(f"validate_url:{(a,b)}")
        
        # a=validate_email_address('sample@erpnext.com')
        # b=validate_email_address('other text, sample@erpnext.com, some other text') 
        # d=validate_email_address('some other text') 
        # frappe.msgprint(f"validate_email_address:{(a,b,d)}")
        
        # a=validate_phone_number('753858375') 
        # b=validate_phone_number('+91-75385837') 
        # c=validate_phone_number('invalid') 
        # d=validate_phone_number('87345%%', throw=True)
        # frappe.msgprint(f"validate_phone_number:{(a,b,c)}")
        
        # cache = frappe.cache()
        # cache.set('name', 'frappe') 
        # cache.get('name')
        # frappe.msgprint(f"cache:{cache}")
        pass
        


@frappe.whitelist(allow_guest=True)

def utl():
    booking = {
        'Bajaj': 'RS200',
        'KTM': 'RC200',
        'Ninja': 'H2r',
        'Yamaha': 'R15',
        'Honda': 'CBR150'
    }

    html = '<h1>Welcome to Sundar Bikes</h1><ol>'
    for company, bike in booking.items():
        html += f'<li>{company} - {bike}</li>'
    html += '</ol>'

    pdf = get_pdf(html)
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    file_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": f"invoice_{timestamp}.pdf",
        "content": pdf,
        "is_private": 0
    }).insert(ignore_permissions=True)

    return file_doc.file_url    