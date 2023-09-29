


from datetime import datetime, timedelta
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    ver_precio2= fields.Boolean(string='Ver admin2')  
    es_admin2=fields.Char(string='Admin')

 



    def action_confirm(self):
        if self.env.user.confirmar_orden_venta == True :

            if self._get_forbidden_state_confirm() & set(self.mapped('state')):
                raise UserError(_(
                    "It is not allowed to confirm an order in the following states: %s",
                    ", ".join(self._get_forbidden_state_confirm()),
                ))

            for order in self:
                if order.partner_id in order.message_partner_ids:
                    continue
                order.message_subscribe([order.partner_id.id])

            self.write(self._prepare_confirmation_values())

            # Context key 'default_name' is sometimes propagated up to here.
            # We don't need it and it creates issues in the creation of linked records.
            context = self._context.copy()
            context.pop('default_name', None)

            self.with_context(context)._action_confirm()
            if self.env.user.has_group('sale.group_auto_done_setting'):
                self.action_done()

            return True
        else:
            raise UserError(_("You do not have the right to confirm the sales order. "))     
                
    

    