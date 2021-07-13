# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MantenimientoPreventivo(models.Model):
    _inherit = ['maintenance.equipment']

    tipo_mantenimiento = fields.One2many('mantenimiento.preventivo','equipo',string="Tipo de Mantenimiento", ondelete='cascade')



class TipodePreventivo(models.Model):
    _name = ['maintenance.equipment']
    _description = "Creación de Mantenimiento Preventivo por Equipo"

    name = fields.Char(string="Tipo de Mantenimiento")
    equipo = fields.Many2one('maintenance.equipment', string="Equipo")
    refacciones = fields.Many2one('product.product', string="Refacciones")
    qty = fields.Float(string="Cantidad", default=1)
    tiempo = fields.Integer(string="Días para Siguiente Mantenimiento")

