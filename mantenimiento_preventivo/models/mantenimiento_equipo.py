# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, date, timedelta


class MantenimientoPreventivo(models.Model):
    _inherit = 'maintenance.equipment'

    tipo_mantenimiento = fields.One2many('mantenimiento.preventivo','equipo',string="Tipo de Mantenimiento", ondelete='cascade')
    
    def mantenimiento_correctivo(self):
        correctivo = self.env['maintenance.request']
        valores_equipo = {}
        valores_equipo.update({
            'name': "Mantenimiento Correctivo",
            'equipment_id': self.id,
            'request_date': date.today(),
            'type': 'corrective',
            'maintenance_team_id': self.maintenance_team_id.id,
            'user_id': self.technician_user_id.id,
            'scheduled_date': date.today(),
        })
        mante_creado = correctivo.create(valores_equipo)
        return{
             'type': 'ir.actions.act_window',
             'res_model': 'maintenance.request',
             'view_type': 'form',
             'view_mode': 'tree,form',
             'target': 'self',
        }



class TipodePreventivo(models.Model):
    _name = 'mantenimiento.preventivo'

    name = fields.Char(string="Tipo de Mantenimiento")
    equipo = fields.Many2one('maintenance.equipment', string="Equipo")
    tiempo = fields.Integer(string="Días para Siguiente Mantenimiento")
    refacciones = fields.One2many('mantenimiento.refacciones', 'refaccion',string="Refacciones", ondelete='cascade')


class Refacciones(models.Model):
    _name = 'mantenimiento.refacciones'

    name = fields.Many2one('product.product', string="Refacciones")
    qty = fields.Float(string="Cantidad", default=1)
    refaccion = fields.Many2one('mantenimiento.preventivo',string="Refaccion")

