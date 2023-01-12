# -*- coding: utf-8 -*-
from odoo import fields,models
from odoo.exceptions import UserError

class internDesk(models.Model):
     _name = "intern.allocation"
     _description = "This is regarding the intern desk allocation"

     name = fields.Char(string='Intern Name',required = True)
     cllg_name = fields.Char(string='College Name',required = True)
     contact_details = fields.Char(string = 'Contact No',required=True)
     joining_date = fields.Date(string = 'Joining Date')
     laptop_assigned = fields.Many2one("laptop.allocation" , string='Laptop Assigned')
     intern_type = fields.Many2one("role.allocation",string='Intern Role')
     description = fields.Char(string='Description')
     desk_no=fields.Many2one("desk.allocation", string="Desk No")
     other_equipments = fields.Many2many("equipment.allocation" , string="Other Equipments")
     email_id = fields.Char(string = 'Email-Id')
     
     
     state = fields.Selection(selection = [('pending','Pending'),('allocated','Allocated')],default='pending')
     status = fields.Selection(selection = [('allocated','Allocated'),('pending','Pending')])
  
     
     def allocated_button(self):
          for record in self:
                    record.status='allocated'
                    record.state='allocated'
     
     def pending_button(self):
          for record in self:
               if record.status == 'allocated':
                    raise UserError('You have already allocated the interns')

     