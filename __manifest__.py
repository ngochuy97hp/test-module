{
    'name': "Odoo Apps Management",

    'summary': """
Manage Odoo apps / modules. Generate apps from a git branch""",

    'description': """
Features at a glance
====================

1. Define and Manage Odoo Modules with multiple versions against Odoo versions
2. Integrated with Odoo's products
3. Integrated with Invoicing for manage billing and payments regarding to your module sales
4. Integrated with Git Management application to allow

   * Add git branches that contains your Odoo Apps/Modules
   * Scan the branches for automatic Odoo Apps / Modules discovering
   * Schedule automatic branches scanning periodically

5. Synchronize modules data with Products

   * Automatically created new products or map with the existing ones identified by product code and module technical name matching
   * Mapp Odoo Versions with Product Attributes
   * Automatic update products images, price, vendor price, product licenses (thanks to the integration with the Product License Management application), etc
   
6. Customer Portal Apps Downloads

   * Customer can login to your portal and download the Apps that she or he bought either
   
     * from the invoice detail page if the invoice is paid
     * from the "My Purchased Apps" page

7. Public download URL

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'author': "T.V.T Marine Automation (aka TVTMA)",
    'website': "https://www.tvtmarine.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Odoo Apps',
    'version': '0.8',

    # any module necessary for this one to work correctly
    'depends': ['to_token_expiration', 'account', 'to_product_odoo_version', 'to_git_odoo_version', 'to_product_license'],

    # always loaded
    'data': [
        'data/partner_data.xml',
        'data/product_category_data.xml',
        'security/module_security.xml',
        'security/ir.model.access.csv',
        'views/root_menu.xml',
        'views/odoo_module_version_image_views.xml',
        'views/odoo_module_version_views.xml',
        'views/odoo_module_views.xml',
        'views/product_template_views.xml',
        'views/git_branch_views.xml',
        'views/git_repository_views.xml',
        'views/software_author_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_invoice_views.xml',
        'views/res_partner_views.xml',
        'views/odoo_module_version_download_stat_views.xml',
        'views/apps_portal_templates.xml',
        'report/account_invoice_report_view.xml',
        'wizard/wizard_git_url_add_views.xml',
        'wizard/wizard_odoo_module_version_download_views.xml',
        'wizard/wizard_odoo_module_version_public_download_views.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 495.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}

