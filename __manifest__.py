# -*- coding: utf-8 -*-
{
    'name': "Spreadsheet Dashboard Pro",
    'summary': "Facilite la création de tableaux de bord avec Odoo Spreadsheet.",
    'description': """
        Ce module ajoute des fonctionnalités avancées pour Odoo Spreadsheet Dashboard :
        - Des modèles (Templates) prêts à l'emploi.
        - Un assistant générateur de requêtes pour faciliter la création de tableaux sans code.
    """,
    'author': "Geoffrey Prelium",
    'website': "https://github.com/geoffrey-prelium",
    'category': 'Productivity/Documents',
    'version': '1.0',
    'depends': ['base', 'spreadsheet_dashboard'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/spreadsheet_query_builder_views.xml',
        'views/spreadsheet_dashboard_template_views.xml',
        'views/spreadsheet_dashboard_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
