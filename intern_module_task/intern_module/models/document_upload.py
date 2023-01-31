# -*- coding: utf-8 -*-
from odoo import fields,models

class Collegeinformation(models.Model):
    _name = "document.document"
    _description = "This is regarding the intern weekly report document"
    
    document_id = fields.Many2one('intern.allocation')
    document_name = fields.Char(string = "File Name")
    # requirement = fields.Selection(
    #     selection=[('project', 'Project'), ('report', 'Weekly Report'),
    #                ('none', 'None')],default="none",string="Requirement of college")
    weekly_report_upload = fields.Binary(string="Weekly Report", store=True) 
    week_report_no = fields.Integer('Week No.')  
    # project_name = fields.Char(string="Project Name")
    
    # project_requirement= fields.Selection(
    #     selection=[('yes', 'Yes'), ('no', 'No'),
    #                ],default="no",string="Project Requirement")