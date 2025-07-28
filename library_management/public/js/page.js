frappe.ready(() => {
    console.log(" Web Form loaded!");


    // Create a new button
    const customBtn = document.createElement("button");
    customBtn.innerText = "Show Message";
    customBtn.type = "button";  
    customBtn.style.marginTop = "20px";
    customBtn.style.padding = "8px 12px";
    customBtn.style.backgroundColor = "#007bff";
    customBtn.style.color = "white";
    customBtn.style.border = "none";
    customBtn.style.borderRadius = "4px";
    customBtn.style.cursor = "pointer";

    // Add click event
    customBtn.addEventListener("click", () => {
        frappe.msgprint(` Web Form loaded!`);
    });

    // Append the button to the form
    const formWrapper = document.querySelector(".web-form");
    if (formWrapper) {
        formWrapper.appendChild(customBtn);
    }
});
