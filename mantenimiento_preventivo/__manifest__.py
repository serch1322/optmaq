# -*- coding: utf-8 -*-

{
    'name': 'Mantenimiento Preventivo y Correctivo',
    'summary': 'Creación de Mantenimiento Preventivo y Correctivo por Equipo de Mantenimiento',
    "version": "14.0.1.0.0",
    "author": "IT Reingenierias",
    'category': 'Industries',
    "website": "https://www.itreingenierias.com/",
    'depends': [
        'maintenance',
        'base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mantenimiento_equipo.xml',
    ],
    'installable': True,
}