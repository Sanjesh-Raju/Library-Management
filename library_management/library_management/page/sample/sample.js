frappe.pages['sample'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'My Custom Controls',
        single_column: true
    });

    let field_area = $('<div class="p-3">').appendTo(page.body);

    const fields = [
        {
            label: 'Enter Name',
            fieldname: 'my_input',
            fieldtype: 'Data'
        },
        {
            label: 'Attachment',
            fieldname: 'attachment',
            fieldtype: 'Attach'
        },
        {
            label: 'User Image',
            fieldname: 'user_image',
            fieldtype: 'Attach Image'
        },
        {
            label: 'Select User (Autocomplete)',
            fieldname: 'user_autocomplete',
            fieldtype: 'Autocomplete',
            options: [
                'faris@erpnext.com',
                'suraj@erpnext.com'
            ]
        },
        {
            label: 'Item Barcode',
            fieldname: 'item_barcode',
            fieldtype: 'Barcode'
        },
        {
            label: 'Enable Feature',
            fieldname: 'enable_feature',
            fieldtype: 'Check'
        },
        {
            label: 'JS Script',
            fieldname: 'script',
            fieldtype: 'Code',
            options: 'Javascript',
            wrap: true,
            max_lines: 10,
            min_lines: 5
        },
        {
            label: 'Favorite Color',
            fieldname: 'user_color',
            fieldtype: 'Color'
        },
        {
            label: 'Select Date Range',
            fieldname: 'date_range',
            fieldtype: 'Date Range'
        },
        {
            label: 'Blog Content (Markdown)',
            fieldname: 'content_md',
            fieldtype: 'Markdown Editor'
        },
        {
            label: 'Select Status',
            fieldname: 'status',
            fieldtype: 'Select',
            options: ['Open', 'Closed', 'Cancelled'].join('\n')
        },
        {
            label: 'Rate Experience',
            fieldname: 'rating',
            fieldtype: 'Rating'
        },
        {
            label: 'Submit Time',
            fieldname: 'in_time',
            fieldtype: 'Time'
        },
        {
            label: 'Fetch Button',
            fieldname: 'fetch_btn',
            fieldtype: 'Button',
            btn_size: 'sm'
        }
    ];

    const controls = {};  

    fields.forEach(field => {
        const control = frappe.ui.form.make_control({
            df: field,
            parent: field_area,
            render_input: true
        });
        control.make_input();
        controls[field.fieldname] = control;
    });

    $('<button class="btn btn-primary mt-3">Show Name</button>')
        .appendTo(field_area)
        .click(() => {
            const name_val = controls['my_input'].get_value();
            frappe.msgprint(`Name entered: ${name_val}`);
        });
};
