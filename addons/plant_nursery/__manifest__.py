# -*- coding: utf-8 -*-
{
    'name': "Plant Nursery",
    'version': '1.0',
    'category': 'Tools',
    'summary': "Plants and customers management",
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/nursery_views.xml',
        'views/nursery_plant_views.xml',
        'views/nursery_customer_views.xml',
        'views/nursery_order_views.xml'
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
