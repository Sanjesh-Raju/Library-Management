frappe.ui.form.on("Field Setting", {
    refresh(frm) {
        if (!frm.doc.payment_id) {
            frm.add_custom_button('💸 Make Payment', function () {
                frappe.require("https://checkout.razorpay.com/v1/checkout.js", function () {
                    let amount_in_paise = 200 * 100;
                    let options = {
                        key: "rzp_test_1DP5mmOlF5G5ag",  
                        amount: amount_in_paise,
                        currency: "INR",
                        name:"Test  Engine",
                        description: "Bill Payment",
                        handler: function (response) {
                            frappe.msgprint("Payment successful. Payment ID: " + response.razorpay_payment_id);
                        },
                        theme: {
                            color: "#54c1f3ff"
                        }
                    };
                    let rzp = new Razorpay(options);
                    rzp.open() ;
                });
            });
        }
    },
});
