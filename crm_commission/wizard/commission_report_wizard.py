from odoo import models, fields
from odoo.exceptions import ValidationError


class CommissionReportWizard(models.TransientModel):
    _name = 'commission.report.wizard'
    _description = 'Commission Report Wizard'

    sales_team_ids = fields.Many2many('crm.team', string='Sales Team')
    sales_person_ids = fields.Many2many('res.users', string='Sales Person')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')

    def print_commission_report(self):
        if self.from_date:
            if self.to_date:
                if self.from_date > self.to_date:
                    raise ValidationError(
                        'Start Date Must Be Less Than End Date')

        # # td = []
        # if self.sales_team_ids:
        #     if self.from_date:
        #         if self.to_date:
        #             sql1 = """SELECT * FROM crm_commission"""
        #             self.env.cr.execute(sql1)
        #             self.env.cr.fetchall()
        #             return self.env.ref(
        #                 'crm_commission.report_commission_plan_xlsx').report_
        #             action(self, data=data)

                # td = list(map(lambda x, y, z, w: (x, y, z, w), tr1))
    # table = ['SlNo', 'Source', 'Destination', 'State', 'Vehicle']
    # data = {
    #     'from_data': self.date_from,
    #     'to_data': self.date_to,
    #     'customer_data': self.customer_id.name,
    #     'sorted_data1': td,
    #     'table_data': table,
    #
    # }
    # return self.env.ref(
    # 'crm_commission.report_commission_plan_xlsx').report_action(
    #         self, data=data)
    #

# if self.from_date > self.to_date:
#     raise ValidationError('Start Date Must Be Less Than End Date')
# data = {
#     'form_data': self.read()[0],
# }
# return self.env.ref(
#     'crm_commission.report_commission_plan_xlsx').report_action(
#     self, data=data)
