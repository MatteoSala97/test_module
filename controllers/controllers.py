# -*- coding: utf-8 -*-
# from odoo import http


# class /odoo/custom/testModule(http.Controller):
#     @http.route('//odoo/custom/test_module//odoo/custom/test_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/custom/test_module//odoo/custom/test_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/custom/test_module.listing', {
#             'root': '//odoo/custom/test_module//odoo/custom/test_module',
#             'objects': http.request.env['/odoo/custom/test_module./odoo/custom/test_module'].search([]),
#         })

#     @http.route('//odoo/custom/test_module//odoo/custom/test_module/objects/<model("/odoo/custom/test_module./odoo/custom/test_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/custom/test_module.object', {
#             'object': obj
#         })
