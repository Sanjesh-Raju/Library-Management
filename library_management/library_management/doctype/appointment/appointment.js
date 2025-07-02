// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointment", {
	// setup: function(frm) {
    //     frappe.msgprint("Setup: Triggered once when form is created for the first time");
    // },

    // before_load: function(frm) {
    //     frappe.msgprint("Before Load: Form is about to load");
    // },

    // onload: function(frm) {
    //     frappe.msgprint("Onload: Form is loading and about to render");
    // },

    // refresh: function(frm) {
    //     frappe.msgprint("Refresh: Form has loaded and rendered");
    //     // frm.disable_save();
    // },

    // onload_post_render: function(frm) {
    //     frappe.msgprint("Onload Post Render: Form is rendered completely");
    // },

    // validate: function(frm) {
    //     if (!frm.doc.patient) {
    //         // frappe.msgprint("Validate: Before before_save");
    //         frappe.throw("patient is required");
    //     }else{
    //         frappe.msgprint("hiii");  
    //     }
    // },

    // before_save: function(frm) {
    //     frappe.msgprint("Before Save");
    // },

    // after_save: function(frm) {
    //     frappe.msgprint("After Save: After form is saved");
    // },

    // before_submit: function(frm) {
    //     frappe.msgprint("Before Submit: Before submit is called");
    // },

    // on_submit: function(frm) {
    //     frappe.msgprint("On Submit: After form is submitted");
    // },

    // before_cancel: function(frm) {
    //     frappe.msgprint("Before Cancel: Before cancel is called");
    // },

    // after_cancel: function(frm) {
    //     frappe.msgprint("After Cancel: After form is cancelled");
    // },

//     timeline_refresh: function(frm) {
//     if (frm.doc.status === "Urgent") {
//         frm.timeline.add_comment(' Urgent appointment. Please review immediately.');
//     }

//     if (frm.doc.priority === "High") {
//         frm.timeline.add_comment('This is a high-priority appointment.');
//     }

//     if (frm.doc.status === "Cancelled") {
//         frm.timeline.add_comment('This appointment was cancelled.');
//     }
// },


    timeline_refresh: function(frm) {
        frappe.msgprint("Timeline Refresh: After form timeline is rendered");
    },

    // // Field-specific change event
    // doctor: function(frm) {
    //     frappe.msgprint("doctor Field Changed:", frm.doc.patient);
    // },


    // items_on_form_rendered: function(frm, grid_row) {
    //     frappe.msgprint("Row form rendered for items table:", grid_row.doc);
    // }

// onload(frm) {
//         if (!frm.doc.a) frm.set_value('a', 10);
//         if (!frm.doc.b) frm.set_value('b', 12);
//         if (!frm.doc.c) frm.set_value('c', 3);
//     },

//     i(frm) {
//         if (frm.doc.i === "a") {
//             frm.set_value('d', frm.doc.a);
//         }
//     },

//     a(frm) {
//         update_e(frm);
//     },

//     d(frm) {
//         update_e(frm);
//     },
//     s(frm) {
//         update_e(frm);
//     }
});

// function update_e(frm) {
//     const a = frm.doc.s ;
//     const d = frm.doc.d;
//     const result = a * d;
//     frm.set_value('e', result);
// }

