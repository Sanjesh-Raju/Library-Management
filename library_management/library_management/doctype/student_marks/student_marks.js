// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Marks', {
    marks: function(frm) {
        if (frm.doc.marks != null) {
            if (frm.doc.marks >= 35) {
                frm.set_value('status', 'Pass');
                frappe.msgprint('You are Pass');
            } else {
                frm.set_value('status', 'Fail');
                frappe.msgprint('You are Fail');
            }
        }
    },
    before_save: function(frm) {
        if (frm.doc.marks == null) {
            frappe.throw('Please fill the Marks');
        }
    },
    refresh(frm) {
        frm.add_custom_button('Submit to Server', () => {
            if (!frm.doc.student_name || !frm.doc.subject_name || frm.doc.marks == null) {
                frappe.msgprint('Please fill all fields before submitting.');
                return;
            }

            frappe.call({
                method: "library_management.library_management.doctype.student_marks.student_marks.student_marks", 
                args: {
                    student_name: frm.doc.student_name,
                    subject_name: frm.doc.subject_name,
                    marks: frm.doc.marks,
                    status: frm.doc.status
                },
                callback: function(rs) {
                    if (rs.message) {
                        frappe.msgprint(rs.message);
                    }
                }
            });
        });
    }
});
