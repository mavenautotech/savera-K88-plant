# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Network Print',
    'version': '16.0.0.1',
    'category': '',
    'sequence': 1,
    'summary': 'Track Network Print',
    'description': """
    This module aims to manage network print.
    ==================================================
    
    Keeps account of the attendances of the employees on the basis of the
    actions(Check in/Check out) performed by them.
       """,
    'depends': ['stock','product'],
    'data': [
    
             'security/ir.model.access.csv',
             'views/user_ip_address_view.xml',
             'views/network_printing.xml',
             'report/prn_report_text.xml',
             'report/report_template.xml',
             
             

    ],
    'demo': [
             

    ],
    'installable': True,
    'auto_install': False,
    'qweb': [ ],
    'application': True,
    "license": "LGPL-3",
}
