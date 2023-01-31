# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class internDesk(models.Model):
    _name = "intern.allocation"
    _description = "This is regarding the intern Orientation"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Intern Name', required=True)
    cllg_name = fields.Many2one('college.information', string='College Name')
    contact_details = fields.Char(string='Work Mobile', required=True)
    joining_date = fields.Date(string='Joining Date')
    laptop_assigned = fields.Many2one(
        "laptop.allocation", string='Laptop Assigned', tracking=True)
    intern_type = fields.Many2one("role.allocation", string='Intern Role')
    description = fields.Char(string='Description')
    desk_no = fields.Many2one("desk.allocation", string="Desk No",tracking=True,domain="[('is_assigned','=',False)]")
    other_equipments = fields.Many2many(
        "equipment.allocation", string="Other Equipments")
    email_id = fields.Char(string='Work Email')
    coach = fields.Many2one(
        "coach.coach",  string="Coach Name", tracking=True)
    evaluation_ids = fields.One2many(
        'evaluation.evaluation', 'intern_allocation_id', string="evaluation")
    personal_module_ids = fields.One2many(
        'personal.module', 'intern_personal_id', string="Personal Module")

    state = fields.Selection(selection=[('new', 'New'), ('functional', 'Functional Training'), ('backend', 'Odoo Backend'), (
        'frontend', 'Odoo Frontend'), ('owl', 'Owl JS'), ('done', 'Done')], tracking=True, default="new")
    status = fields.Selection(selection=[('allocated', 'Allocated')])
    intern_img = fields.Binary()
    department = fields.Selection(selection=[('r&d','Research & Development'),('offshore','Offshore'),('upgrade','Upgrade')],string="Department")
    document_ids = fields.One2many('document.document','document_id')
    password = fields.Char('Password')
    requirement = fields.Selection (selection=[('project', 'Project'), ('report', 'Weekly Report'),
                   ('none', 'None')],default="none",string="Requirement of college")
    project_name = fields.Char(string="Project Name")
    
    
    is_readonly = fields.Boolean('Readonly',default=False,compute ="_is_readonly")

    

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Name must be Unique')]


        # For auto allocating the desk
    def allocated_button(self):
        for record in self:
          domain = ['is_assigned', '=', False]
          records = self.env['desk.allocation'].search([domain])
          if len(records):
               record.desk_no = records[0]
               records[0].is_assigned = True
          else:
               raise ValidationError("You don't have desk available to assign.")
               
          
          if record.desk_no:
               record.status = 'allocated'
               record.state = 'functional'
          else:
               raise UserError('You need to assign seat no first')            
    
    @api.model 
    def create(self,vals):
            id = self.env['res.users'].search([('name','=',vals['name'])]).id
            if not id:
                self.env['res.users'].create({
                    'name': vals['name'],
                    'login':vals['email_id'],
                    'password':vals['password']
                })
            return super(internDesk,self).create(vals)
        
    def _is_readonly(self):
        for rec in self:
            usr = self.env['res.users'].browse(self.env.uid)
            if usr.has_group('intern_module.intern_group_user'):
                rec.is_readonly = True
            else:
                rec.is_readonly = False
    attrs="{'readonly':[('is_readonly','=',True)]}"