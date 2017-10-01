
from odoo import exceptions, _
from odoo import _, api, fields, models

class res_users_extended(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    _description = 'Users Management'

    company_name = fields.Text('Company Name')
    amount = fields.Integer('Designation')

    _sql_constraints = [
        ('name_match_uniq', 'unique(match, name)', 'Participant has already bet on this match!! '),
    ]

