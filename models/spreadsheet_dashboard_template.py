# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SpreadsheetDashboardTemplate(models.Model):
    _name = 'spreadsheet.dashboard.template'
    _description = 'Spreadsheet Dashboard Template'
    _order = 'sequence, id'

    name = fields.Char('Template Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    dashboard_group_id = fields.Many2one('spreadsheet.dashboard.group', string='Dashboard Group', required=True)
    raw_data = fields.Binary('Spreadsheet Data', attachment=True, required=True, help="Odoo Spreadsheet JSON data")
    preview_image = fields.Binary('Preview Image')
    description = fields.Text('Description')

    def action_instantiate_dashboard(self):
        """ Creates a new dashboard from this template """
        self.ensure_one()
        dashboard = self.env['spreadsheet.dashboard'].create({
            'name': f"{self.name} (Copy)",
            'dashboard_group_id': self.dashboard_group_id.id,
            'raw': self.raw_data,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'action_spreadsheet_dashboard',
            'params': {
                'spreadsheet_id': dashboard.id,
            }
        }
