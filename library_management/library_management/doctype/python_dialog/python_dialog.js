// Copyright (c) 2025, sanjesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Python Dialog", {
	refresh(frm) {

        frappe.msgprint({
  message: "Here is your detailed audit log...",
  title: "Audit Info",
  is_minimizable: true,
  wide: true
});

fetch('http://localhost:8001/api/method/frappe.auth.get_logged_user', {
  headers: {
    'Authorization': 'token d10e03842f6f27e: b4dbe509b36fe36'
  }
})
.then(response => response.json())
.then(data => console.log(data));
console.log(data)


	},
});
