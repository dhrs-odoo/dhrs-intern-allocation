from odoo import fields,models

class internRole(models.Model):
     _name = "role.allocation"
     _description = "This is regarding the intern role allocation"
     
     name = fields.Char(string='Name',required = True)