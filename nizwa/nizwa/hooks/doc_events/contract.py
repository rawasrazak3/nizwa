import frappe
from datetime import date
from frappe.model.naming import make_autoname

def autoname(doc, method):
    if doc.party_type == 'Customer':
        doc.name = make_autoname(doc.custom_contract_no)

def on_update(doc, method):
    if doc.party_type == 'Customer' and doc.is_new():
        price_list_name =  doc.custom_contract_name + doc.custom_contract_no
        if not frappe.db.exist("Price List", price_list_name):
            price_list_doc = frappe.new_doc("Price List")
            price_list_doc.price_list_name = price_list_name
            price_list_doc.currency = "OMR"
            price_list_doc.selling = 1
            price_list_doc.append("countries", {
                "country": "Oman"
            })
            price_list_doc.save(ignore_permissions=True)
