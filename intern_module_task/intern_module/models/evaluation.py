from odoo import fields,models

class deskAllocation(models.Model):
     _name = "evaluation.evaluation"
     _description = "This is regarding the Desk allocation"
     
     
    #  name = fields.Char(string='Name')
     week = fields.Integer(string = 'week')
     odoo_concept = fields.Char(string="Odoo Concept")
    #  code_quality = fields.Many2many(string="Code Quality")
    #  productivity = fields.Many2many(string = "Productivity")
     interaction = fields.Char(string = "Interaction" )
    #  evaluated = fields.Many2many(string = "Evaluated By")
     remarks = fields.Text(string = "Remarks")
     user_admin_id = fields.Many2one('intern.allocation')