from odoo import fields,models

class equipmentAllocation(models.Model):
     _name = "equipment.allocation"
     _description = "This is regarding the equipment allocation"
     
     name = fields.Char(string='Name',required = True)
     technician_name = fields.Char(string = 'Technician Name')
     model = fields.Char(string='Model')
     location = fields.Char(string = 'Used in Location')
     war_expire =fields.Date(string='Warranty Expiration Date')
     mac_address=fields.Char(string="Mac Address")
     color = fields.Integer()