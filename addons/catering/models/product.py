# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
  _inherit = 'product.product'
  
  alcohol_level = fields.Float('Alcohol level', digits=(3,2))

  @api.depends('alcohol_level')
  def _compute_taxes_id(self):
    for record in self:
      if record.alcohol_level <= 0.05:
        record.taxes_id.python_compute = "Tax 6.00%"
      elif record.alcohol_level > 0.05:
        record.taxes_id.python_compute = "Tax 21.00%"
