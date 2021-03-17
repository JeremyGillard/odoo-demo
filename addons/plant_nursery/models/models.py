# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Plants(models.Model):
  _name = 'nursery.plant'
  _description = 'Nursery Plants'

  name = fields.Char("Plant Name")
  price = fields.Float()
  image = fields.Binary("Plant Image", attachment=True)

  order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")

  order_count = fields.Integer(compute='_compute_order_count', store=True, string="Total sold")

  @api.depends('order_ids')
  def _compute_order_count(self):
    for plant in self:
      plant.order_count = len(plant.order_ids)

  nubmer_in_stock = fields.Integer()

  @api.constrains('order_count', 'number_in_stock')
  def _check_available_in_stock(self):
    for plant in self:
      if plant.number_in_stock and plant.order_count > plant.number_in_stock:
        raise UserError(f'There is only {plant.number_in_stock} {plant.name} in stock but {plant.order_count} were sold')


class Customer(models.Model):
  _name = 'nursery.customer'
  _description = 'Nursery Customers'

  name = fields.Char("Customer Name", required=True)
  email = fields.Char(help="To receive the newsletter")


class Order(models.Model):
  _name = 'nursery.order'
  _description = 'Nursery Orders'

  name = fields.Datetime(default=fields.Datetime.now)
  plant_id = fields.Many2one("nursery.plant", required=True)
  customer_id = fields.Many2one("nursery.customer")
  state = fields.Selection([
    ('draft', 'Draft'),
    ('confirm', 'Confirmed'),
    ('cancel', 'Canceled')
  ], default='draft')
  last_modification = fields.Datetime(readonly=True)

  def write(self, values):
    values['last_modification'] = fields.Datetime.now()

    return super(Order, self).write(values)

  def unlink(self):
    for order in self:
      if order.state == 'confirm':
        raise UserError('You can not delete confirmed orders')

    return super(Order, self).unlink()

