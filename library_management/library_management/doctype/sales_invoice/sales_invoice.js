frappe.ui.form.on("Sales Invoice", {
    refresh(frm) {
        frm.add_custom_button(__('Upload PDF to Google Drive'), function () {
           frappe.call({
    method: 'library_management.library_management.integrations.google_drive.upload_local_file_to_drive',
    args: {
        filename: 'example.pdf'  // just the filename in /public/files/
    },
    freeze: true,
    freeze_message: 'Uploading to Google Drive...',
    callback: function(r) {
        if (r.message && r.message.webViewLink) {
            frappe.msgprint(__('Uploaded! <a href="' + r.message.webViewLink + '" target="_blank">Open on Drive</a>'));
        } else {
            frappe.msgprint(__('Upload failed.'));
        }
    }
});

        });
    }
});

