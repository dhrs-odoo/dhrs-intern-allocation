# -*- coding: utf-8 -*-
from odoo import fields,models

class Collegeinformation(models.Model):
    _name = "college.information"
    _description = "This is regarding the intern college information"
    
    name = fields.Char(string="Name")
    cllg_name_ids = fields.One2many('intern.allocation','cllg_name',string='College Name')