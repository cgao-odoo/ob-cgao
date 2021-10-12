# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nypw(models.Model):
    _name = 'nypw.nypw'
    _description = 'nypw.nypw'

    name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    pairs_per_case = fields.Float(compute="_value_pc", store=True)
    price_per_pair = fields.Float(compute="_value_pc", store=True)
    sales_price = fields.Float(compute="_value_pc", store=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
