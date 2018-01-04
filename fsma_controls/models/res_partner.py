from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    organic_certification = fields.Binary('Organic Certification')
    organic_cert_issue_date = fields.Date('Organic Cert. Issue Date')
    organic_cert_expiration_date = fields.Date('Organic Cert. Expiration Date')
    food_safety_certificate = fields.Binary('Food Safety Certificate')
    food_safety_certificate_exp_date = fields.Date('Food Safety Certificate Exp. Date')
    third_party_audit_date = fields.Date('3rd Party Audit Date')
    third_party_report_reviewed = fields.Date('3rd Party Report Reviewed')
    annual_approval_date = fields.Date('Annual Approval Date')
    comments = fields.Text('Comments')
    specs = fields.Boolean('Specs')
    allergen_statement = fields.Boolean('Allergen Statement')
    gluten_cert_exp_date = fields.Date('Gluten Cert. Exp Date')
    vendor_questionnaire = fields.Boolean('Vendor Questionnaire')
    nutrition_data = fields.Boolean('Nutrition Data')
    aflatoxin_statement = fields.Boolean('Aflatoxin Statement')
    letter_of_guarantee = fields.Boolean('Letter of Guarantee')
    letter_of_guarantee_date = fields.Date('Letter of Guarantee Date')
    reg_compliance_review = fields.Boolean('Reg. Compliance Review')
