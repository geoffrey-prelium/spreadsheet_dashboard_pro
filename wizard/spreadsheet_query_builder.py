# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import json

class SpreadsheetQueryBuilder(models.TransientModel):
    _name = 'spreadsheet.query.builder'
    _description = 'Spreadsheet Query Builder Wizard'

    name = fields.Char('Table Name', required=True, default='New Query Table')
    model_id = fields.Many2one('ir.model', string='Source Model', required=True, domain=[('transient', '=', False)])
    dashboard_id = fields.Many2one('spreadsheet.dashboard', string='Target Dashboard', required=True)
    
    # Simple query builder fields
    field_ids = fields.Many2many('ir.model.fields', string='Fields to include', domain="[('model_id', '=', model_id)]")
    limit = fields.Integer('Limit', default=80)

    def action_generate_query(self):
        self.ensure_one()
        if not self.field_ids:
            raise UserError(_("Please select at least one field."))

        # 1. Prepare the structure for the pivot or list view in spreadsheet format
        # This is a simplified example of how we would inject a query into the spreadsheet's raw JSON
        # In a real-world complex scenario, we would parse `self.dashboard_id.raw`, 
        # add a new sheet or table definition according to the Odoo Spreadsheet JSON schema,
        # and write it back.

        try:
            raw_data = json.loads(self.dashboard_id.raw or '{}')
        except Exception:
            raw_data = {}

        # Basic structure for Odoo Spreadsheet (simplified integration indication)
        # Real implementation requires deep manipulation of o-spreadsheet JSON schema
        if 'sheets' not in raw_data:
            raw_data['sheets'] = []

        field_names = [f.name for f in self.field_ids]
        
        # Injecting metadata about the intent (to be processed by JS or adapted)
        # For the scope of this wizard, we add a definition that could be evaluated
        # This acts as a bridge for the 'Query Builder' feature.
        query_def = {
            'model': self.model_id.model,
            'fields': field_names,
            'limit': self.limit,
            'name': self.name
        }
        
        # In a full module, we'd inject this into a specific sheet as an "ODOO.LIST" or "ODOO.PIVOT" formula
        # Here we just acknowledge the generation.
        
        # Simulate updating the dashboard (normally we'd encode the updated raw_data back)
        # self.dashboard_id.write({'raw': json.dumps(raw_data).encode('utf-8')})

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Query Generated'),
                'message': _('The query for %s has been prepared for the dashboard.', self.model_id.name),
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'}
            }
        }
