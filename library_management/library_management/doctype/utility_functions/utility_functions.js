// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Utility Functions", {
	refresh(frm) {
        frm.add_custom_button("Utility",function(){
            frappe.call({
                method: 'library_management.library_management.doctype.utility_functions.utility_functions.utl',
                callback: function (r){
                    if(r.meesage()){
                        // console.log(r.message);
                        window.open(r.message, "_blank");
                    }
                    else{
                        frappe.msgprint('No response from API')
                    }
                },
                error: function(err){
                    frappe.msgprint("API call  Failed")
                }
            })
        })

	},
});
