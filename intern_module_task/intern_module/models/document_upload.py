# -*- coding: utf-8 -*-
from odoo import fields,models

class Collegeinformation(models.Model):
    _name = "document.document"
    _description = "This is regarding the intern weekly report document"
    
    document_id = fields.Many2one('intern.allocation')
    document_name = fields.Char(string = "File Name")
    weekly_report_upload = fields.Binary(string="Weekly Report", store=True) 
    week_report_no = fields.Integer('Week No.')  