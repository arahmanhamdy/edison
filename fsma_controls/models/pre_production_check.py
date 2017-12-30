from odoo import models, fields, api


class PreProductionCheck(models.Model):
    _name = "pre.production.check"
    _rec_name = "id"

    select_options = [
        ("acc", "Acceptable inspection"),
        ("dev", "Deviation noted requires Corrective Action"),
    ]

    sanitary_procedure = fields.Selection(select_options, "Sanitary Procedure")
    food_contact_surfaces = fields.Selection(select_options, "Food contact surfaces")
    spray_equipment_with_water = fields.Selection(select_options, "Spray equipment with water")
    label_and_store_cleaning_materials = fields.Selection(select_options, "Label and Store cleaning materials")
    atp_swab = fields.Selection(select_options, "ATP Swab")
    transport_equipment = fields.Selection(select_options, "Transport equipment")
    labeling_cleaners = fields.Selection(select_options, "Labeling Cleaners")
    examine_surfaces = fields.Selection(select_options, "Examine Surfaces")
    sanitizing_equipment = fields.Selection(select_options, "Sanitizing Equipment")
    remove_debris = fields.Selection(select_options, "Remove Debris")
    non_food_contact_surfaces = fields.Selection(select_options, "Non food contact surfaces")
    inspect_for_missing_parts = fields.Selection(select_options, "Inspect for missing parts")
    cover_all_electrical_components = fields.Selection(select_options, 'Cover all electrical components')
    inspect_pre_operational_equipment = fields.Selection(select_options, 'Inspect pre-operational equipment')
    apply_cleaner = fields.Selection(select_options, 'Apply Cleaner')
    scrubbing_equipment = fields.Selection(select_options, 'Scrubbing Equipment')
    approved_sanitizer = fields.Selection(select_options, 'Approved Sanitizer')
    spray_equipment_utensils_with_water = fields.Selection(select_options, 'Spray equipment/utensils with water')
    use_appropriate_tools = fields.Selection(select_options, 'Use appropriate tools')
    bulk_product_and_packaging_storage = fields.Selection(select_options, 'Bulk product and packaging storage')
    re_assemble_equipment = fields.Selection(select_options, 'Re-assemble equipment')
    unacceptable_results = fields.Selection(select_options, 'Unacceptable results')
    wipe_production_room_work_tables = fields.Selection(select_options, 'Wipe production room work tables')
    hang_hose = fields.Selection(select_options, 'Hang hose')
    sweep_and_mop_production_floors = fields.Selection(select_options, 'Sweep and mop production floors')
    wipe_down_any_dust = fields.Selection(select_options, 'Wipe Down any Dust')
    sweep_mats_and_mop_as_needed = fields.Selection(select_options, 'Sweep mats and mop as needed')
    wipe_down_all_hand_wash_sinks_daily = fields.Selection(select_options, 'Wipe down all hand wash sinks daily')
    damp_mop_floor_and_wipe_walls = fields.Selection(select_options, 'Damp mop floor and wipe walls')
    allergen_preventive_controls = fields.Selection(select_options, 'Allergen Preventive Controls')
    empty_trash_bins = fields.Selection(select_options, 'Empty trash bins')
    wipe_production_room = fields.Selection(select_options, 'Wipe Production Room')
    wash_trash_bins = fields.Selection(select_options, 'Wash trash bins')
    in_house_monitoring = fields.Selection(select_options, 'In-house monitoring')
    good_manufacturing_practices = fields.Selection(select_options, 'Good Manufacturing Practices')
    sanitize_conveyor_belt = fields.Selection(select_options, 'Sanitize conveyor belt')
    sanitize_all_parts = fields.Selection(select_options, 'Sanitize all parts')
    disassemble_clean_and_sanitize = fields.Selection(select_options, 'Disassemble, clean and sanitize')
