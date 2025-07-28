frappe.pages['live-chart'].on_page_load = function(wrapper) {
    console.log("Custom JS loaded for live-chart!");

    const btn = document.createElement("button");
    btn.innerText = "Click Me!";
    btn.style.padding = "10px";
    btn.style.marginTop = "20px";
    btn.style.backgroundColor = "#007bff";
    btn.style.color = "white";
    btn.onclick = function () {
        frappe.msgprint("Hello from custom page!");
    };

    wrapper.page.body.appendChild(btn);
};
