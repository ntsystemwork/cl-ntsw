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

        # para la localizacion argentina
        'l10n_ar_base',  # esto se instala solo
        'l10n_ar_account',  # esto se instala solo
        'l10n_ar_afipws_fe',  # Factura Electrónica Argentina
        'l10n_ar_aeroo_einvoice',  # impresion de factura electronica aeroo
        'l10n_ar_account_vat_ledger_citi',
        'account_debt_management',
        'l10n_ar_aeroo_payment_group',
        'l10n_ar_account_withholding',
        'account_ux',  # hace pilas de cosas ver en el modulo

        # utilitarios
        'auto_backup',  # poner el backup en: /var/odoo/backups/
        'due_payments_argentina_fix',
        'product_currency',
        'product_unique',

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

        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'it-projects-llc-mail-addons', 'branch': '11.0'},

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
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '11.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ]
}
