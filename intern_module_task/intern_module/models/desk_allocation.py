from odoo import fields,models

class deskAllocation(models.Model):
     _name = "desk.allocation"
     _description = "This is regarding the Desk allocation"
     _rec_name = "desk_no"

     
     name = fields.Char(string='Name')
     desk_no = fields.Char(string='Desk No')
     desk_no_ids = fields.One2many('intern.allocation','desk_no',string = 'Intern Name')
     
     # def name_get(self):
     #      res =[]
     #      for rec in self:
     #           res.append((rec.id, '%s' %( rec.desk_no)))
     #      return res
     
     