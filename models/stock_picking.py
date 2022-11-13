# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'cancel.motif.class']

    def action_cancel_with_motif(self):
        return self.with_context(model=self._name,model_ids=self.ids,method='action_cancel')._action_cancel_motif_wizard()

