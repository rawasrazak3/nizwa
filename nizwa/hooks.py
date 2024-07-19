app_name = "nizwa"
app_title = "NIZWA"
app_publisher = "rawas"
app_description = "nizwa"
app_email = "rawasrazak3@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nizwa/css/nizwa.css"
# app_include_js = "/assets/nizwa/js/nizwa.js"

# include js, css files in header of web template
# web_include_css = "/assets/nizwa/css/nizwa.css"
# web_include_js = "/assets/nizwa/js/nizwa.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nizwa/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
	"Sales Order" : "public/js/doctype_js/sales_order.js",
    "Sales Invoice" : "public/js/doctype_js/sales_invoice.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "nizwa.utils.jinja_methods",
# 	"filters": "nizwa.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "nizwa.install.before_install"
# after_install = "nizwa.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nizwa.uninstall.before_uninstall"
# after_uninstall = "nizwa.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "nizwa.utils.before_app_install"
# after_app_install = "nizwa.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "nizwa.utils.before_app_uninstall"
# after_app_uninstall = "nizwa.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nizwa.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
	"Retention Bonus":"nizwa.nizwa.hooks.doc_events.retension_bonus.CustomRetentionBonus",
    "Additional Salary":"nizwa.nizwa.hooks.doc_events.additional_salary.CustomAdditionalSalary"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
	"Retention Bonus": {
		#"on_submit": "nizwa.nizwa.hooks.doc_events.retension_bonus.on_submit",
        "before_validate": "nizwa.nizwa.hooks.doc_events.retension_bonus.before_validate"
	},
    "Contract": {
		"validate": "nizwa.nizwa.hooks.doc_events.contract.validate",
        "on_submit": "nizwa.nizwa.hooks.doc_events.contract.on_submit"
	}
}

fixtures = [
    {
    "doctype": "Custom Field",
    "filters": [
        [
            "name",
            "in",
            [ 
                "Journal Entry-custom_employee2_sign",
                "Journal Entry-custom_employee1_sign",
                "Journal Entry-custom_column_break_xrzut",
                "Journal Entry-custom_section_break_uqjm8",
                "Retention Bonus-custom_status",
                "Retention Bonus-custom_npt_hours",
                "Journal Entry-custom_employee_name3",
                "Journal Entry-custom_employee_name2",
                "Journal Entry-custom_employee_name1",
                "Journal Entry-custom_approved_by",
                "Journal Entry-custom_verified_by",
                "Journal Entry-custom_prepared_by",
                "Payment Entry-custom_approved_date",
                "Payment Entry-custom_checked_date",
                "Payment Entry-custom_prepared_date",
                "Payment Entry-custom_column_break_tnxxh",
                "Payment Entry-custom_column_break_p9ydi",
                "Payment Entry-custom_column_break_wv1wm",
                "Payment Entry-custom_approved_sign",
                "Payment Entry-custom_approved_by_sec",
                "Payment Entry-custom_checked_sign",
                "Payment Entry-custom_checked_by_sec",
                "Payment Entry-custom_prepared_sign",
                "Payment Entry-custom_prepared_by_sec",
                "Quotation-custom_submission_date",
                "Payment Entry-custom_employee_name",
                "Payment Entry-custom_checked_by",
                "Sales Invoice-custom_accumulated_amount",
                "Sales Invoice-custom_contract_value",
                "Sales Invoice-custom_contract_end_date",
                "Sales Invoice-custom_contract_start_date",
                "User Email-custom_user_email_for_mr",
                "Material Request-custom_material_request",
                "Employee-custom_ptw_attach",
                "Employee-custom_ptw_expiry_date",
                "Employee-custom_ptw_card_no",
                "Sales Invoice-custom_previous_invoice_amount",
                "Sales Invoice-custom_invoice_table",
                "Sales Invoice-custom_fetch_invoices",
                "Sales Invoice-custom_discount_percentage",
                "Sales Invoice-custom_old_invoice_discount_percentage",
                "Sales Invoice-custom_to_date",
                "Sales Invoice-custom_from_date",
                "Sales Invoice-custom_sales_invoice_special_discount",
                "Attendance-custom_retention_bonus",
                "Attendance-custom_column_break_sldim",
                "Sales Order Item-custom_days",
                "Sales Order Item-custom_to_date",
                "Sales Order Item-custom_from_date",
                "Sales Order Item-custom_qty",
                "Retention Bonus-custom_shift_type",
                "Retention Bonus-custom_column_break_djj1g",
                "Retention Bonus-custom_cost_center",
                "Retention Bonus-custom_project",
                "Retention Bonus-custom_section_break_7qtkn",
                "Leave Application-custom_leave_approver_name",
                "Payment Entry-custom_employee_name2",
                "Payment Entry-custom_employee_name1",
                "Quotation Item-custom_lih_dbr_charges_tool",
                "Quotation-custom_reference",
                "Quotation-custom_section_break_wcume",
                "Payment Entry-custom_approved_by",
                "Payment Entry-custom_prepared_by",
                "Purchase Order-custom_employee_name",
                "Purchase Order-custom_employee_name1",
                "Purchase Order-custom_approved_by",
                "Purchase Order-custom_prepared_by",
                "Sales Order-custom_service_ticket_no",
                "Sales Order-custom_account_no",
                "Sales Order-custom_column_break_umdjb",
                "Sales Order-custom_bank_address",
                "Sales Order-custom_account_name",
                "Sales Order-custom_accounts_details",
                "Sales Invoice Item-custom_qty",
                "Sales Order-custom_well_or_location_no",
                "Sales Invoice Item-custom_days",
                "Sales Invoice-custom_block_no",
                "Retention Bonus-custom_attendance_date",
                "Material Request-custom_project",
                "Material Request-custom_cost_center",
                "Purchase Order-custom_md_ref_no",
                "Purchase Order-custom_purchase_reference_no",
                "Sales Order-custom_purchase_order_no",
                "Customer-custom_bank_address",
                "Customer-custom_account_no",
                "Customer-custom_account_name",
                "Document Naming Rule-custom_customer_name",
                "Quotation-custom_company_details",
                "Employee-custom_column_break_ludnf",
                "Employee-custom_ptw",
                "Employee-custom_contract_attach",
                "Employee-custom_contract_expiry_date",
                "Employee-custom_contract_no",
                "Employee-custom_employee_contract",
                "Employee-custom_h2s_attach",
                "Employee-custom_h2s_expiry_date",
                "Employee-custom_card_no",
                "Employee-custom_h2s",
                "Employee-custom_license_attach",
                "Employee-custom_opal_license_attach",
                "Employee-custom_medical_attach",
                "Employee-custom_visa_attach",
                "Employee-custom_resident_card_attach",
                "Employee-custom_passport_attach",
                "Material Request-custom_purpose",
                "Retention Bonus-custom_client_name",
                "Contract-custom_payment_terms",
                "Sales Invoice-custom_bank_address",
                "Sales Invoice-custom_account_no",
                "Sales Invoice-custom_column_break_kxfmx",
                "Sales Invoice-custom_account_name",
                "Sales Invoice-custom_accounts_details",
                "Sales Invoice-custom_vendor_no",
                "Customer-custom_vendor_no",
                "Sales Invoice Item-custom_po_line",
                "Retention Bonus-custom_service_ticket",
                "Supplier-custom_group_supplier",
                "Sales Invoice-custom_contract_no",
                "Sales Invoice-custom_contract_name",
                "Sales Invoice-custom_contract",
                "Sales Invoice-custom_rig_hoist_no",
                "Sales Invoice-custom_well_or_location_no",
                "Sales Invoice-custom_service_ticket_no",
                "Sales Invoice-custom_job_order_no",
                "Sales Invoice-custom_purchase_order_no",
                "Sales Invoice-custom_job_end_date",
                "Sales Invoice-custom_job_start_date",
                "Sales Invoice-custom_vat_no",
                "Employee-custom_nationality",
                "Retention Bonus-custom_remarks",
                "Retention Bonus-custom_rig_no",
                "Retention Bonus-custom_well_no",
                "Project-custom_contract",
                "Sales Order-custom_call_out_date",
                "Sales Order-custom_rig_hoist_no",
                "Sales Order-custom_service_type",
                "Sales Order-custom_well_or_location",
                "Sales Order-custom_ne_ticket_no",
                "Sales Order-custom_contract_name",
                "Sales Order-custom_contract_no",
                "Sales Order-custom_vat_no",
                "Customer-custom_vat_no",
                "Price List-custom_contract",
                "Contract-custom_contract_name",
                "Sales Order-custom_contract",
                "Employee-custom_license_expiry_date",
                "Employee-custom_opal_license_expiry_date",
                "Employee-custom_license_details",
                "Employee-custom_column_break_939kk",
                "Employee-custom_license_no",
                "Employee-custom_column_break_gu8bv",
                "Employee-custom_opal_license_no",
                "Employee-custom_opal_license",
                "Employee-custom_medical_expiry_date",
                "Employee-custom_column_break_afytd",
                "Employee-custom_medical_no",
                "Employee-custom_medical",
                "Employee-custom_visa_expiry_date",
                "Employee-custom_column_break_gjhgf",
                "Employee-custom_visa_no",
                "Employee-custom_visa",
                "Employee-custom_resident_expiry_date",
                "Employee-custom_column_break_z0c8x",
                "Employee-custom_resident_no",
                "Employee-custom_resident_card",
                "Contract-custom_contract_no",
                "SUPPLIER ASSESSMENT FORM-custom_date",
                "SUPPLIER ASSESSMENT FORM-custom_column_break_8rypt",
                "SUPPLIER ASSESSMENT FORM-custom_name_and_designation",
                "SUPPLIER ASSESSMENT FORM-custom_prepared_by",
                "SUPPLIER ASSESSMENT FORM-custom_section_break_nc5fi",
                "SUPPLIER ASSESSMENT FORM-custom_scope_of_supply",
                "SUPPLIER ASSESSMENT FORM-custom_evaluation_comments",
                "SUPPLIER ASSESSMENT FORM-custom_criteria_for_evaluation_and_selection",
                "SUPPLIER ASSESSMENT FORM-custom_evaluation_sheet_",
                "Employee-custom_column_break_qgowy",
                "Employee-custom_bonus_details",
                "Employee-custom_bonus",
                "Employee Checkin-custom_cost_center",
                "Employee Checkin-custom_project",
                "Employee Checkin-custom_more_information",
                "Attendance-custom_cost_center",
                "Attendance-custom_project",
                "Attendance-custom_more_information",
                "Supplier-custom_supplier_type1",
                "Material Request Item-custom_part_no",
                "Item Price-custom_quantity",
                "Purchase Order Item-custom_part_no",
                "Item-custom_part_no",
                "Supplier-custom_supplier_type",
                "Purchase Order-custom_signature_image",
                "Purchase Order-custom_sign",
                "Purchase Order-custom_sign_here",
                "Purchase Order-custom_attach_signature_image",
                "Purchase Order-custom_signature_type",
                "Purchase Order-custom_signature",
                "Material Request-custom_section__department",
                "Material Request-custom_request_by",
                "Delivery Note-customer_name_in_arabic",
                "Sales Order-customer_name_in_arabic",
                "POS Invoice-customer_name_in_arabic",
                "Sales Invoice-customer_name_in_arabic",
                "Customer-customer_name_in_arabic",
                "Supplier-custom_documents",
                "Supplier-custom_documents_attach",
                "Supplier-custom_column_break_ar2aw",
                "Supplier-custom_iso_9001",
                "Supplier-custom_column_break_6nmju",
                "Supplier-custom_api_q2",
                "Supplier-custom_column_break_rrzy6",
                "Supplier-custom_iso_14001",
                "Supplier-custom_api_q1",
                "Supplier-custom_certificates",
                "Supplier-custom_trade_references",
                "Supplier-custom_major_client_trade_references",
                "Supplier-custom_authorized_signature",
                "Supplier-custom_authorized_date",
                "Supplier-custom_authorized_name",
                "Supplier-custom_column_break_n1dp6",
                "Supplier-custom_authorized_position",
                "Supplier-custom_authorized_signatures",
                "Supplier-custom_legal_status",
                "Supplier-custom_an_exclusive_agent",
                "Supplier-custom_global_branches",
                "Supplier-custom_number_of_branches",
                "Supplier-custom_company_type",
                "Supplier-custom_branch_in_oman",
                "Supplier-custom_company_origin",
                "Supplier-custom_column_break_hk0bs",
                "Supplier-custom_is_oman",
                "Supplier-custom_year_of_incorporation",
                "Supplier-custom_commercial_registration_no",

            ]
        ]
    ]
    }
]
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nizwa.tasks.all"
# 	],
# 	"daily": [
# 		"nizwa.tasks.daily"
# 	],
# 	"hourly": [
# 		"nizwa.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nizwa.tasks.weekly"
# 	],
# 	"monthly": [
# 		"nizwa.tasks.monthly"
# 	],
# }
scheduler_events = {
	"daily": [
		"nizwa.utils.send_supplier_document_expiry_notification"
	]
}


# Testing
# -------

# before_tests = "nizwa.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nizwa.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nizwa.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nizwa.utils.before_request"]
# after_request = ["nizwa.utils.after_request"]

# Job Events
# ----------
# before_job = ["nizwa.utils.before_job"]
# after_job = ["nizwa.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"nizwa.auth.validate"
# ]
