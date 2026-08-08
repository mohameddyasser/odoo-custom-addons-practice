# from odoo import models, fields, api


# class my_app_module(models.Model):
#     _name = 'my_app_module.my_app_module'
#     _description = 'my_app_module.my_app_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

