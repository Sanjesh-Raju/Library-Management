import frappe
import time

# 👤 Override the default sender info
def get_sender_details():
    return "John Test", "john@example.com"

# 📤 Override the email send function
def send(self, sender, recipient, msg):
    try:
        # Simulate sending email via third-party
        frappe.logger().info(f"Sending email to {recipient} from {sender}")
        
        # Fake delay to simulate sending
        time.sleep(2)

        # Log content
        frappe.logger().info(f"Email content:\n{msg}")

        # ✅ Mark as sending and then sent
        self.update_status("Sending")
        self.update_status("Sent")

        # Optional: add log comment
        frappe.logger().info("Email successfully sent via custom hook.")
        
    except Exception as e:
        # ❌ Handle failure
        self.update_status("Error")
        frappe.log_error(f"Failed to send email to {recipient}: {str(e)}")
