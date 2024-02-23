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
		"on_submit": "nizwa.nizwa.hooks.doc_events.retension_bonus.on_submit",
        "before_validate": "nizwa.nizwa.hooks.doc_events.retension_bonus.before_validate"
	},
    "Contract": {
		"autoname": "nizwa.nizwa.hooks.doc_events.contract.autoname",
        "on_update": "nizwa.nizwa.hooks.doc_events.contract.on_update"
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
                "Retention Bonus-custom_section_break_7qtkn",
                "Retention Bonus-custom_project",
                "Retention Bonus-custom_cost_center",
                "Retention Bonus-custom_column_break_djj1g",
                "Retention Bonus-custom_shift_type",
                "Attendance-custom_column_break_sldim",
                "Attendance-custom_retention_bonus"
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
