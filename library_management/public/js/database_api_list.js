frappe.listview_settings['Database API'] = {
    onload: function (listview) {
        listview.page.add_inner_button('Fetch Open Records', () => {
            frappe.call({
                method: 'library_management.library_management.doctype.database_api.database_api.fetch_open_records',
                callback: function (r) {
                    if (r.message) {
                        frappe.msgprint(__('Open Records:<br>' + JSON.stringify(r.message, null, 2)));
                    } else {
                        frappe.msgprint(__('No open records found.'));
                    }
                }
            });
        });
    }
};
