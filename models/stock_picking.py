# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'cancel.motif.class']

    cancel_motif = fields.Text(string="Cancel motif",compute='_compute_cancel_motif',store=True)

    @api.depends('cancel_motif_id')
    def _compute_cancel_motif(self):
        for each in self:
            each.cancel_motif = each.cancel_motif_id.description or each.cancel_motif_id.name

    def action_cancel_with_motif(self):
        return self.with_context(model=self._name,model_ids=self.ids,method='action_cancel')._action_cancel_motif_wizard()

