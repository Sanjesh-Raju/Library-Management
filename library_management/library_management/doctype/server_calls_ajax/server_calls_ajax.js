// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server Calls AJAX", {
	refresh(frm) {

//-------------frappe.call 

// frappe.call('ping')
//  .then(r => {
//  console.log(r)
//  })

// frappe.call('frappe.core.doctype.user.user.get_role_profile', {
//  role_profile: 'tester'
// }).then(r => {
//  console.log(r.message)
// })

// --------------frappe.db.get_doc 

// frappe.db.get_doc('Query Builder', 'QB-001')
//  .then(doc => {
//  console.log(doc)
//  })

//-----------------frappe.db.get_list 

// frappe.db.get_list('Query Builder', {
//  fields: ['name1', 'status'],
//  filters: {
//  status: 'Open'
//  }
// }).then(records => {
//  console.log(records);
// })

//---------------------frappe.db.get_value 

// frappe.db.get_value('Query Builder', 'QB-003', 'status')
//  .then(r => {
//  console.log(r.message.status) 
//  })

//-----------------frappe.db.get\single\value 

 frappe.db.get_single_value('System Settings', 'time_zone')
 .then(time_zone => {
 console.log(time_zone);
 })

//--------------------frappe.db.set_value 

//  frappe.db.set_value('Query Builder', 'QB-001','status', 'open')
//  .then(r => {
//  let doc = r.message;
//  console.log(doc);
//  })

//-------------frappe.db.insert 

// frappe.db.insert({
//  doctype: 'Query Builder'}).then(doc => {
//  console.log(doc);
// })

// ---------frappe.db.count 

// frappe.db.count('Query Builder')
//  .then(count => {
//  console.log(count)
//  })

// frappe.db.count('Query Builder', { status: 'Open' })
//  .then(count => {
//  console.log(count)
//  })

//-----frappe.db.delete_doc 

// frappe.db.delete_doc('Query Builder', 'QB-005')
// frappe.msgprint("Delete the record")

//--------frappe.db.exists 

frappe.db.exists('Query Builder', 'QB-005')
 .then(exists => {
 console.log(exists) 
 })


	},
});
