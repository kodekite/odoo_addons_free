# -*- coding: utf-8 -*-
from odoo import http

# class Dev75DocumentManualNumber(http.Controller):
#     @http.route('/dev_75_document_manual_number/dev_75_document_manual_number/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_75_document_manual_number/dev_75_document_manual_number/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_75_document_manual_number.listing', {
#             'root': '/dev_75_document_manual_number/dev_75_document_manual_number',
#             'objects': http.request.env['dev_75_document_manual_number.dev_75_document_manual_number'].search([]),
#         })

#     @http.route('/dev_75_document_manual_number/dev_75_document_manual_number/objects/<model("dev_75_document_manual_number.dev_75_document_manual_number"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_75_document_manual_number.object', {
#             'object': obj
#         })