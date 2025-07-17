// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt


frappe.ui.form.on("Realtime", {
    refresh: function(frm) {
        frappe.realtime.on('new_task_created', function(data) {
            frappe.msgprint(__('New Task Created: ') + data.task_name);
        });
    }
});
