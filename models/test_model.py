from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.module'
    _description = 'Modulo di Test con una lista di nomi'

    name = fields.Char(string='Nome')
