from odoo import models, fields, api


class LabSubmission(models.Model):
    _name = "lab.submission"
    _rec_name = "id"

    product_id = fields.Many2one("product.product", "Product")
    lot_id = fields.Many2one("stock.production.lot", "Lot/Serial")
    special_instructions = fields.Text("Special Instructions", default="Do not test for listeria monocytogenes")
    salmonella_spp = fields.Boolean('Salmonella spp.', default=True)
    staphylococcus_aureus = fields.Boolean('Staphylococcus aureus', default=True)
    yeast_and_mold = fields.Boolean('Yeast and Mold', default=True)
    gluten = fields.Boolean('Gluten', default=True)
    microbial_identification = fields.Boolean('Microbial Identification')
    others = fields.Boolean('Others')
    aerobic_plate_count = fields.Boolean('Aerobic Plate Count', default=True)
    clostridium_spp = fields.Boolean('CLostridium spp.', default=True)
    coliform = fields.Boolean('Coliform', default=True)
    ecoli = fields.Boolean('E.Coli', default=True)
    ecoli_o157_h7 = fields.Boolean('E.Coli O157:H7', default=True)
    listeria_spp = fields.Boolean('Listeria spp.', default=True)
    listeria_monocytogenes = fields.Boolean('Listeria monocytogenes', default=True)
    state = fields.Selection([("pcqi", "PCQI"), ("done", "Done")], default="pcqi")
    pcqi_user_id = fields.Many2one("res.users", "PCQI By", readonly=True)
    pcqi_date = fields.Datetime("PCQI On", readonly=True)


    @api.multi
    def action_done(self):
        self.ensure_one()
        self.update({
            "state": "done",
            "pcqi_user_id": self.env.user.id,
            "pcqi_date": fields.Datetime.now()
        })
