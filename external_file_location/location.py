# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2015 Akretion (http://www.akretion.com).
#   @author Valentin CHEMIERE <valentin.chemiere@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields
from abstract_task import AbstractTask
from helper import itersubclasses

class Location(models.Model):
    _name = 'external.file.location'
    _description = 'Description'

    name = fields.Char(string='Name')
    protocol = fields.Selection(selection='_get_protocol')
    address = fields.Char(string='Address')
    port = fields.Integer()
    login = fields.Char()
    password = fields.Char()
    task_ids = fields.One2many('external.file.task', 'location_id')


    def _get_protocol(self):
        res = []
        for cls in itersubclasses(AbstractTask):
            if not cls._synchronize_type:
                cls_info = (cls._key, cls._name)
                res.append(cls_info)
        return res

