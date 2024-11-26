{
    'name': 'Purchase Entity Link',
    'version': '1.0',
    'summary': 'Vincula órdenes de compra con diversas entidades',
    'author': 'ALPHAQUEB CONSULTING SAS',
    'category': 'Purchases',
    'depends': ['purchase', 'fleet', 'project', 'maintenance', 'hr', 'calendar'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
}
