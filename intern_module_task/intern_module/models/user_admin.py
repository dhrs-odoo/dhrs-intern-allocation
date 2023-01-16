# -*- coding: utf-8 -*-
from odoo import fields,models
from odoo.exceptions import UserError , ValidationError

class internDesk(models.Model):
     _name = "intern.allocation"
     _description = "This is regarding the intern desk allocation"
     _inherit = ['mail.thread', 'mail.activity.mixin']

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
     coach = fields.Many2one("functional.training",  string = "Coach Name")
     
     
     state = fields.Selection(selection = [('pending','Pending'),('allocated','Allocated')],default='pending',tracking = True)
     status = fields.Selection(selection = [('allocated','Allocated'),('pending','Pending')])
     
     _sql_constraints = [('name_unique','UNIQUE(name)','Name must be Unique')]
  
     
     def allocated_button(self):
          for record in self:
                    record.status='allocated'
                    record.state='allocated'
     
     def pending_button(self):
          for record in self:
               if record.status == 'allocated':
                    raise UserError('You have already allocated the interns')
               else :
                    record.status == 'pending'
                    record.state  == 'pending'

     