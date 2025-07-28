frappe.ui.form.on("Dialog API", {
    refresh(frm) {
        // Custom button to show dialog for Driver Details
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
                        // Save data into current document fields
                    frm.set_value('first_name', values.first_name);
                    frm.set_value('last_name', values.last_name);
                    frm.set_value('age', values.age);

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



frappe.show_progress('Loading..', 70, 100, 'Please wait');






    }
});
