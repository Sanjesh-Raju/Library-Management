// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Utilities API", {
    refresh(frm) {
// ---------------->frappe.get_route 
        frm.add_custom_button('Show Route', () => {
            const route = frappe.get_route();
            console.log(route);

        })
//---------------->frappe.set_route 
        frm.add_custom_button('Go to Task List', () => {
            frappe.set_route('List', 'article',{ article_name: 'Harry Potters' });
        });

    frm.add_custom_button('Go to New Article', () => {
    frappe.new_doc('Article');
});

        frm.add_custom_button('Go to Task ', () => {
            frappe.set_route('Form', 'article','Harry Potters');
        
        });
        
        frm.add_custom_button('Go to Tasksss ', () => {
            frappe.set_route('List/article/calender');
        });
    
//---------------->frappe.format 

let currency = frm.doc.currency; 
let formatted_currency = frappe.format(currency, { fieldtype: 'Currency' });
frappe.msgprint(`Employee's salary is: ${formatted_currency}`);

//---------------->frappe.provide 
        
frm.add_custom_button('frappe provide', () => {
        let a = 20;
        let b = 10;
        let result = add_numbers(a, b);
        frappe.msgprint("result:" + result)
    });

    }
});

//---------------->frappe.require

frappe.require('/assets/library_management/js/web.js', () => {
})