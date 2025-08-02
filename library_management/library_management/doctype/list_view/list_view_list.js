frappe.listview_settings['List View'] = {
    add_fields: ["status", "priority", "due_date"],

    get_indicator(doc) {
        if (doc.status === "Open") {
            return [__("Open"), "orange", "status,=,Open"];
        } else if (doc.status === "In Progress") {
            return [__("In Progress"), "blue", "status,=,In Progress"];
        } else if (doc.status === "Closed") {
            return [__("Closed"), "green", "status,=,Closed"];
        }
    },

    onload(listview) {
        const style = document.createElement('style');
        style.innerHTML = `
            /* List row font */
            .list-row-container {
                font-family: 'Arial', sans-serif !important;
                font-size: 15px !important;
                color: #333 !important;
            }

            /* Status pill font */
            .list-row-container .indicator-pill {
                font-weight: 700;
                font-family: 'Courier New', monospace;
            }

            /* Toolbar buttons */
            .page-head .page-actions .btn {
                font-family: 'Verdana', sans-serif;
                font-weight: bold;
            }

            /* 🔶 Title link (main name field) */
            .list-row .list-row-col.ellipsis a {
                font-family: 'Georgia', serif;
                font-size: 17px;
                color: #0066cc !important;
                font-weight: bold;
            }
        `;
        document.head.appendChild(style);

        listview.page.add_inner_button(__('Click Me'), () => {
            frappe.msgprint(__("Open List View Customization."));
        });
    },


};
