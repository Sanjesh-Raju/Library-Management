frappe.ui.form.on("Dialog API", {
    refresh(frm) {
        // Custom button to show dialog for Driver Details
        frm.add_custom_button('Dialog API', () => {
            let d = new frappe.ui.Dialog({
                title: 'Driver Details',
                fields: [
                    { label: 'First Name', fieldname: 'first_name', fieldtype: 'Data', reqd: 1 },
                    { label: 'Last Name', fieldname: 'last_name', fieldtype: 'Data', reqd: 1 },
                    { label: 'Age', fieldname: 'age', fieldtype: 'Int', reqd: 1 }
                ],
                size: 'small',
                primary_action_label: 'Submit',
                primary_action: (values) => {
                    console.log("Driver details:", values);
                    d.hide();
                }
            });
            d.show();
        });

    }
});
