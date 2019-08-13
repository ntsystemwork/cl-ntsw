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
        {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-odoo-argentina', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-sale', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
         'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
         'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-partner-contact', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-web', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-tools', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-social', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-ux', 'branch': '11.0'},

        # enterprise only
        {'usr': 'jobiols', 'repo': 'adhoc-enterprise-extensions', 'branch': '11.0'},


    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '11.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ]
}
