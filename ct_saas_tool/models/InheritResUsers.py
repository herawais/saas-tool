# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import AccessDenied, AccessError
import logging
_logger = logging.getLogger(__name__)


class Users(models.Model):
    _inherit = "res.users"

    @api.model
    def _check_credentials(self, password,env):
        """ Override this method to plug additional authentication methods"""
        try:
            super(Users, self).check_credentials(password,env)
        except Exception as e:
            user = self.sudo().search([('id', '=', self._uid), ('password', '=', password)])
            if not user:
                raise AccessDenied()
