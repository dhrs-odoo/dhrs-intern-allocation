from odoo import fields,models

class deskAllocation(models.Model):
     _name = "desk.allocation"
     _description = "This is regarding the Desk allocation"

     
     name = fields.Char(string='Name')
     desk_no = fields.Char(string='Desk No')
     
     def name_get(self):
          res =[]
          for rec in self:
               res.append((rec.id, '%s - %s' %(rec.name, rec.desk_no)))
          return res
     
     