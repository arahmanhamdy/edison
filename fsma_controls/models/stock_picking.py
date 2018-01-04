from odoo import models, fields


class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    lab_submission_id = fields.Many2one("lab.submission", "Lab Submission Form")
    photo_upload = fields.Binary("Photo upload")
    semi_trailer = fields.Boolean('Semi-Trailer')
    common_carrier = fields.Boolean('Common Carrier')
    ocean_container = fields.Boolean('Ocean Container')
    personal_vehicle = fields.Boolean('Personal Vehicle')
    allergen = fields.Boolean('Allergen Clearly Stated on Pallet Tag')
    foreign_odors = fields.Boolean('Foreign Odors')
    moisture = fields.Boolean('Moisture')
    pests = fields.Boolean('Pests')
    broken_glass = fields.Boolean('Broken Glass')
    substances = fields.Boolean('Substances or residues that may compromise organic integrity')
    holes= fields.Boolean('Holes in sides or bed that may compromise organic integrity')
    pallet_damage = fields.Boolean('Pallet Damage: broken/torn packaging')
    signs_of_contamination = fields.Boolean('Signs of contamination and infestation')
    number_of_broken_torn_packaging = fields.Integer('Number of broken/torn packaging')
    corrective_action = fields.Text('Corrective Action')
