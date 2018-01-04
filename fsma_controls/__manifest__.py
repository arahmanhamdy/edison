{
    'name': 'FSMA Controls',
    'author': 'Creatify',
    'website': 'http://www.creatify.xyz',
    'sequence': 1,
    'depends': ["mrp", "stock"],
    'data': [
        'views/res_partner_view.xml',
        'views/stock_picking_view.xml',
        'views/restroom_log_view.xml',
        'views/lab_submission_view.xml',
        'views/foreign_material_view.xml',
        'views/pre_production_check_view.xml',
        'views/production_check_view.xml',
        'views/post_production_check_view.xml',
        'views/menu_view.xml',
        'report/report_deliveryslip.xml',
        'report/post_production_report.xml',
        'report/restroom_log_report.xml',
        'security/fsma_security.xml',
        'security/ir.model.access.csv',
    ],
}
