# -*- coding: utf-8 -*-
{
    'name': "ospt_document_list_filter",

    'summary': """
        This module used to filter Document Tree only show their
    """,

    'description': """
        1. Create Invoice Tree filtered based on user created
        2. Create Some User allowed to see All Data In Tree
    """,

    'author': "Kode Kite",
    'website': "http://www.onespt.blogspot.com",
    'images': ['static/description/images/gambar.jpg'],
    'price':'20',
    'currency':'EUR',
    'license':'OPL-1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Filter',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}