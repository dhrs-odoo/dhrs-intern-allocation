# -*- coding: utf-8 -*-

{
    'name':'Intern OnBoarding',
    'author' : 'Dhrumil Shah',
    'depends' : ['base','mail'],
    'version' : '1.0',
    'category' : 'Intern Allocation/Roles',
    'data' : [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/intern_allocation_view.xml',
        'views/action_intern_allocation.xml',
        'views/view_ intern_role_allocation.xml',
        'views/desk_allocation_view.xml',
        'views/laptop_allocation_view.xml',
        'views/view_equipment.xml',
        'views/college_information_view.xml',
        'views/document_upload_view.xml',
        'views/res_users_view.xml',
    ],
    
    'demo' : [
        'demo/laptop_demo_data.xml',
        'demo/intern_allocation_demo_data.xml',
        'demo/intern_role_demo.xml',
        'demo/desk_demo_data.xml',
        'demo/other_equipment_demo_data.xml',
        'demo/cllg_demo_data.xml',
    ],
    
    'application' : True,
    'installable' : True,
    'license' : 'LGPL-3',
    
    
}