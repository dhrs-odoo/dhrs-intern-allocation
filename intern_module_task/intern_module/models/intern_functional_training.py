# -*- coding: utf-8 -*-
from odoo import fields,models

class Coach(models.Model):
    _name = "coach.coach"
    _description = "This is regarding the intern functional training"
    
    name = fields.Char(string="Name")
    coach = fields.Char(string="Coach Name")
    coach_ids = fields.One2many("intern.allocation" , "coach", string="Coach")
    course_link= fields.Char("Course Link")