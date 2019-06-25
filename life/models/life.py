# For copyright and license notices, see __manifest__.py file in module root

from odoo import api, fields, models
import datetime as dt

#este es el code que aparece en ntsw
#M1805047502205

# password cript for admin id = 28
# $pbkdf2-sha512$25000$Y8yZ8z7HeC8F4HzvXWstRQ$oTBGJDQRNyqwXw0rAMnQk1vjJeEwvJFrhOD/fD2TNosISgMDz2f1JSXTXo/1fPeP/yMF.B2MHWll4O26X7CQ7w

class Life(models.TransientModel):
    _name = 'lifes'

    def extend_life(self):
        config_obj = self.env['ir.config_parameter'].sudo()

        # eliminar el codigo de activacion
        domain = [('key', '=', 'database.enterprise_code')]
        config = config_obj.search(domain)
        if config:
            config.unlink()

        # pasar a trail
        config.set_param('database.expiration_reason', 'trail')

        # actualizar fecha
        date = dt.datetime.now() + dt.timedelta(days=28)
        date = date.strftime('%Y-%m-%d 00:00:00')
        config.set_param('database.expiration_date', date)
