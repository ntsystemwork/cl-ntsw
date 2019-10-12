# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019  NT System Work  (http://www.ntsystemwork.com)
#    All Rights Reserved.
#
#
# -----------------------------------------------------------------------------
{
    'name': 'ntsw',
    'version': '11.0e.0.0.2',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customizacion para NTSW',
    'author': 'NTSystemWork',
    'depends': [
        'sale_management',
        'account_invoicing',
        'purchase',
        'crm',
        'project',
        'stock',
        'helpdesk',
        'hr_recruitment',

        'standard_depends_ee',

        # utilitarios
        'product_currency',
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'ntsystemwork', 'repo': 'cl-ntsw', 'branch': '11.0', 'ssh': True},
        {'usr': 'ntsystemwork', 'repo': 'common-addons', 'branch': '11.0', 'ssh':True},

        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting',         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '11.0'},

        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-ux', 'branch': '11.0'},

        # enterprise only
        {'usr': 'ingadhoc', 'repo': 'enterprise-extensions', 'branch': '11.0'},

    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '11.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ]
}
