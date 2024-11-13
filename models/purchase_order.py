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
    ], string='Tipo de Entidad', default='machine')

    machine_id = fields.Many2one('machine.machine', string='Máquina')
    user_id = fields.Many2one(
        'res.users', 
        string='Usuario', 
        domain="[('active', '=', True)]"  # Mostrar todos los usuarios activos
    )
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

    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)
        for record in self:
            if 'entity_type' in vals:
                entity_label = dict(self._fields['entity_type'].selection).get(vals['entity_type'])
                record.message_post(body=f"El tipo de entidad cambió a: {entity_label}")

            # Registrar cambios en las vinculaciones según el tipo de entidad
            if 'machine_id' in vals and record.entity_type == 'machine':
                machine_name = record.machine_id.name if record.machine_id else 'Sin Máquina asignada'
                record.message_post(body=f"Máquina vinculada cambiada a: {machine_name}")
            if 'user_id' in vals and record.entity_type == 'user':
                user_name = record.user_id.name if record.user_id else 'Sin Usuario asignado'
                record.message_post(body=f"Usuario vinculado cambiado a: {user_name}")
            if 'event_id' in vals and record.entity_type == 'event':
                event_name = record.event_id.name if record.event_id else 'Sin Evento asignado'
                record.message_post(body=f"Evento vinculado cambiado a: {event_name}")
            if 'project_id' in vals and record.entity_type == 'project':
                project_name = record.project_id.name if record.project_id else 'Sin Proyecto asignado'
                record.message_post(body=f"Proyecto vinculado cambiado a: {project_name}")
            if 'task_id' in vals and record.entity_type == 'task':
                task_name = record.task_id.name if record.task_id else 'Sin Tarea asignada'
                record.message_post(body=f"Tarea vinculada cambiada a: {task_name}")
            if 'vehicle_id' in vals and record.entity_type == 'fleet':
                vehicle_name = record.vehicle_id.name if record.vehicle_id else 'Sin Vehículo asignado'
                record.message_post(body=f"Vehículo vinculado cambiado a: {vehicle_name}")
        return res
