# Copyright (c) 2024, rawas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalaryCertificate(Document):
    pass

@frappe.whitelist()
def get_salary_detail(employee):
    salary_detail = []
    
    salary_structure_assignment = frappe.db.get_value('Salary Structure Assignment', {'employee': employee }, ['salary_structure'])
    if salary_structure_assignment:
        salary_detail = frappe.get_all('Salary Detail', 
                                        filters={'parent': salary_structure_assignment, 
                                                 'depends_on_payment_days': 1, 
                                                 'parentfield': 'earnings',
                                                 'parenttype': 'Salary Structure',
                                                 'docstatus': 1 },
                                        fields=['salary_component', 'abbr', 'amount'])
    
    return salary_detail
