def before_write(file_doc):
    # file_doc is the File DocType
    frappe.logger().info(f"Preparing to save file: {file_doc.file_name}")
    if file_doc.file_size > 1 * 1024 * 1024:  # 10 MB
        frappe.throw("File too large. Max 10MB allowed.")
