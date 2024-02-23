import frappe


def validate(doc, method):
    if doc.rate == 0:
        employee = frappe.get_doc("Employee", doc.employee)
        for item in employee.custom_bonus_details:
            if item.salary_component == doc.salary_component:
                doc.rate = item.rate

def on_submit(doc, method):
    attendance = frappe.db.get_value("Attendance", {'attendance_date': doc.bonus_payment_date, 'employee': doc.employee}, 'name')
    if not attendance:
        attendance_doc = frappe.new_doc("Attendance")
        attendance_doc.attendance_date = doc.bonus_payment_date
        attendance_doc.employee = doc.employee
        attendance_doc.status = 'Present'
        attendance_doc.company = 'Nizwa Energy SPC'
        attendance_doc.shift = doc.custom_shift_type
        attendance_doc.custom_project = doc.custom_project
        attendance_doc.custom_cost_center = doc.custom_cost_center
        attendance_doc.custom_retention_bonus = doc.name
        attendance_doc.save(ignore_permissions=True)
        attendance_doc.submit()

