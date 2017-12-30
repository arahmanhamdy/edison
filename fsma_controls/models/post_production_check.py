from odoo import models, fields


class PostProductionCheck(models.Model):
    _name = "post.production.check"
    _rec_name = "id"

    select_options = [
        ("acc", "Acceptable inspection"),
        ("dev", "Deviation noted requires Corrective Action"),
    ]
    poor_health = fields.Selection(select_options, 'Poor Health')
    designated_uniform = fields.Selection(select_options, 'Designated uniform')
    handle_with_care = fields.Selection(select_options, 'Handle with care')
    use_sanitizer = fields.Selection(select_options, 'Use Sanitizer')
    outer_garments_requirments = fields.Selection(select_options, 'Outer Garments requirments')
    no_smoking = fields.Selection(select_options, 'No smoking')
    designated_area_for_meds = fields.Selection(select_options, 'Designated area for meds')
    supply_products = fields.Selection(select_options, 'Supply products')
    hand_wash_facilities = fields.Selection(select_options, 'Hand wash facilities')
    prevent_contamination = fields.Selection(select_options, 'Prevent Contamination')
    equipment_are_cleaned_and_sanitized = fields.Selection(select_options, 'Equipment are cleaned and sanitized')
    wipe_dry_equipment = fields.Selection(select_options, 'Wipe Dry equipment')
    ensure_sanitizing_conveyor_belt = fields.Selection(select_options, 'Ensure Sanitizing conveyor belt')
    maintain_inventory = fields.Selection(select_options, 'Maintain Inventory')
    malfunctioning_pieces = fields.Selection(select_options, 'Malfunctioning pieces')
    disassemble_clean_sanitize = fields.Selection(select_options, 'Disassemble, clean & sanitize.')
    disassemble_parts_and_sanitize = fields.Selection(select_options, 'Disassemble parts and sanitize')
    remove_debris = fields.Selection(select_options, 'Remove debris')
    prevent_cross_contact = fields.Selection(select_options, 'Prevent Cross contact')
    maintain_log = fields.Selection(select_options, 'Maintain Log')
    maintain_h2o2 = fields.Selection(select_options, 'Maintain H2O2')
    cip_procedures = fields.Selection(select_options, 'CIP Procedures')
    clean_and_sanitize_equipment = fields.Selection(select_options, 'Clean and Sanitize equipment')
    pallets = fields.Selection(select_options, 'Pallets')
    production_supplies = fields.Selection(select_options, 'Production Supplies')
    maintain_bags = fields.Selection(select_options, 'Maintain bags')
    hygiene_practices_and_procedures = fields.Selection(select_options, 'hygiene practices, and procedures')
    identifiy_issues = fields.Selection(select_options, 'Identifiy issues')
