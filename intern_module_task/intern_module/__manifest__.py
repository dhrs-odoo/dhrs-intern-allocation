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
        'views/intern_role_allocation.xml',
        'views/desk_view.xml',
        'views/equipment_view.xml',
    ],
    
    'demo' : [
        'demo/demo_data.xml',
        'demo/intern_role_demo.xml',
        'demo/fields_demo_data.xml',
        'demo/desk_demo_data.xml',
    ],
    
    'application' : True,
    'installable' : True,
    
    
}