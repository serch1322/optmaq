# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MantenimientoPreventivo(models.Model):
    _inherit = 'maintenance.equipment'

    tipo_mantenimiento = fields.One2many('mantenimiento.preventivo','equipo',string="Tipo de Mantenimiento", ondelete='cascade')

class TipodePreventivo(models.Model):
    _name = 'mantenimiento.preventivo'

    name = fields.Char(string="Tipo de Mantenimiento")
    equipo = fields.Many2one('maintenance.equipment', string="Equipo")
    tiempo = fields.Integer(string="Días para Siguiente Mantenimiento")
    refacciones = fields.One2many('mantenimiento.refacciones', 'refaccion',string="Tipo de Refacciones", ondelete='cascade')


class Refacciones(models.Model):
    _name = 'mantenimiento.refacciones'

    name = fields.Many2one('product.product', string="Refacciones")
    qty = fields.Float(string="Cantidad", default=1)
    refaccion = fields.Many2one('mantenimiento.preventivo',string="Refaccion")

