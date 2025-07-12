# Copyright (c) 2025, sanjesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import now_datetime
import random
from frappe.model.document import Document


class SensorData(Document):
	pass



@frappe.whitelist()
def get_live_sensor_data():
    data = frappe.get_all(
        "Sensor Data", 
        fields=["value", "timestamp"],
        order_by="timestamp desc",
        limit=10
    )
    data.reverse()
    return {
        "labels": [d.timestamp.strftime("%H:%M:%S") for d in data],
        "values": [d.value for d in data]
    }



@frappe.whitelist()
def create_sensor_record():
    value = random.uniform(21.0, 80.0)
    doc = frappe.get_doc({
        "doctype": "Sensor Data",
        "value": value,
        "timestamp": now_datetime()
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"status": "success", "value": value}
