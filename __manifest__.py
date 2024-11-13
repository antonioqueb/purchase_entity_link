# purchase_entity_link/__manifest__.py

{
    'name': 'Purchase Entity Link',
    'version': '1.0',
    'summary': 'Vincula órdenes de compra con diversas entidades',
    'author': 'ALPHAQUEB CONSULTING SAS',
    'category': 'Purchases',
    'depends': ['purchase', 'fleet', 'project', 'maintenance', 'hr', 'calendar'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
