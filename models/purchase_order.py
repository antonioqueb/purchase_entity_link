from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    entity_type = fields.Selection([
        ('machine', 'Máquina'),
        ('user', 'Usuario'),
        ('event', 'Evento'),
        ('project', 'Proyecto'),
        ('task', 'Tarea'),
        ('fleet', 'Flota'),
    ], string='Tipo de Entidad')

    machine_id = fields.Many2one('machine.machine', string='Máquina')
    user_id = fields.Many2one('res.users', string='Usuario')
    event_id = fields.Many2one('calendar.event', string='Evento')
    project_id = fields.Many2one('project.project', string='Proyecto')
    task_id = fields.Many2one('project.task', string='Tarea')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehículo')

    @api.constrains('entity_type')
    def _check_entity(self):
        for record in self:
            if record.entity_type == 'machine' and not record.machine_id:
                raise ValidationError('Debe seleccionar una Máquina.')
            if record.entity_type == 'user' and not record.user_id:
                raise ValidationError('Debe seleccionar un Usuario.')
            if record.entity_type == 'event' and not record.event_id:
                raise ValidationError('Debe seleccionar un Evento.')
            if record.entity_type == 'project' and not record.project_id:
                raise ValidationError('Debe seleccionar un Proyecto.')
            if record.entity_type == 'task' and not record.task_id:
                raise ValidationError('Debe seleccionar una Tarea.')
            if record.entity_type == 'fleet' and not record.vehicle_id:
                raise ValidationError('Debe seleccionar un Vehículo.')
