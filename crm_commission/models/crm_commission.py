from odoo import api, fields, models


class CrmCommission(models.Model):
    _name = 'crm.commission'
    _description = "CRM Commission"

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active')
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')
    type = fields.Selection([
        ('product wise', 'Product Wise'),
        ('revenue wise', 'Revenue Wise')], required=True, string='Type')
    from_amount = fields.Float(string='From Amount')
    to_amount = fields.Float(string='To Amount')
    rate_percent = fields.Integer(string='Rate Percentage')
    sequence_no = fields.Char('CRM Commission', required=True, index=True,
                              copy=False, default='New')
    revenue_type = fields.Selection([
        ('straight', 'Straight'),
        ('graduated', 'Graduated')], default='straight', string='Revenue Type')
    product_line_ids = fields.One2many('product.list', 'reference_id',
                                       string='Product Line')
    total_revenue = fields.Float(string='Total Revenue',
                                 compute='_compute_total_revenue')
    commission_amt = fields.Float(string='Commission Amount',
                                  compute='_compute_commission_amt')

    @api.model
    def create(self, vals):
        vals['sequence_no'] = self.env['ir.sequence'].next_by_code(
            'crm.commission')
        return super(CrmCommission, self).create(vals)

    @api.depends('from_amount', 'to_amount')
    def _compute_total_revenue(self):
        for rec in self:
            rec.total_revenue = rec.to_amount - rec.from_amount

    @api.depends('from_amount', 'to_amount', 'rate_percent', 'product_line_ids')
    def _compute_commission_amt(self):
        if self.type == 'product wise':
            for line in self.product_line_ids:
                self.commission_amt += (line.percentage_rate * line.max_amount)/100
        else:
            self.commission_amt = (self.to_amount - self.from_amount) * self.rate_percent / 100


class SalesTeamInherit(models.Model):
    _inherit = 'crm.team'

    sales_team_id = fields.Many2one('crm.commission', string='Commission Plan')


# class SalesPersonInherit(models.Model):
#     _inherit = 'res.users'
#
#     sales_person_id = fields.Many2one('crm.commission',
#                                       string='Commission Plan')


class ProductWiseList(models.Model):
    _name = 'product.list'

    product_category_id = fields.Many2one('product.category',
                                          string='Product Category')
    product_id = fields.Many2one('product.product', string='Product')
    percentage_rate = fields.Float(string='Rate of Percentage')
    max_amount = fields.Float(string='Max Commission Amount')
    reference_id = fields.Many2one('crm.commission', string='Reference ID')
