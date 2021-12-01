# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CRM Commission',
    'version': '1.0',
    'summary': 'Module for CRM Commission',
    'sequence': 10,
    'description': """CRM Commission Plan Software""",
    'category': 'Productivity',
    'depends': ['report_xlsx', 'sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/commission_sequence.xml',
        'wizard/commission_report_wizard.xml',
        'report/report.xml',
        'views/crm_commission.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
