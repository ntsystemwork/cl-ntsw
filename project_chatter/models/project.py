from odoo import api, fields, models
import datetime
from datetime import timedelta

class project(models.Model):
    _inherit = ["project.project", "mail.activity.mixin"]
