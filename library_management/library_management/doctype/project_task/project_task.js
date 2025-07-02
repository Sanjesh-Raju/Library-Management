frappe.ui.form.on("Project Task", {
	refresh(frm) {
        frm.add_custom_button('Show Notes', function () {
            frappe.call({
                method: "library_management.library_management.doctype.project_task.project_task.get_notes", 
                callback: function (r) {
                    if (r.message && Array.isArray(r.message)) {
                        
                        frappe.msgprint({
                            title: __('Notification'),
                            indicator: 'green',
                            message: __('Document updated successfully:<br>') +  r.message
                            .map(note => `Task: ${note.task_name} | Status: ${note.status}`)
                            .join('<br>')
                        });
                        console.log(r.message);
                    } else {
                        frappe.msgprint("No notes found.");
                    }
                }
            });
        });
    }
});


