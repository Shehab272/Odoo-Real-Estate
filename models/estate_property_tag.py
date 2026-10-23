from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

from odoo.exceptions import ValidationError

class estate_property_tag(models.Model):
     _name = 'estate.property.tag'
     _description = 'Estate Property Tag'
     
     name = fields.Char(string='Name',required=True)



     _check_tag_name = models.Constraint(
          'UNIQUE(name)',
          'A property tag name must be unique.',
     )