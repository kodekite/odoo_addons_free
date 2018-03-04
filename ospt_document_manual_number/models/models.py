# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	manual_number = fields.Char(string="Manual Number")

	_sql_constraints = [
	    ('unq_man_number_po', 'unique(manual_number)', 'Manual Number already exists!')
	]

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	manual_number = fields.Char(string="Manual Number")

	_sql_constraints = [
	    ('unq_man_number_stock_picking', 'unique(manual_number)', 'Manual Number already exists!')
	]

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	manual_number = fields.Char(string="Manual Number")

	_sql_constraints = [
	    ('unq_man_number_so', 'unique(manual_number)', 'Manual Number already exists!')
	]
	
class AccountInvoice(models.Model):
	_inherit = 'account.invoice'

	manual_number = fields.Char(string="Manual Number")

	_sql_constraints = [
	    ('unq_man_number_inv', 'unique(manual_number)', 'Manual Number already exists!')
	]