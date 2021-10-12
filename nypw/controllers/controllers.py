# -*- coding: utf-8 -*-
# from odoo import http


# class Nypw(http.Controller):
#     @http.route('/nypw/nypw/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nypw/nypw/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nypw.listing', {
#             'root': '/nypw/nypw',
#             'objects': http.request.env['nypw.nypw'].search([]),
#         })

#     @http.route('/nypw/nypw/objects/<model("nypw.nypw"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nypw.object', {
#             'object': obj
#         })
