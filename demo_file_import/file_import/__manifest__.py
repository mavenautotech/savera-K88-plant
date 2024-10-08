# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.
{
    'name': 'File Import Demo',
    'description': 'This is File Import using FTP in odoo 15',
    'summary': 'File Import',
    'category': 'File Import',
    'sequence': 1,
    'version': '1.0',
    'author': 'Maven Autotech Pvt Ltd',
    'website': 'https://www.mavenautomation.in',
    'depends': [

    ],

    'data': ['security/ir.model.access.csv',
             'views/stock_view.xml',
             # 'views/ftp_config.xml',
             'views/data.xml',
             'report/report.xml',
             # 'report/varification_report.xml',
             ],
    'demo': [

    ],
    # 'qweb': ['static/src/xml/button.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,

}
