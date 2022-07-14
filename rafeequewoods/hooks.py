from . import __version__ as app_version

app_name = "rafeequewoods"
app_title = "Rafeequewoods"
app_publisher = "wahni green technologies"
app_description = "wood industry"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "safvanph41@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rafeequewoods/css/rafeequewoods.css"
# app_include_js = "/assets/rafeequewoods/js/rafeequewoods.js"

# include js, css files in header of web template
# web_include_css = "/assets/rafeequewoods/css/rafeequewoods.css"
# web_include_js = "/assets/rafeequewoods/js/rafeequewoods.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rafeequewoods/public/scss/website"

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
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rafeequewoods.install.before_install"
# after_install = "rafeequewoods.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rafeequewoods.uninstall.before_uninstall"
# after_uninstall = "rafeequewoods.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rafeequewoods.notifications.get_notification_config"

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

doc_events = {
	"Sales Invoice": {
		"on_submit": "rafeequewoods.crud_events.generate_gst_invoice"
	},
	"Payment Entry":{
		"on_submit": "rafeequewoods.crud_events.generate_payment_entry"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rafeequewoods.tasks.all"
# 	],
# 	"daily": [
# 		"rafeequewoods.tasks.daily"
# 	],
# 	"hourly": [
# 		"rafeequewoods.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rafeequewoods.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rafeequewoods.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rafeequewoods.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rafeequewoods.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rafeequewoods.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"rafeequewoods.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name", "in", [
					"Payment Entry-auto_creation",
					"Sales Invoice-gst_same_rate",
					"Sales Invoice-auto_creation",
					"GST Settings-gst_company",
					"Sales Invoice Item-gst_cut",
					"Sales Invoice Item-use_same_rate",
					"Item-gst_cut"
				]
			]
		]
	}
]
