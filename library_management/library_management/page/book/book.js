frappe.pages['book'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Book',
    });

    page.set_title('My Page');
    page.set_title_sub('Subtitle');
    page.set_indicator('Pending', 'blue');

    // Primary action button
    let $btn = page.set_primary_action('New', () => create_new());
    $btn.css('background-color', '#af4ca0ff');
    $btn.css('color', 'white');

    // Secondary action button
    let $btn1 = page.set_secondary_action('Refresh', () => refresh());
    $btn1.css('background-color', '#6ed987ff');
    $btn1.css('color', 'white');

    // Menu items
    page.add_menu_item('Send Email', function() {
        frappe.msgprint('Send Email clicked');
    });

    page.add_menu_item('Send Update', function() {
        frappe.msgprint('Send Update clicked');
    });

    // Actions
    page.add_action_item('Delete', () => delete_items());

    // Inner buttons
    page.add_inner_button('Update Posts', () => update_posts());
    page.add_inner_button('New Post', () => new_post(), 'Make');

    page.change_inner_button_type('Update Posts', null, 'danger');
    page.change_inner_button_type('New Post', 'Make', 'primary');

    // Select field
    let field = page.add_field({
        label: 'Status',
        fieldtype: 'Select',
        fieldname: 'status',
        options: ['Open', 'Closed', 'Cancelled'],
        change() {
            console.log('Selected Status:', field.get_value());
        }
    });

    // 💡 Book data
    const books = [
        {
            title: 'The Alchemist',
            image: 'https://thumbs.dreamstime.com/b/open-book-feather-quill-teal-background-writing-literature-open-book-feather-quill-teal-background-writing-literature-361548553.jpg',
            description: 'A novel by Paulo Coelho.'
        },
        {
            title: 'Atomic Habits',
            image: 'https://thumbs.dreamstime.com/b/flying-magic-books-library-367534733.jpg',
            description: 'Build good habits, break bad ones.'
        },
        {
            title: 'Deep Work',
            image: 'https://images.unsplash.com/photo-1541963463532-d68292c34b19?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Ym9va3xlbnwwfHwwfHx8MA%3D%3D',
            description: 'Rules for focused success in a distracted world.'
        }
    ];

    // 🧱 Card Grid Section
    const $grid = $(`<div class="row mt-4"></div>`).appendTo(page.body);

    books.forEach(book => {
        const $card = $(`
            <div class="col-md-4">
                <div class="card" style="margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <img src="${book.image}" class="card-img-top" alt="${book.title}" style="height: 150px; object-fit: cover;">
                    <div class="card-body">
                        <h5 class="card-title">${book.title}</h5>
                        <p class="card-text">${book.description}</p>
                        <button class="btn btn-primary btn-sm">View</button>
                    </div>
                </div>
            </div>
        `);
        $grid.append($card);
    });

    // Helper functions
    function create_new() {
        frappe.msgprint('New button clicked');
    }

    function refresh() {
        frappe.msgprint('Page refreshed');
    }

    function delete_items() {
        frappe.confirm('Are you sure to delete?', () => {
            frappe.msgprint('Deleted!');
        });
    }

    function update_posts() {
        frappe.msgprint('Updating posts...');
    }

    function new_post() {
        frappe.msgprint('Creating new post...');
    }
};
