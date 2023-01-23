# -*- coding: utf-8 -*-

{
    'name':'Intern Management',
    'author' : 'Dhrumil Shah',
    'depends' : ['base','mail'],
    'version' : '1.0',
    'data' : [
        'security/ir.model.access.csv',
        'views/view_intern_allocation.xml',
        'views/action_intern_allocation.xml',
        'views/intern_role_allocation.xml',
        'views/desk_view.xml',
        'views/laptop_view.xml',
        'views/view_equipment.xml',
        'views/functional_training_view.xml',
        'views/college_information_view.xml',
    ],
    
    'demo' : [
        'demo/laptop_demo_data.xml',
        'demo/fields_demo_data.xml',
        'demo/intern_role_demo.xml',
        'demo/desk_demo_data.xml',
        'demo/other_equipment_demo_data.xml',
        'demo/evaluatedby_demo_data.xml',
        'demo/coach_demo_data.xml',
    ],
    
    'application' : True,
    'installable' : True,
    'license' : 'LGPL-3',
    
    
}