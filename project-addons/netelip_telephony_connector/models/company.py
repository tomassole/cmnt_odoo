# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2019 Comunitea All Rights Reserved
#    $Omar Castiñeira Saavedra <omar@comunitea.com>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class ResCompany(models.Model):

    _inherit = "res.company"

    netelip_api_key = fields.Char("Netelip API Key")


class BaseConfigSettings(models.TransientModel):

    _inherit = 'base.config.settings'

    netelip_api_key = fields.Char("Netelip API Key",
                                  default=lambda s: s.env.user.company_id.
                                  netelip_api_key)

    @api.multi
    def set_netelip_api_key(self):
        self.env.user.company_id.netelip_api_key = self.netelip_api_key
