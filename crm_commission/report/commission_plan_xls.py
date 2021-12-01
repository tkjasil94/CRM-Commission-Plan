import base64
import io
from odoo import models


class CommissionPlanReportXlsx(models.AbstractModel):
    _name = 'report.crm_commission.report_commission_plan_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, demo):
        print("######################", data['demo'])
        # sheet = workbook.add_worksheet('Details')
        # bold = workbook.add_format({'bold': True})
        #
        # sheet.set_column('D:D', 12)
        # sheet.set_column('E:E', 15)
        #
        # row = 3
        # col = 3
        # sheet.write(row, col, 'Reference', bold)
        # sheet.write(row, col+1, 'Name', bold)
        # for rec in data['demo']:
        #     row = row + 1
        #     sheet.write(row, col, rec['name'])
        #     sheet.write(row, col + 1, rec['type'])

