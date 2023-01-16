# -*- coding: utf-8 -*-
from odoo import fields,models

class Functionaltraining(models.Model):
    _name = "functional.training"
    _description = "This is regarding the intern functional training"
    
    name = fields.Char(string="Name")
    coach = fields.Char(string="Coach Name")
    coach_ids = fields.One2many("intern.allocation" , "coach", string="Coach Name")
    course_link= fields.Char("Course Link")