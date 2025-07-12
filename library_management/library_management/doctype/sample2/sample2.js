// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt
frappe.ui.form.on('Sample2', {
    before_submit: function(frm) {
        if (frm.doc.unique) {
            frappe.call({
                method: "library_management.library_management.doctype.sample2.sample2.fetch_sample1_data",
                args: {
                    unique: frm.doc.unique
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value("full_name", r.message.full_name);
                    
                        frm.set_value("phone", r.message.phone);
                    }
                }
            });
        }
    }
});

