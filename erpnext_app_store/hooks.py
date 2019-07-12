# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_app_store"
app_title = "Erpnext App Store"
app_publisher = "Aminov Emil"
app_description = "Application on frappe. There you can install apps from repositories to your frappe application"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "amionv99@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_app_store/css/erpnext_app_store.css"
# app_include_js = "/assets/erpnext_app_store/js/erpnext_app_store.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_app_store/css/erpnext_app_store.css"
# web_include_js = "/assets/erpnext_app_store/js/erpnext_app_store.js"

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

# Website user home page (by function)
# get_website_user_home_page = "erpnext_app_store.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_app_store.install.before_install"
# after_install = "erpnext_app_store.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_app_store.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }


scheduler_events = {
    # "cron": {
    #     "0/2 * * * *": [
    #         "erpnext_app_store.doctype.info_updater_from_github.update_info"
    #     ]
    # },
    "all": [
        "erpnext_app_store.tasks.all",
        "erpnext_app_store.doctype.info_updater_from_github.update_info"
    ], # 4 minutes
    "daily": [
        "erpnext_app_store.tasks.daily"
    ],
    "hourly": [
        "erpnext_app_store.tasks.hourly"
    ],
    "weekly": [
        "erpnext_app_store.tasks.weekly"
    ],
    "monthly": [
        "erpnext_app_store.tasks.monthly"
    ]
}

# Testing
# -------

# before_tests = "erpnext_app_store.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_app_store.event.get_events"
# }
