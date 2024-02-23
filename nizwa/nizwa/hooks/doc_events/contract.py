import frappe
from datetime import date
from frappe.model.naming import make_autoname

def autoname(doc, method):
    if doc.party_type == 'Customer':
        doc.name = make_autoname(doc.custom_contract_no)

def on_submit(doc, method):
    if doc.party_type == 'Customer':
        if not frappe.db.exists("Price List", doc.name):
            price_list_doc = frappe.new_doc("Price List")
            price_list_doc.price_list_name = doc.name
            price_list_doc.currency = "OMR"
            price_list_doc.selling = 1
            price_list_doc.append("countries", {
                "country": "Oman"
            })
            price_list_doc.save(ignore_permissions=True)
