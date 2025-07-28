// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Employee', {
    refresh(frm) {
        // // Create a new page to display Employee List
        // let page = frappe.ui.make_app_page({
        //     title: 'Employee List',
        //     parent: frm.fields_dict.custom_section.wrapper,  // Parent element to append the page content
        //     single_column: true
        // });

        // // Fetch employees from the backend
        // frappe.call({
        //     method: 'frappe.client.get_list',
        //     args: {
        //         doctype: 'Employee',
        //         fields: ['employee_name', 'employee_id', 'department', 'status']
        //     },
        //     callback: function(response) {
        //         let employees = response.message;
        //         let html = '<ul>';
        //         employees.forEach(function(employee) {
        //             html += `<li>${employee.employee_name} - ${employee.employee_id} - ${employee.department} - ${employee.status}</li>`;
        //         });
        //         html += '</ul>';

        //         // Append the HTML content to the page
        //         $(page.page_body).html(html);
        //     }
        // });
    }
});
