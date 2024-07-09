# -*- coding: utf-8 -*-
{
    'name': "Fixes conciliacion",

    'summary': """ """,

    'description': """ """,

    'author': "Xmarts",
    'website': "http://web.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'mail',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
