import frappe
from frappe.utils import date_diff, today
#     add_months,
#     cint,
#     date_diff,
#     flt,
#     get_first_day,
#     get_last_day,
#     get_link_to_form,
#     getdate,
#     rounded,
#     today,
# )


@frappe.whitelist(allow_guest=True)
def send_supplier_document_expiry_notification():
    suppliers = frappe.db.get_list("Supplier", filters = {'disabled': 0}, fields = ['name'])
    for supplier in suppliers:
        supplier_doc = frappe.get_doc("Supplier", supplier.name)
        for item in supplier_doc.custom_documents:
            if item.expiry_date:
                current_date = today()
                if date_diff(item.expiry_date, current_date) == item.notification_time:
                    send_supplier_notification(supplier_doc.name, item.document_type, item.document_number)



@frappe.whitelist(allow_guest=True)
def send_supplier_notification(supplier, document_type, document_number, expire_days):
    message= document_type + " Document with document number" + document_number +  " will be expired in " + expire_days
    receiver = 'abrarpv97@gmail.com'
    email_args = {
        'recipients': [receiver],
        'message': (message),
        'subject': document_type + "Document Expires Soon for Supplier" + supplier,
    }
    frappe.sendmail(**email_args)