// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("leave management", {
	refresh(frm) {
        console.log("Leave Management refresh called");

        if (frm.doc.attached_file) {
            frm.add_custom_button(__('Download File'), () => {
                const url = `/api/method/library_management.library_management.doctype.leave_management.leave_management.download_file?docname=${encodeURIComponent(frm.doc.name)}`;
                window.open(url);
            });
        }
	},
});
