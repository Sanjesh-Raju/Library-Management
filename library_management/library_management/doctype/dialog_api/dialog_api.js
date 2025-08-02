frappe.ui.form.on("Dialog API", {
    refresh(frm) {
        frm.add_custom_button('Dialog API', () => {
            let d = new frappe.ui.Dialog({
                title: 'Driver Details',
                fields: [
                    { label: 'First Name', fieldname: 'first_name', fieldtype: 'Data', reqd: 1 },
                    { label: 'Last Name', fieldname: 'last_name', fieldtype: 'Data', reqd: 1 },
                ],
                size: 'small',
                primary_action_label: 'Submit',
                primary_action: (values) => {
                    console.log("Driver details:", values);
                    frm.set_value('first_name', values.first_name);
                    frm.set_value('last_name', values.last_name);

                    d.hide();
                }
            });
            d.show();
        });

//         frappe.msgprint({
//     title: __('Notification'),
//     indicator: 'green',
//     message: __('Testing Work successfully')
// });

// frappe.throw(__('This is an Error Message'))

// frappe.prompt([
//     {
//         label: 'First Name',
//         fieldname: 'first_name',
//         fieldtype: 'Data'
//     },
   
// ], (values) => {
//        frappe.msgprint({
//     title: __('prompt'),
//     indicator: 'green',
//     message: __(values.first_name)
// });
  
// })

// frappe.confirm(
//     'Are you sure you want to proceed?',
//     () => {
//         frappe.msgprint('You clicked Yes! Proceeding...');
//     },
//     () => {
//         frappe.msgprint('You clicked No! Action cancelled.');
//     }
// );

// frappe.warn(
//     'Are you sure you want to proceed?',         // Primary message (title)
//     'There are unsaved changes on this page',    // Description (body text)
//     () => {
//         frappe.msgprint('Continuing with your action...');
//     },
//     'Continue',  // Label for the Continue button
//     true         // Makes the dialog minimizable (can be collapsed)
// );

// frappe.show_alert('Hi, you have a new message', 5);

// frappe.show_alert({
//     message:__('Hi, you have a new message'),
//     indicator:'green'
// }, 5);




// frappe.show_progress('Loading..', 70, 100, 'Please wait');


// frappe.new_doc("Sales Invoice");



    }
});
