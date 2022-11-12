# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'cancel.motif.class']

    def action_cancel(self):
        # Here we have to pay attention to pass the super method not the current or we will enter in endless vicious circle
        return self.with_context(model=self._name,model_ids=self.ids,method='_origin_action_cancel')._action_cancel_motif_wizard()

    def _origin_action_cancel(self):
        return super(StockPicking, self).action_cancel()
