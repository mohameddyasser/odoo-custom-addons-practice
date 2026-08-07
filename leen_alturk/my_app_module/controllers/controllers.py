# from odoo import http


# class MyAppModule(http.Controller):
#     @http.route('/my_app_module/my_app_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_app_module/my_app_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_app_module.listing', {
#             'root': '/my_app_module/my_app_module',
#             'objects': http.request.env['my_app_module.my_app_module'].search([]),
#         })

#     @http.route('/my_app_module/my_app_module/objects/<model("my_app_module.my_app_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_app_module.object', {
#             'object': obj
#         })

