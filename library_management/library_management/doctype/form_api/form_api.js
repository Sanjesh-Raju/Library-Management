// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Form Api", {
	refresh(frm) {
        // set_value

//         frm.set_value('location', 'namakkal') 

//         frm.set_value({
//             status: "Open",
//             supermarket_name:"sks"
//         })  

//         frm.set_value('location', 'New location')
//             .then(() => {
//             frappe.msgprint(" Location !!!")
//             }
//         ) 

// // -----------------------------------------------------------------------------------------------------------------------

//         // Refresh: - Not Working

//         // frm.add_custom_button("Refresh",()=>{
//         //     frm.refresh();
//         //     // frappe.msgprint("Refreshed")
//         // });

//  // ---------------------------------------------------------------------------------------------------------------------

//         // Save:

//         frm.add_custom_button("Save",()=>{
            
//             frm.set_value('status', 'Closed')
//             frm.save();
//             frappe.show_alert({
//                 message:('Save Button Clicked'),
//                 indicator:'blue'
//             });
//         });

//  // ---------------------------------------------------------------------------------------------------------------------


// // ------->Submit

//         frm.add_custom_button("Submit",()=>{
//             frm.save("Submit");
//             frm.set_value('status', 'Closed')
//             frappe.show_alert({
//                 message:('Submit Button Clicked'),
//                 indicator:'yellow'
//             });
//         });

//  // ---------------------------------------------------------------------------------------------------------------------

//  //--------> Cancel

//         frm.add_custom_button("Cancel",()=>{
//             frm.save("Cancel");
//             frm.set_value('status', 'Closed')
//             frappe.show_alert({
//                 message:('Cancel Button Clicked'),
//                 indicator:'yellow'
//             }, 5);
//         });


//  // Email Doc

//         frm.add_custom_button("Email Doc",()=>{
//             frm.email_doc();
//             frappe.show_alert({
//                 message:('Email Doc Clicked'),
//                 indicator:'yellow'
//             }, 5);
//         });

// // Reload Doc

//         frm.add_custom_button("Reload Doc",()=>{
//             frm.reload_doc();
//             frappe.msgprint({
//                 message:('Reload Doc Clicked'),
//                 indicator:'yellow'
//             }, 5);
//         });

// // Refresh Field 

//         frm.add_custom_button("Refresh Field",()=>{
//             frm.refresh_field('location');
//             frm.refresh_field('status');
//             frappe.show_alert({
//                 message:('Refresh Field Clicked'),
//                 indicator:'yellow'
//             }, 5);
//         });

 
// Is Dirty 
 
        // frm.add_custom_button("Is Dirty",()=>{
        //      if (frm.is_dirty()) {
        //         frappe.show_alert('Form is Dirty')
        //     } else {
        //         frappe.show_alert('Form is Not Dirty')
        //     }
        // });

// Is New
 
        // frm.add_custom_button("Is New",()=>{
        //      if (frm.is_new()) {
        //         frappe.show_alert('Form is New')
        //     } else {
        //         frappe.show_alert('Form is Not New')
        //     }
        // },'status');

        // frm.add_custom_button("Closed",()=>{
        //      if (frm.is_new()) {
        //         frappe.show_alert('Form is New')
        //     } else {
        //         frappe.show_alert('Form is Not New')
        //     }
        // },'status');
 
        // // Change Custom Button Type - Working
 
        // frm.change_custom_button_type('Is New', null, 'success'); // Button Label, Group Label, Button Type(Primary, Danger, Success, Warning)
        // frm.change_custom_button_type('Closed', 'status', 'danger');
 
        // // Remove Custom Button - Working
 
        // frm.add_custom_button("Remove Is New Button",()=>{
        //     frm.remove_custom_button("Is New");
        // })
 
 

 // Set Intro
 
        // if (!frm.doc.description) {
        //     frm.set_intro('Please set the value of description');
        // }
 
        // if (!frm.doc.description) {
        //     frm.set_intro('Welcome to document', 'blue');
        // }
 

 

 
    // Enable Save and Disable Save 
 
    // checked(frm){
    //     if(frm.doc.checked){
    //         frm.disable_save();
    //     } else {
    //         frm.enable_save();
    //     }
    // },
 

 
    // Set DF Property 
 
    // checked(frm){
    //     if(frm.doc.checked){
    //         frm.set_df_property('description', 'reqd', 1)
    //         frm.set_df_property('description', 'fieldtype', 'Text Editor');
    //     } else {
    //         frm.set_df_property('description', 'reqd', 0)
    //     }
    // },
 

 
    // Toogle Enable 
 
    // checked(frm) {
    //     if (frm.doc.checked) {
    //         frm.toggle_enable("description", false);  // Enable the field
    //     } else {
    //         frm.toggle_enable("description", true); // Disable the field
    //     }
    // }
 

 
    // Toggle Reqd 
 
    // checked(frm) {
    //     if (frm.doc.checked) {
    //         frm.toggle_reqd("description", true);  
    //     } else {
    //         frm.toggle_reqd("description", false);
    //     }
    // }
 

 
    // Toggle Display 
 
    // checked(frm) {
    //     if (frm.doc.checked) {
    //         frm.toggle_display("description", false);
    //     } else {
    //         frm.toggle_display("description", true);
    //     }
    // }
 

 
 
// });
let my_field = frappe.ui.form.make_control({
    df: {
        label: "Customer Name",
        fieldname: "customer_name",
        fieldtype: "Data",
        reqd: 1
    },
    parent: wrapper,  // HTML element to attach this field to
    render_input: true
});

	},
});


frappe.listview_settings['Form Api'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Create New Supermarket', function() {
            frappe.new_doc('Supermarket');
        });

        listview.page.add_inner_button('Get Open Supermarkets', function() {
            frappe.call({
                method: 'your_app.api.supermarket.get_open_supermarkets',
                callback: function(r) {
                    frappe.msgprint('Found ' + r.message.length + ' open supermarkets');
                    console.log(r.message);
                }
            });
        });
    }
};

