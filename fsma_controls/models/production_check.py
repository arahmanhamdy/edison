from odoo import models, fields, api


class ProductionCheck(models.Model):
    _name = "production.check"
    _rec_name = "id"

    select_options = [
        ("acc", "Acceptable inspection"),
        ("dev", "Deviation noted requires Corrective Action"),
    ]

    warehouse = fields.Selection([("1", "1"), ("2", "2")], "Warehouse")
    illness = fields.Selection(select_options, 'Illness')
    clean_garments = fields.Selection(select_options, 'Clean Garments')
    eating_or_drinking = fields.Selection(select_options, 'Eating or Drinking')
    wash_hands = fields.Selection(select_options, 'Wash Hands')
    food_beverages = fields.Selection(select_options, 'Food, Beverages')
    jewelry_policy = fields.Selection(select_options, 'Jewelry Policy')
    sanitizers_operation = fields.Selection(select_options, 'Sanitizers Operation')
    wash_facilities_supplied = fields.Selection(select_options, 'Wash Facilities Supplied')
    change_rooms = fields.Selection(select_options, 'Change Rooms')
    pest_control = fields.Selection(select_options, 'Pest Control')
    receiving = fields.Selection(select_options, 'Receiving')
    allergen_control = fields.Selection(select_options, 'Allergen Control')
    shipping = fields.Selection(select_options, 'Shipping')
    effective_emp = fields.Selection(select_options, 'Effective EMP')
    fm_control = fields.Selection(select_options, 'FM Control')
    mop_and_broom = fields.Selection(select_options, 'Mop and Broom')
    security = fields.Selection(select_options, 'Security')
    water_delivery = fields.Selection(select_options, 'Water Delivery')
    floors_and_drains = fields.Selection(select_options, 'Floors and Drains')
    walls_doors_and_ceiling = fields.Selection(select_options, 'Walls, Doors and Ceiling')
    exterior_dock = fields.Selection(select_options, 'Exterior Dock')
    dock_doors = fields.Selection(select_options, 'Dock Doors')
    sweep_front = fields.Selection(select_options, 'Sweep Front')
    hvac_filter_replacement = fields.Selection(select_options, 'HVAC Filter Replacement')
    fire_safelty = fields.Selection(select_options, 'Fire Safelty')
    waste_mngt = fields.Selection(select_options, 'Waste Mngt')
    food_processing_areas = fields.Selection(select_options, 'Food Processing Areas')
    inspection_stations = fields.Selection(select_options, 'Inspection Stations')
    storage_areas = fields.Selection(select_options, 'Storage Areas')
    light_fittings_are_clean = fields.Selection(select_options, 'Light Fittings are Clean')
    light_fixtures = fields.Selection(select_options, 'Light Fixtures')
    light_fittings_breakage = fields.Selection(select_options, 'Light Fittings Breakage')
    forklift = fields.Selection(select_options, 'Forklift')
    lockout = fields.Selection(select_options, 'Lockout')
    blade_sharpness = fields.Selection(select_options, 'Blade Sharpness')
    knife_blade = fields.Selection(select_options, 'Knife Blade')
    blade_disposal = fields.Selection(select_options, 'Blade Disposal')
    cutters_and_knives_location = fields.Selection(select_options, 'Cutters and Knives Location')
    key_control = fields.Selection(select_options, 'Key Control')
    haz_comm = fields.Selection(select_options, 'Haz Comm')
    first_aid = fields.Selection(select_options, 'First Aid')
    shelf_stable_packaged_goods = fields.Selection(select_options, 'Shelf Stable Packaged Goods')
    hazardous_chemicals = fields.Selection(select_options, 'Hazardous Chemicals')
    scales = fields.Selection(select_options, 'Scales')
    toolbox_talks = fields.Selection(select_options, 'Toolbox Talks')
    ups = fields.Selection(select_options, 'UPS')
