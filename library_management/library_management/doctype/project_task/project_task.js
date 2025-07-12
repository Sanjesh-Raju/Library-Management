// frappe.ui.form.on("Project Task", {
// 	refresh(frm) {
//         frm.add_custom_button('Show Notes', function () {
//             frappe.call({
//                 method: "library_management.library_management.doctype.project_task.project_task.get_notes", 
//                 callback: function (r) {
//                     if (r.message && Array.isArray(r.message)) {

//                         frappe.msgprint({
//                             title: __('Notification'),
//                             indicator: 'green',
//                             message: __('Document updated successfully:<br>') +  r.message
//                             .map(note => `Task: ${note.task_name} | Status: ${note.status}`)
//                             .join('<br>')
//                         });
//                         console.log(r.message);
//                     } else {
//                         frappe.msgprint("No notes found.");
//                     }
//                 }
//             });
//         });
//     }
// });

// // frappe.ui.form.on('Project Task', {
// //     refresh: function(frm) {
// //         frappe.msgprint(__('Form has been refreshed'));
// //         frm.add_custom_button(__('Refresh Form'), function() {
// //             frm.reload_doc();  
// //         });
// //     }
// // });

frappe.ui.form.on('Project Task', {
    refresh: function(frm) {
        frm.add_custom_button(__('Refresh Form'), function() {
            frm.reload_doc();
            frappe.msgprint('Refresh!');
        }, __('Actions'));

        frm.add_custom_button(__('Say Hello'), function() {
            frappe.msgprint('Hello!');
        }, __('Actions'));

        frm.add_custom_button(__('Custom Alert'), function() {
            frappe.show_alert('This is a custom alert!');
        
        }, __('Actions'));
    }
});

frappe.ui.form.on('Project Task', {
    refresh: function(frm) {
        const group = __('Actions');

        frm.add_custom_button(__('Go to Customer List'), function() {
            frappe.set_route(['List', 'Article']);
        }, group);

        frm.add_custom_button(__('add New Article'), function() {
            frappe.set_route(['Form', 'Article']);
            frappe.new_doc('Article');
        }, group);

        frm.add_custom_button(__('Open Specific Task'), function() {
            frappe.set_route(['Form', 'Project Task', 'TASK-0001']);
        }, group);
    }
});

// frappe.ui.form.on('Project Task', {
//     refresh(frm) {
//         frm.add_custom_button(__('Create Task'), function() {
//             frappe.prompt([
//                 {
//                     label: 'Task Name',
//                     fieldname: 'task_name',
//                     fieldtype: 'Data',
//                     reqd: 1
//                 },
//                 {
//                     label: 'Status',
//                     fieldname: 'status',
//                     fieldtype: 'Select',
//                     options: ['Open', 'In Progress', 'Completed'],
//                     default: 'Open'
//                 }
//             ], function(values) {
//                 frappe.call({
//                     method: "library_management.library_management.doctype.project_task.project_task.create_task",  
//                     args: {
//                         task_name: values.task_name,
//                         status: values.status
//                     },
//                     callback: function(response) {
//                         if (response.message) {
//                             frappe.msgprint("Task created");
//                         }
//                     }
//                 });
//             }, 'Enter Task Details', 'Create');
//         });
//     }
// });

frappe.ui.form.on('Project Task', {
    refresh(frm) {
        frm.add_custom_button(__('Create Task1'), function() {
            frappe.call({
                method: "library_management.library_management.doctype.project_task.project_task.create_task",  
                args: {
                    task_name: "My New Task",
                    status: "Open"
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint("Task created: " + response.message);
                    }
                }
            });
        });
    }
});

