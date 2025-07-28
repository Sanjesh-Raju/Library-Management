app_name = "library_management"
app_title = "library_management"
app_publisher = "sanjesh"
app_description = "library management"
app_email = "sanjesh@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_management",
# 		"logo": "/assets/library_management/logo.png",
# 		"title": "library_management",
# 		"route": "/library_management",
# 		"has_permission": "library_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_management/public/icons.svg"

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
# 	"methods": "library_management.utils.jinja_methods",
# 	"filters": "library_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_management.utils.before_app_install"
# after_app_install = "library_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_management.utils.before_app_uninstall"
# after_app_uninstall = "library_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_management.tasks.all"
# 	],
# 	"daily": [
# 		"library_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["library_management.utils.before_request"]
# after_request = ["library_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_management.utils.before_job"]
# after_job = ["library_management.utils.after_job"]

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
# 	"library_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

doctype_js = {
    "Form Api": "public/js/form_api_list.js"
}


# scheduler_events = {
#     "hourly": [
#         "library_management.doctype.utilities_api.utilities_api.show_test_message"
#     ]
# }

page_js = {
    "live-chart": "public/js/live_chart.js",
    "bitcoin-chart": "public/js/bitcoin_chart.js"

}

app_include_templates = ["templates/includes/live_chart.html"]



# scheduler_events = {
#     "cron": {
#         "* * * * *": [
#             "library_management.library_management.doctype.sensor_data.sensor_data.create_sensor_record"
#         ]
#     }
# }


doctype_list_js = {
    "Database API": "public/js/database_api_list.js"
}


# my_app/hooks.py

website_context = {
    "brand_html": '<img src="https://www.logoground.com/uploads12/dv12y20232395842023-04-063833463panda.jpg" alt="Logo" style="height:40px; vertical-align:middle; margin-right:10px;"><b>My Brand</b>',

    "top_bar_items": [
        {"label": "Home", "url": "/"},
        {"label": "Contact", "url": "/contact"}
    ],
    "favicon": "/assets/my_app/images/favicon.png",
    "splash_image": "/assets/my_app/images/splash.png"
}

#------------------------------------------------------------------------------------------------------------------------------------------------------


# app_include_js = "/assets/library_management/js/main.js"
app_include_css = "/assets/library_management/css/app1.css"


website_context = {
    "favicon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0lsq0SpUwbknMZo9ZiGP4zv_95ynllj857w&s",
    "brand_html":'<div><img src="https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTEwL3JtNTM1LWJvb2stMDJhXzEucG5n.png.png"/>Library</div>',

    # "top_bar_items": [
    #     {"label": "Home", "url": "/", "target": "_self"},
    #     {"label": "Members", "url": "/library-member", "target": "_self"},
    #     {"label": "Books", "url": "/book", "target": "_self"},
    #     {"label": "Contact", "url": "/contact", "target": "_self"},
    # ],
    "footer_items": [
        {"label": "Privacy", "url": "/privacy"},
        {"label": "Terms", "url": "/terms"},
    ],
}

# website_context = {
#     "favicon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0lsq0SpUwbknMZo9ZiGP4zv_95ynllj857w&s",
#     "slogan": "Library for all readers",
#     "brand_html": "📚 Frappe Library",
#     "navbar_items": [
#         {"label": "Home", "url": "/", "target": "_self"},
#         {"label": "Members", "url": "/library-member", "target": "_self"},
#         {"label": "Books", "url": "/book", "target": "_self"},
#         {"label": "Contact", "url": "/contact", "target": "_self"},
#     ],
#     "footer_items": [
#         {"label": "Privacy", "url": "/privacy"},
#         {"label": "Terms", "url": "/terms"},
#     ],
#     "hero_title": "Welcome to the Gold Library ✨",
#     "hero_subtitle": "Explore our collection of rare and modern books",
#     "custom_css": "/assets/your_app/css/website.css",
#     "custom_js": "/assets/your_app/js/website.js"
# }




# your_app/hooks.py

website_redirects = [
    # {"source": "/app/users/", "target": "https://chatgpt.com/"},
    # {"source": "/app/private/library-management", "target": "/app/doctype/view/list"},
#     # {"source": "/app(/.*)?", "target": "https://docs.frappe.io/framework/user/en/api/form"},
#     # {"source": r'/items/item\?item_name=(.*)', "target": '/items/\1', "match_with_query_string": True},
#     {
#     # "source": r'/app/private/library-management\?id=(.*)',
#     # "target": '/app/library-membership/\\1',
#     # "match_with_query_string": True
# }

]

website_route_rules = [
    {
        "from_route": "/library-membership/<name>",
        "to_route": "app/library-membership/LMS00005"
    }
]

# web_include_js = "/assets/library_management/js/web.js"
# web_include_css = "/assets/library_management/css/web1.css"

webform_include_js = {
    "Article": "public/js/page.js"
}

webform_include_css = {
    "Article": "public/css/page1.css"
}

# hooks.py in your custom app

# page_js = {
#     "live-chart": "public/js/custom_page.js"
# }



# before_migrate = "library_management.library_management.migrate.before_migrate"
# after_migrate = "library_management.library_management.migrate.after_migrate"


# home_page = "homepage"


# role_home_page = {
#     "Accounts Manager": "Jinja_API"

# }

# get_website_user_home_page = "library_management.library_management.page.get_home_page"


portal_menu_items = [
    {"title": "Book", "route": "/homepage", "role": "Accounts Manager"},
    {"title": "Post Book", "route": "/new-article/", "role": "Customer"},
]

standard_portal_menu_items = [
    {"title": "Book", "route": "/article", "role": "Accounts Manager"},
    {"title": "Post Book", "route": "/new-article/", "role": "Customer"},
]



override_email_send = "library_management.library_management.overrides.email.send"
get_sender_details = "library_management.library_management.overrides.email.get_sender_details"







before_write_file = "library_management.library_management.overrides.file.before_write"



extend_website_page_controller_context = {
    "frappe.www.404": "library_management.library_management.error_page.context_404"
}
