# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /odoo/custom/test_module(models.Model):
#     _name = '/odoo/custom/test_module./odoo/custom/test_module'
#     _description = '/odoo/custom/test_module./odoo/custom/test_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
