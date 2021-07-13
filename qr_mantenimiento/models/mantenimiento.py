# -*- coding: utf-8 -*-

import qrcode
import base64

from io import BytesIO

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class QRMantenimiento(models.Model):
    _inherit = ['maintenance.equipment']

    codigo_qr = fields.Binary('Codigo QR')

    def generar_qr(self):
        if self.id:
            data = self.id
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data("%s/web#id=%s&action=344&model=c&view_type=form&cids=1&menu_id=227"%(base_url,data))
            qr.make(fit=True)
            img = qr.make_image()
            tmp = BytesIO()
            img.save(tmp, format="PNG")
            qr_img = base64.b64encode(tmp.getvalue())
            self.codigo_qr = qr_img
        else:
            None