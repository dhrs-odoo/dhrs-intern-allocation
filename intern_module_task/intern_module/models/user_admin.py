# -*- coding: utf-8 -*-
from odoo import fields,models

class internDesk(models.Model):
     _name = "intern.allocation"
     _description = "This is regarding the intern desk allocation"

     name = fields.Char(string='Intern Name',required = True)
     cllg_name = fields.Char(string='College Name',required = True)
     contact_details = fields.Char(string = 'Contact No',required=True)
     joining_date = fields.Date(string = 'Joining Date')
     equipment_type = fields.Many2many("equipment.allocation" , string='Equipments')
     intern_type = fields.Many2one("role.allocation",string='Intern Role')
     description = fields.Char(string='Description')
     desk_no=fields.Many2one("desk.allocation", string="Desk No")
     
     
     state = fields.Selection(selection = [('new','New'),('allocated','Allocated')],default='new')
  
     


     