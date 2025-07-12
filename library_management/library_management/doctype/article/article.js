// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt





frappe.ui.form.on('Article', {
    items_remove(frm, cdt, cdn) {
        if(!confirm("Are you sure you want to delete this row?")) {
            // Prevent removal - tricky in Frappe as removal is already done here,
            // so best to override grid behavior or use validations before save.
        }
    }
});
