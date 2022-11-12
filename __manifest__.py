# -*- coding: utf-8 -*- 


{
    'name': 'Transfers cancel motif',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Stock',
    'demo': [],
    'depends': ['stock','cancel_motif'],
    'data': [
        'views/cancel_motif_views.xml',
        'views/stock_picking_views.xml'
    ],
    'license': 'LGPL-3',
}
