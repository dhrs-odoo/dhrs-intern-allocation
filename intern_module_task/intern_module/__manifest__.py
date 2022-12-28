# -*- coding: utf-8 -*-

{
    'name':'Intern Management',
    'author' : 'Dhrumil Shah',
    'depends' : ['base'],
    'version' : '1.0',
    'data' : [
        'security/ir.model.access.csv',
        'views/view_intern_allocation.xml',
        'views/action_intern_allocation.xml',
        'views/intern_role_allocation.xml'
    ],
    
    'demo' : [
        'demo/demo_data.xml',
        'demo/intern_role_demo.xml',
    ],
    
    'application' : True,
    'installable' : True,
    
    
}