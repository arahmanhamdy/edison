from odoo import models, fields, api


class RestroomLog(models.Model):
    _name = "restroom.log"
    _rec_name = "id"

    select_options = [
        ("chk", "Checked"),
        ("fill", "Filled"),
    ]

    bathroom = fields.Integer("Bathroom #")
    is_toilets_cleaned = fields.Boolean("Toilets Cleaned")
    is_mirrors_cleaned = fields.Boolean("Mirrors Cleaned")
    is_sinks_cleaned = fields.Boolean("Sinks Cleaned")
    is_floors_mopped = fields.Boolean("Floors Mopped")
    is_floors_swept = fields.Boolean("Floors Swept")
    toilet_paper = fields.Selection(select_options, "Toilet paper")
    paper_towels = fields.Selection(select_options, "Paper Towels")
    seat_covers = fields.Selection(select_options, "Seat Covers")
    soap_dispenser = fields.Selection(select_options, "Soap Dispenser")
    trash = fields.Selection([("chk", "Checked"), ("emp", "Emptied")], "Trash")

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
