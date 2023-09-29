# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

from datetime import timedelta
from itertools import groupby
from markupsafe import Markup

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError




class ButtonConfirm_add_user(models.Model):
    _inherit = 'res.users'
    confirmar_orden_venta= fields.Boolean(string='Confirm Sale Order', help="Allows the user confirm order") 
   





