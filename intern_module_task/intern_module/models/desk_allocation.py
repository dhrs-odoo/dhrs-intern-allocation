from odoo import fields,models

class deskAllocation(models.Model):
     _name = "desk.allocation"
     _description = "This is regarding the Desk allocation"
     _order="sequence"

     desk_no = fields.Integer(string = "Desk No")
     desk_type = fields.Selection(
        selection=[('straight desk', 'Straight Desk'), ('l shape', 'L Shape')],string="Desk Type"
    )
     # desk_no_ids = fields.One2many('intern.allocation','desk_no',string = 'Intern Name')
     is_assigned = fields.Boolean('Assigned')
     sequence = fields.Integer('Sequence',default=1)
     
     def name_get(self):
          res =[]
          for rec in self:
               res.append((rec.id, '%s - %s' %( rec.desk_no, rec.desk_type)))
          return res
    
    
