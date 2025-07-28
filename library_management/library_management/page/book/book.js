frappe.pages['book'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Book',
		// single_column: true
		
	});

	page.set_title('My Page')
	page.set_title_sub('Subtitle')
	page.set_indicator('Pending', 'blue')
	// page.clear_indicator()

let $btn = page.set_primary_action('New', () => create_new());
$btn.css('background-color', '#af4ca0ff'); 
$btn.css('color', 'white');  
// page.clear_primary_action()

let $btn1 = page.set_secondary_action('Refresh', () => refresh())
$btn1.css('background-color', '#6ed987ff'); 
$btn1.css('color', 'white');

// page.clear_secondary_action()
page.add_menu_item('Send Email', function() {
    frappe.msgprint('Send Email clicked');
});

page.add_menu_item('Send Update', function() {
    frappe.msgprint('Send Update clicked');
});

// page.clear_menu()

page.add_action_item('Delete', () => delete_items())
// page.clear_actions_menu()

page.add_inner_button('Update Posts', () => update_posts())
page.add_inner_button('New Post', () => new_post(), 'Make')


// change type of ungrouped button
page.change_inner_button_type('Update Posts', null, 'danger');

// change type of a button in a group
page.change_inner_button_type('New Post', 'Make', 'primary');
page.clear_inner_toolbar()


let field = page.add_field({
    label: 'Status',
    fieldtype: 'Select',
    fieldname: 'status',
    options: [
        'Open',
        'Closed',
        'Cancelled'
    ],
    change() {
        console.log(field.get_value());
    }
	
	
});
// page.clear_fields()










































}









