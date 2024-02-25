import frappe
from datetime import date
from frappe.model.naming import make_autoname

def validate(doc, method):
    if doc.party_type == 'Customer' and doc.is_new():
        doc.name = doc.custom_contract_no

def on_submit(doc, method):
    if doc.party_type == 'Customer':
        if not frappe.db.exists("Price List", {'custom_contract': doc.name}):
            price_list_doc = frappe.new_doc("Price List")
            price_list_doc.price_list_name = doc.custom_contract_name + "-" +  doc.custom_contract_no
            price_list_doc.currency = "OMR"
            price_list_doc.selling = 1
            price_list_doc.custom_contract = doc.name
            price_list_doc.append("countries", {
                "country": "Oman"
            })
            price_list_doc.save(ignore_permissions=True)
        if not frappe.db.exists("Project", {'custom_contract': doc.name}):
            project_doc = frappe.new_doc("Project")
            project_doc.project_name = doc.custom_contract_name + "-" +  doc.custom_contract_no
            project_doc.custom_contract = doc.name
            project_doc.save(ignore_permissions=True)
