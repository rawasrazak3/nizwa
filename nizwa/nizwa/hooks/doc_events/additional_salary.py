import frappe
from frappe import _, bold
from frappe.model.document import Document
from frappe.utils import comma_and, date_diff, formatdate, getdate

from hrms.hr.utils import validate_active_employee


from hrms.payroll.doctype.additional_salary.additional_salary import AdditionalSalary

class CustomAdditionalSalary(AdditionalSalary):
    def validate(self):
        validate_active_employee(self.employee)
        self.validate_dates()
        self.validate_salary_structure()
        self.validate_recurring_additional_salary_overlap()
        self.validate_employee_referral()

        if float(self.amount) < 0:
            frappe.throw(_("Amount should not be less than zero"))