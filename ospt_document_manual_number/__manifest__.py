# -*- coding: utf-8 -*-
{
    'name': "ospt_document_manual_number",

    'summary': """
        This module used to add manual number (For PPN) to document
    """,

    'description': """
        I.  Membuat field manual number di document PO
        II. Membuat field manual number di document IP
        III. Membuat field manual number di document SO
        IV. Membuat field manual number di document DO
        V.  Membuat field manual number di document INV
    """,

    'author': "Kode Kite",
    'website': "http://www.onespt.blogspot.com",
    'images': ['static/description/images/gambar1.jpg'],
    'price':'5',
    'currency':'EUR',
    'license':'OPL-1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Form',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

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