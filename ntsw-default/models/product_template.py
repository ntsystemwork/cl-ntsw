# -*- coding: utf-8 -*-
# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields, api, _


@api.multi
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def fix_template(self):
        for prod in self.search([]):
            prod.force_currency_id = 3


@api.multi
class ResPartner(models.Model):
    _inherit = 'res.partner'

    def fix_partner(self):
        """ cambiar la lista 8 IMPO-DOLAR 2019 USD (que estaba archivada) por
            la 30 IMPO-DOLAR 2019
        """
        pricelist = self.env['product.pricelist'].search([('id', '=', 30)])
        for partner in self.search([]):
            if partner.property_product_pricelist.id == 8:
                partner.property_product_pricelist = pricelist
