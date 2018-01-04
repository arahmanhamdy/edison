from odoo import models, fields, api


class ForeignMaterial(models.Model):
    _name = "foreign.material"
    _rec_name = "id"

    select_options = [
        ("pass", "Pass"),
        ("fail", "Fail"),
    ]

    product_id = fields.Many2one("product.product", "Product")
    lot_id = fields.Many2one("stock.production.lot", "Lot/Serial")
    log = fields.Selection([("ams", "AMS"), ("act", "Action Pac")], "Log")
    order_id = fields.Many2one("mrp.production", "Manufacturing Order")
    blue_card = fields.Selection(select_options, 'BLUE CARD - Stainless 5.556 mm')
    yellow_card = fields.Selection(select_options, 'YELLOW CARD- Ferrous 2.5 mm')
    red_card = fields.Selection(select_options, 'RED CARD- Non-Ferrous 5.5 mm')
    findings = fields.Text('Findings')
    corrective_action = fields.Text('CORRECTIVE ACTION')
    metal_object_retained = fields.Text('METAL OBJECT RETAINED')
    rejects = fields.Integer('Rejects')
    poundage_destroyed = fields.Float('Poundage Destroyed')
    detection_method = fields.Text('Detection Method')
    evidence = fields.Text('Evidence')

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
