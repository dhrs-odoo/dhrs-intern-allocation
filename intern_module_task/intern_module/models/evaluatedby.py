from odoo import fields,models

class equipmentAllocation(models.Model):
     _name = "evaluatedby.evaluatedby"
     _description = "This is regarding the equipment allocation"
     
     name = fields.Char(string='Name',required = True)
     