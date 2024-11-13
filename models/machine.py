from odoo import models, fields

class Machine(models.Model):
    _name = 'machine.machine'
    _description = 'Máquina'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    # Añade más campos según tus necesidades
